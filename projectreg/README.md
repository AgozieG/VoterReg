# Farmer Voting Registration System

## 🎯 Project Overview

This is a comprehensive voting system for farmer registration where:
- Users register with a unique **RC Number** 
- They receive a unique **12-digit Voter Number**
- They can vote for one of **4 farmers**
- Results show the **winning farmer** with vote distribution

## ✨ What's New

### Replaced "State" with "RC Number"
- Removed the `state` field from the registration form
- Added `rc_number` as a unique identifier
- Prevents duplicate registrations with the same RC number

### Unique Voter Number System
- Each registered voter gets a unique 12-digit number
- Displayed on success page with dots (••••••••••••)
- Eye icon allows users to view/hide the number
- Required for voting process

### Complete Voting System
- **Vote Menu**: Added to home page navigation
- **Voting Form**: Requires RC Number + Unique Number + Farm Name
- **Farmer Selection**: Choose from 4 farmers (Ahmed, John, Mary, David)
- **Validation**: All credentials must match registration record
- **One Vote Per Person**: Database constraint prevents double voting
- **Results Page**: Shows winner (🏆) and vote distribution

## 📁 Project Structure

```
projectreg/
├── manage.py
├── create_farmers.py          # Script to create 4 farmers
├── IMPLEMENTATION_SUMMARY.md  # Technical details
├── QUICK_START.md            # User guide
├── db.sqlite3                # Database
├── projectreg/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── appreg/
    ├── models.py             # Updated with new fields and models
    ├── views.py              # Added voting views
    ├── urls.py               # Added voting routes
    ├── forms.py              # Updated registration form
    ├── admin.py              # Updated admin interface
    ├── migrations/
    │   └── 0001_initial.py   # Database migrations
    ├── templates/appreg/
    │   ├── home.html                 # Added Vote link
    │   ├── register.html             # Updated with RC number
    │   ├── register_success.html     # Shows unique voter number
    │   ├── vote.html                 # NEW - Voting page
    │   ├── voting_results.html       # NEW - Results page
    │   ├── admin_dashboard.html
    │   ├── admin_login.html
    │   └── base.html
    └── static/
        └── appreg/
            ├── style1.css
            ├── style4.css
            └── script1.js
```

## 🗄️ Database Models

### Voter Model (Updated)
```python
- firstname: CharField
- surname: CharField
- dob: DateField
- email: EmailField
- gender: CharField (choices)
- phone: CharField
- marital_status: CharField (choices)
- rc_number: CharField (unique) ✨ NEW
- unique_voter_number: CharField (indexed) ✨ NEW
- mine_name: CharField
- created_at: DateTimeField
```

### Farmer Model ✨ NEW
```python
- name: CharField (unique)
- description: TextField
- votes_count: IntegerField (default: 0)
- created_at: DateTimeField
```

### Vote Model ✨ NEW
```python
- voter: OneToOneField (Voter)
- farmer: ForeignKey (Farmer)
- created_at: DateTimeField
```

## 🔐 Validation Rules

### Registration
- RC Number must be unique (prevents duplicate registration)
- If RC exists: "This RC number already exists"

### Voting
- RC Number must exist in database
- Unique Number must match the voter's record
- Farm Name must match the voter's record
- Must not have already voted

Error messages for invalid credentials:
```
"Invalid RC Number, Unique Number, or Farm Name. 
Please check your details and try again."
```

## 📊 Voting Features

### Vote Page (`/vote/`)
- Three credential fields (RC, Unique Number, Farm Name)
- Four farmer cards showing current vote counts
- Selected farmer highlighted in blue
- Submit button to cast vote

### Results Page (`/vote/results/`)
- 🏆 Current leader with gold badge
- Total votes cast counter
- Number of farmers running
- Complete ranking table:
  - Rank (with medal emoji: 🥇 🥈 🥉)
  - Farmer name
  - Vote count (in blue)
  - Vote distribution bar with percentage

## 🚀 Getting Started

### 1. First Time Setup
```bash
# Navigate to project
cd projectreg

# Activate virtual environment
superenv\Scripts\activate  # Windows

# Install dependencies (if needed)
pip install django==5.2.8

# Run migrations
python manage.py migrate

# Create farmers
python create_farmers.py
```

### 2. Start Server
```bash
python manage.py runserver 8000
```

### 3. Open Application
```
http://127.0.0.1:8000
```

## 📋 Usage Flow

1. **User Registers**
   - Fills registration form
   - Enters RC Number (must be unique)
   - Submits registration

2. **Registration Success**
   - Shows unique 12-digit voter number
   - Eye icon to show/hide number
   - Links to vote page or home

3. **User Votes**
   - Click "Vote" in menu
   - Enter RC Number
   - Enter Unique Voter Number
   - Enter Farm Name
   - Select a farmer
   - Click "Cast Vote"

4. **View Results**
   - See current winner with 🏆
   - View vote counts
   - See vote distribution percentages

## 🛠️ Admin Dashboard

Access at `/admin/`
- Username: `admin`
- Password: `admin123`

Admin can:
- View all voters with RC numbers
- View unique voter numbers
- Search voters by RC, name, email, farm
- View all farmers and vote counts
- View all votes cast
- Delete voters if needed
- Filter by various criteria

## 🔄 Farmer Presets

4 farmers are created:
1. **Farmer Ahmed** - Crop cultivation & sustainable farming
2. **Farmer John** - Organic farming & animal husbandry
3. **Farmer Mary** - Vegetable farming & market gardening
4. **Farmer David** - Modern farming techniques & technology

## 📝 File Changes Summary

| File | Change | Status |
|------|--------|--------|
| models.py | Added Farmer, Vote models; updated Voter | ✓ |
| forms.py | Replaced state → rc_number | ✓ |
| views.py | Added vote(), submit_vote(), voting_results() | ✓ |
| urls.py | Added voting routes | ✓ |
| admin.py | Updated for new models | ✓ |
| home.html | Added Vote menu link | ✓ |
| register.html | Updated to use rc_number | ✓ |
| register_success.html | Shows unique voter number with eye icon | ✓ |
| vote.html | NEW - Voting page | ✓ |
| voting_results.html | NEW - Results display | ✓ |

## 🎨 UI/UX Features

- **Blue theme** for voting-related buttons and highlights
- **Eye icon** (👁️) to toggle unique number visibility
- **Medal emojis** (🥇🥈🥉) for ranking
- **Gold badge** (🏆) for winner
- **Progress bars** showing vote distribution with percentages
- **Responsive design** with card-based layout
- **Error messages** for validation failures
- **Success messages** for completed actions

## 🔒 Security

- RC number uniqueness enforced at database level
- One vote per voter enforced with OneToOne relationship
- Credential validation on every vote attempt
- Admin panel protected with password
- SQL injection prevention via Django ORM
- CSRF protection on forms

## 📈 Scalability

- Vote counts tracked efficiently
- IndexDB on unique_voter_number for fast lookups
- Foreign key relationships for data integrity
- Can handle hundreds of voters and votes

## 🐛 Error Handling

```
Registration:
- "This RC number already exists"

Voting:
- "Invalid RC Number, Unique Number, or Farm Name"
- "You have already voted"
- "Selected farmer not found"

General:
- Database integrity errors prevented
- Form validation on both client and server
```

## 📞 Support

For issues:
1. Check QUICK_START.md for troubleshooting
2. Verify all credentials match registration
3. Check admin panel for data
4. Reset database if needed (see QUICK_START.md)

---

**Status**: ✅ Fully Implemented & Ready to Deploy  
**Version**: 1.0  
**Last Updated**: January 22, 2026  
**Django Version**: 5.2.8  
**Python Version**: 3.10+
