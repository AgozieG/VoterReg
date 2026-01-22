from django.shortcuts import render, redirect
from .forms import VoterForm
from .models import Voter, Farmer, Vote
from django.contrib import messages
from django.db.models import Q, Count
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'appreg/home.html')

def register(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        # Check if RC number already exists
        rc_number = request.POST.get('rc_number', '').strip()
        if Voter.objects.filter(rc_number=rc_number).exists():
            messages.error(request, 'This RC number already exists. Please use a different RC number.')
            return render(request, 'appreg/register.html', {'form': form})
        
        if form.is_valid():
            try:
                voter = form.save()
                # Store unique number in session to show on success page
                request.session['unique_voter_number'] = voter.unique_voter_number
                request.session['voter_name'] = voter.firstname
                return redirect('register_success')
            except IntegrityError:
                messages.error(request, 'An error occurred. This RC number may already be registered.')
                form = VoterForm()
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VoterForm()
    
    return render(request, 'appreg/register.html', {'form': form})

def register_success(request):
    unique_number = request.session.get('unique_voter_number', '')
    voter_name = request.session.get('voter_name', '')
    context = {
        'unique_number': unique_number,
        'voter_name': voter_name,
    }
    return render(request, 'appreg/register_success.html', context)

# Voting views
def vote(request):
    farmers = Farmer.objects.all()
    context = {'farmers': farmers}
    return render(request, 'appreg/vote.html', context)

def submit_vote(request):
    if request.method == 'POST':
        rc_number = request.POST.get('rc_number', '').strip()
        unique_number = request.POST.get('unique_number', '').strip()
        farm_name = request.POST.get('farm_name', '').strip()
        farmer_id = request.POST.get('farmer_id', '')
        
        # Validate that voter exists and credentials match
        try:
            voter = Voter.objects.get(rc_number=rc_number, unique_voter_number=unique_number, mine_name=farm_name)
        except Voter.DoesNotExist:
            messages.error(request, 'Invalid RC Number, Unique Number, or Farm Name. Please check your details and try again.')
            farmers = Farmer.objects.all()
            return render(request, 'appreg/vote.html', {'farmers': farmers})
        
        # Check if voter has already voted
        if Vote.objects.filter(voter=voter).exists():
            messages.error(request, 'You have already voted. Each voter can only vote once.')
            farmers = Farmer.objects.all()
            return render(request, 'appreg/vote.html', {'farmers': farmers})
        
        # Get farmer and record vote
        try:
            farmer = Farmer.objects.get(id=farmer_id)
            vote = Vote.objects.create(voter=voter, farmer=farmer)
            farmer.votes_count += 1
            farmer.save()
            
            # Redirect to results page
            return redirect('voting_results')
        except Farmer.DoesNotExist:
            messages.error(request, 'Selected farmer not found.')
            farmers = Farmer.objects.all()
            return render(request, 'appreg/vote.html', {'farmers': farmers})
    
    return redirect('vote')

def voting_results(request):
    # Get the farmer with the highest votes
    farmers = Farmer.objects.all().order_by('-votes_count')
    total_votes = Vote.objects.count()
    
    winner = farmers.first() if farmers.exists() else None
    
    context = {
        'winner': winner,
        'farmers': farmers,
        'total_votes': total_votes,
    }
    return render(request, 'appreg/voting_results.html', context)

# Admin Views
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'appreg/admin_login.html')

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        messages.error(request, 'Please login first.')
        return redirect('admin_login')
    
    voters = Voter.objects.all().order_by('-created_at')
    voters_count = voters.count()
    male_count = voters.filter(gender='M').count()
    female_count = voters.filter(gender='F').count()
    
    context = {
        'voters': voters,
        'voters_count': voters_count,
        'male_count': male_count,
        'female_count': female_count,
    }
    
    return render(request, 'appreg/admin_dashboard.html', context)

def delete_voter(request, voter_id):
    if not request.session.get('admin_logged_in'):
        messages.error(request, 'Please login first.')
        return redirect('admin_login')
    
    try:
        voter = Voter.objects.get(id=voter_id)
        voter_name = f"{voter.firstname} {voter.surname}"
        voter.delete()
        messages.success(request, f'Voter {voter_name} has been deleted successfully.')
    except Voter.DoesNotExist:
        messages.error(request, 'Voter not found.')
    
    return redirect('admin_dashboard')

def admin_logout(request):
    request.session['admin_logged_in'] = False
    messages.success(request, 'You have been logged out.')
    return redirect('home')