# Quick Start Guide

## Setup (First Time Only)

1. **Activate Virtual Environment**
   ```bash
   # On Windows
   superenv\Scripts\activate
   ```

2. **Navigate to Project**
   ```bash
   cd projectreg
   ```

3. **Run Migrations** (already done)
   ```bash
   python manage.py migrate
   ```

4. **Create Farmers** (already done)
   ```bash
   python create_farmers.py
   ```

## Running the Application

1. **Start Development Server**
   ```bash
   python manage.py runserver 8000
   ```

2. **Open in Browser**
   ```
   http://127.0.0.1:8000
   ```

## Testing the Full Flow

### Step 1: Register a Voter
- Click "Register" button
- Fill in all required fields:
  - Surname: e.g., "Okoro"
  - First Name: e.g., "John"
  - Date of Birth: Select date
  - Email: e.g., user@example.com
  - Gender: Select option
  - Phone: e.g., +2348012345678
  - Marital Status: Select option
  - **RC Number**: e.g., "RC123456" (Must be unique!)
  - Farm Name: e.g., "Green Valley Farm"
- Click "Register" button

### Step 2: Save Your Unique Number
- On success page, you'll see your Unique Voter Number
- Click the eye icon (👁️) to view it
- **Write it down or remember it** - you'll need it to vote!
- The number format is 12 digits

### Step 3: Go to Vote
- Click "Vote" in the menu
- Enter your credentials:
  - RC Number: The one you registered with
  - Unique Voter Number: From the success page
  - Farm Name: The farm name you registered with
- All three must match exactly!

### Step 4: Select Farmer
- Choose one of the 4 farmers:
  1. Farmer Ahmed
  2. Farmer John
  3. Farmer Mary
  4. Farmer David
- Click "Cast Vote"

### Step 5: View Results
- You'll see:
  - Current winner (🏆)
  - Vote count for each farmer
  - Vote distribution percentage
  - Ranking of all farmers

## Admin Panel

Access admin at: `http://127.0.0.1:8000/admin/`

Default credentials:
- Username: `admin`
- Password: `admin123`

Can view:
- All registered voters
- All farmers and their vote counts
- All individual votes cast
- Delete voters if needed

## Troubleshooting

### "This RC number already exists"
- The RC number you entered was already registered
- Try a different RC number

### "Invalid RC Number, Unique Number, or Farm Name"
- One or more of your credentials don't match your registration
- Check spelling and exact text matches
- Make sure you have the correct Unique Number

### "You have already voted"
- You've already cast your vote
- Each voter can only vote once

### Server won't start
- Make sure you're in the `projectreg` directory
- Verify Python is installed: `python --version`
- Check port 8000 isn't already in use

## Database Reset (if needed)

If you want to start fresh:

1. Delete `db.sqlite3`
2. Delete migration files in `appreg/migrations/` except `__init__.py`
3. Run migrations again:
   ```bash
   python manage.py makemigrations appreg
   python manage.py migrate
   ```
4. Create farmers again:
   ```bash
   python create_farmers.py
   ```

## Key Features

✓ Unique RC Numbers - Prevent duplicate registrations
✓ Unique Voter Numbers - 12-digit number for each voter  
✓ Eye Icon - Toggle visibility of voter number
✓ Vote Menu - Easy access from home page
✓ Credential Validation - Must match registration
✓ One Vote Per Person - Database constraint
✓ Live Results - See winner and vote counts
✓ Admin Dashboard - Manage voters and view statistics

---

**Version**: 1.0
**Last Updated**: January 22, 2026
