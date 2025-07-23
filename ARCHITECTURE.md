# Pet Phonebook Architecture Documentation

## [Schema Diagram](https://www.canva.com/design/DAGtzGozkwY/_G3aM1M_RUiBtUu8ZQVY5g/edit)

### User Interface Layer

#### Specific Contact 
**Header**:
- Displays contact name (name/surname/patronymic)
  
**Contact Information**:
- Telephone number
- Email address
- Messaging apps (Telegram, Vkontakte, Facebook, Instagram)
  - Each method shows relevant contact data for quick communication

**Additional Fields**:
- Birthday
- Workplace
- Address
- Notes

**Actions**:
- Edit
- Delete
- Back to `<contact list>`

#### Contact List 
**Header Section**:
- Title: "Pet Phone"
- Search bar
- "Add Contact" button

**Main Content Area**:
- When contacts exist:
  - Alphabetically sorted list (A→Z)
  - Each contact card displays contact name
- Empty state:
  - "No contacts" message
  - "Create first contact" prompt

#### Contact Form 
**Required Fields**:
- Contact name
- Communication methods (at least one required)

**Optional Fields**:
- Birthday (date picker)
- Workplace (multi-line field)
- Address (multi-line field)
- Notes (free-form text)

**Actions**:
- Save contact
- Back to `<contact list>`

### Business Logic Layer

#### ID Handling
- Primary contact identifier in database

#### Contact List Flow
1. `show contact list`:
   - Calls `<get contact list>` or `<find contact>`
   - Accepts all parameters from these requests
   - Transfers data to `<contact list>` page

2. `show specific contact`:
   - Calls `<get contact>`
   - Accepts all parameters from these requests
   - Transfers data to `<specific contact>` page


3. `get contact list`:
   - Application startup
   - Makes database request (no parameters)
   - Retrieves list with fields:
     - ID
     - Contact name
   - Passes full list to `<show contact list>`

4. `find contact`:
   - Activated from search bar
   - Makes database request with:
     - Search string content
   - Returns filtered list (ID + name)
   - Passes results to `<show contact list>`

#### Contact Management Flows
1. `get contact`:
   - Triggered by contact selection
   - Database request with:
     - ID parameter
   - Returns full contact info including:
     - Name
     - Communication methods
     - Additional fields
   - Passes data to `<show specific contact>`

2. `delete contact`:
   - Initiated from `specific contact`
   - Database request with:
     - ID parameter
   - Returns operation status
   - Redirects to `<get contact list>`

3. `update contact`:
   - Initiated from `specific contact`
   - Database request with:
     - User-selected field updates
   - Returns operation status
   - Redirects to `<get contact>`

4. `add contact`:
   - Initiated from contact form
   - Database request with:
     - Required fields (name + ≥1 communication method)
     - Optional fields
   - Returns operation status
   - Redirects to `<get contact>`
