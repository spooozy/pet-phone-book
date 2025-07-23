# Features Overview

## Core Features:
- **Contact List Overview [Under development]**:
    - User can see all saved contacts in alphabetical order.
- **View Contact Details [Under development]**:
    - User can view all saved details about selected contact.
- **Add New Contact [Under development]**:
    - User can create a new contact with different communication methods (phone number, email, Telegram, Instagram, etc.) and additional info such as date of birth, place of work and address.
- **Edit Contact [Under development]**:
    - User can edit contacts by changing saved data or adding new ones.
- **Delete Contact [Under development]**:
    - User can delete a contact with confirmation recieved before deleting to avoid accidental actions.
- **Search Through Contact List[Under development]**:
    - User can find the contact he is interested in through the search bar by full name.

## More About PhoneBook Features:
## 1. Contact List Overview
- Displays all contacts in alphabetical order upon app launch.
- Shows a message if no contacts saved.

## 2. Contact Operations
### 2.1 Add Contact
- Click on "Add Contact" opens a form with:
    - Required Fields:
        - Name.
        - Priority method of communication (phone number field is shown, other fields available with pressing “Alternative ways of communication” button).
    - Optional Fields.
- Validation:
    - If fields are invalid, errors are highlighted with descriptive messages.
- Save Flow:
    - On successful save -> confirmation message -> redirect to contact list.
    - On cancel -> form resets -> return to contact list.

### 2.2 Edit Contact
- Initiation:
    - Clicking "Edit" button opens a pre-filled form with existing contact data.
- Validation:
    - Incorrect fields are highlighted with error messages.
- Save Flow:
    - On save -> validation -> DB update -> success message -> return to contact details view.
- Cancel Flow:
    - Confirmation dialog:
        - Yes -> reset form -> return to contact details view.
        - No -> resume editing.

### 2.3 Delete Contact
- Initiation: 
    - Clicking "Delete" button triggers a confirmation:
        - Confirm -> contact removed -> success message -> return to contact list.
        - Cancel -> return to contact list without changes.

### 2.4 View Contact Details
- Display:
    - All saved contact fields are shown in a read-only view.

## 3. Contact Search
- Search Bar: Input field at the top of the contact list.
- Functionality:
    - Real-time filtering by name (case-insensitive).
    - If no matches -> "No results found for '[query]'".

## Out of Scope for MVP
- Filtering by multiple parameters
- Adding specific contacts to favorites
- Adding an avatar field for a contact
- Grouping contacts by tags
