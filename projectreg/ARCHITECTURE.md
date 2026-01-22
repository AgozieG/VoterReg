# System Architecture & Flow Diagram

## 📊 User Registration Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER REGISTRATION                         │
└─────────────────────────────────────────────────────────────┘
                           ↓
        ┌─────────────────────────────────────┐
        │  Navigate to /register/              │
        └─────────────────────────────────────┘
                           ↓
        ┌─────────────────────────────────────┐
        │  Fill Registration Form:             │
        │  - Firstname                         │
        │  - Surname                           │
        │  - Date of Birth                     │
        │  - Email                             │
        │  - Gender                            │
        │  - Phone                             │
        │  - Marital Status                    │
        │  - RC Number ✨ NEW                  │
        │  - Farm Name                         │
        └─────────────────────────────────────┘
                           ↓
        ┌─────────────────────────────────────┐
        │  Validate RC Number Uniqueness       │
        │  (Check if already exists)           │
        └─────────────────────────────────────┘
                    ↙         ↘
          ✓ Unique      ✗ Duplicate
             ↓                ↓
      ┌──────────────┐  ┌─────────────────────┐
      │ Create Voter │  │ Show Error Message: │
      │ Generate     │  │ "RC number already  │
      │ Unique Number│  │  exists"            │
      │ (12-digit)   │  └─────────────────────┘
      └──────────────┘           ↓
          ↓              Return to form
      ┌──────────────────────────────────┐
      │ Redirect to /register/success/    │
      └──────────────────────────────────┘
             ↓
      ┌──────────────────────────────────┐
      │ Display Success Page:             │
      │ - Greeting with name              │
      │ - Unique Voter Number             │
      │   (shown as dots initially)       │
      │ - Eye icon to show/hide           │
      │ - "Go to Vote" button             │
      │ - "Back to Home" button           │
      └──────────────────────────────────┘
```

## 🗳️ Voting Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      VOTING SYSTEM                           │
└─────────────────────────────────────────────────────────────┘
                           ↓
        ┌─────────────────────────────────────┐
        │  Click "Vote" in Navigation Menu    │
        └─────────────────────────────────────┘
                           ↓
        ┌─────────────────────────────────────┐
        │  Navigate to /vote/                 │
        │                                     │
        │  Enter Credentials:                 │
        │  1. RC Number                       │
        │  2. Unique Voter Number             │
        │  3. Farm Name                       │
        │                                     │
        │  Select a Farmer:                   │
        │  □ Farmer Ahmed   (votes: 0)        │
        │  □ Farmer John    (votes: 0)        │
        │  □ Farmer Mary    (votes: 0)        │
        │  □ Farmer David   (votes: 0)        │
        │                                     │
        │  [Cast Vote Button]                 │
        └─────────────────────────────────────┘
                           ↓
        ┌─────────────────────────────────────┐
        │  Validate Credentials:              │
        │  - Find voter by RC number          │
        │  - Check unique number matches      │
        │  - Check farm name matches          │
        │  - Check if already voted           │
        └─────────────────────────────────────┘
         ↙              ↓              ↘
    ✗ Invalid    ✓ Valid       ✗ Already Voted
       ↓            ↓                  ↓
    Error       ┌─────────────┐   Error Message
    Message     │ Create Vote │   "You have
                │ Record      │   already voted"
                │             │
                │ Increment   │   Return to
                │ Farmer      │   voting page
                │ votes_count │
                └─────────────┘
                       ↓
        ┌─────────────────────────────────────┐
        │  Redirect to /vote/results/         │
        └─────────────────────────────────────┘
                       ↓
        ┌─────────────────────────────────────┐
        │  Display Results Page:              │
        │                                     │
        │  🏆 Current Leader:                 │
        │     [Farmer with most votes]        │
        │                                     │
        │  Statistics:                        │
        │  - Total Votes: N                   │
        │  - Farmers Running: 4               │
        │                                     │
        │  Vote Rankings:                     │
        │  🥇 1st: Farmer A (25%)  ████       │
        │  🥈 2nd: Farmer B (15%)  ██        │
        │  🥉 3rd: Farmer C (35%)  ██████     │
        │  #4:    Farmer D (25%)  ████       │
        │                                     │
        │  [Vote Again] [Back to Home]        │
        └─────────────────────────────────────┘
```

## 🗄️ Database Relationships

```
┌─────────────────────────────┐
│         VOTER               │
├─────────────────────────────┤
│ id (PK)                     │
│ firstname                   │
│ surname                     │
│ dob                         │
│ email                       │
│ gender                      │
│ phone                       │
│ marital_status              │
│ rc_number (UNIQUE) ✨       │
│ unique_voter_number (INDEX) │
│ mine_name                   │
│ created_at                  │
└──────────────┬──────────────┘
               │ (1:1)
               ├─────────────────┐
               │                 │
               ↓                 ↓
        ┌─────────────┐   ┌──────────────┐
        │    VOTE     │   │    FARMER    │
        ├─────────────┤   ├──────────────┤
        │ id (PK)     │   │ id (PK)      │
        │ voter_id (FK)── │ name (UNIQUE)│
        │ farmer_id (FK)──│ description  │
        │ created_at  │   │ votes_count  │
        └─────────────┘   │ created_at   │
                          └──────────────┘
```

## 🔄 Data Flow Diagram

```
┌──────────────────────────────────────────────────────┐
│              REGISTRATION MODULE                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Input: Form Data                                    │
│    ↓                                                 │
│  Validate RC Uniqueness                              │
│    ↓                                                 │
│  Generate unique_voter_number (12-digit random)      │
│    ↓                                                 │
│  Create Voter Record                                 │
│    ↓                                                 │
│  Output: Unique Voter Number                         │
│         (Displayed in success page)                  │
│                                                      │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│              VOTING MODULE                           │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Input: Credentials (RC, Unique#, Farm Name)         │
│         Farmer Choice                                │
│    ↓                                                 │
│  Query Voter by RC Number                            │
│    ↓                                                 │
│  Validate: unique_voter_number matches               │
│    ↓                                                 │
│  Validate: mine_name (farm name) matches             │
│    ↓                                                 │
│  Check: Vote doesn't already exist (OneToOne)        │
│    ↓                                                 │
│  Create Vote Record                                  │
│    ↓                                                 │
│  Increment Farmer votes_count                        │
│    ↓                                                 │
│  Output: Redirect to Results Page                    │
│                                                      │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│              RESULTS MODULE                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Query: All Farmers ordered by votes_count (DESC)    │
│    ↓                                                 │
│  Find: Farmer with highest votes_count (winner)      │
│    ↓                                                 │
│  Calculate: Vote percentages (votes/total)           │
│    ↓                                                 │
│  Output: Ranked list with percentages                │
│          Winner highlighted with 🏆 badge           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 🚀 API Endpoints

```
GET /                          → Home page
GET /register/                 → Registration form
POST /register/                → Process registration
GET /register/success/         → Success with unique number
GET /vote/                     → Voting form
POST /vote/submit/             → Process vote
GET /vote/results/             → Show results

GET /admin/login/              → Admin login
POST /admin/login/             → Process admin login
GET /admin/dashboard/          → Admin dashboard
POST /admin/delete/<id>/       → Delete voter
GET /admin/logout/             → Admin logout
```

## 📱 Page Views

```
┌──────────────────────────────────────┐
│         HOME PAGE                    │
│  ┌────────────────────────────────┐  │
│  │ Navigation:                    │  │
│  │ [About] [How to Register]      │  │
│  │ [Why Vote] [Register] [Vote]⭐ │  │
│  │ [Admin]                        │  │
│  └────────────────────────────────┘  │
│  ┌────────────────────────────────┐  │
│  │ Hero Section                   │  │
│  │ - Tagline                      │  │
│  │ - [Begin Registration]         │  │
│  │ - [Learn More]                 │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
                ↓
        ┌──────────────────────────┐
        │   REGISTER PAGE          │
        │ [Form with RC field]     │
        └──────────────────────────┘
                ↓
    ┌────────────────────────────────┐
    │   REGISTRATION SUCCESS        │
    │ ┌─────────────────────────────┐│
    │ │ ✓ Registration Successful! ││
    │ │                             ││
    │ │ Your Unique Voter Number:   ││
    │ │ ••••••••••••  [👁️ Show]     ││
    │ │                             ││
    │ │ [Back to Home] [Go to Vote] ││
    │ └─────────────────────────────┘│
    └────────────────────────────────┘
                ↓
        ┌──────────────────────────┐
        │   VOTE PAGE              │
        │ ┌──────────────────────┐ │
        │ │ Credentials:         │ │
        │ │ [RC Number]          │ │
        │ │ [Unique Number]      │ │
        │ │ [Farm Name]          │ │
        │ └──────────────────────┘ │
        │ ┌──────────────────────┐ │
        │ │ Select Farmer:       │ │
        │ │ □ Farmer Ahmed  (0)  │ │
        │ │ □ Farmer John   (0)  │ │
        │ │ □ Farmer Mary   (0)  │ │
        │ │ □ Farmer David  (0)  │ │
        │ │ [Cast Vote]          │ │
        │ └──────────────────────┘ │
        └──────────────────────────┘
                ↓
    ┌────────────────────────────────┐
    │   RESULTS PAGE                 │
    │ ┌─────────────────────────────┐│
    │ │ 🎉 Thank You for Voting!   ││
    │ │                             ││
    │ │ 🏆 Current Leader:          ││
    │ │    Farmer X (15 votes)      ││
    │ │                             ││
    │ │ 🥇 1st: Farmer X (40%) ████││
    │ │ 🥈 2nd: Farmer Y (30%) ███ ││
    │ │ 🥉 3rd: Farmer Z (20%) ██  ││
    │ │ #4:    Farmer W (10%) █    ││
    │ │                             ││
    │ │ [Vote Again] [Back to Home] ││
    │ └─────────────────────────────┘│
    └────────────────────────────────┘
```

## 🔐 Security Flow

```
REGISTRATION:
User Input → Form Validation → RC Uniqueness Check
    ↓
If Duplicate: Show Error & Return Form
    ↓
If Valid: Generate Unique Number → Save to DB
    ↓
Display Success Page with Unique Number

VOTING:
User Credentials → Query Database → Credential Match Check
    ↓
If No Match: Show Error & Return Form
    ↓
If Voted Already: Show Error & Return Form
    ↓
If Valid: Create Vote → Update Vote Count
    ↓
Show Results Page
```

---

**System Status**: ✅ Fully Functional  
**Last Updated**: January 22, 2026
