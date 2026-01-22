from django.urls import path
from .views import home, register, register_success, admin_login, admin_dashboard, delete_voter, admin_logout, vote, submit_vote, voting_results

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/success/', register_success, name='register_success'),
    path('vote/', vote, name='vote'),
    path('vote/submit/', submit_vote, name='submit_vote'),
    path('vote/results/', voting_results, name='voting_results'),
    path('login/', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('delete/<int:voter_id>/', delete_voter, name='delete_voter'),
    path('logout/', admin_logout, name='admin_logout'),
]