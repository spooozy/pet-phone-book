# Features Overview

This document provides an overview of the application's functionality, including features that have already been implemented, features in the development process, and options for expanding the functionality.

## Core Features:

### Implemented:

### Not Implemented:

- **Contact List Overview**:
    - User can view all saved contacts in alphabetical order. If contacts are not saved, a corresponding message is displayed.

- **View Contact Details**:
    - User can view all saved details about the selected contact in read-only format.

- **Add New Contact**:
    - User can create a new contact by filling out a form with mandatory fields (name and primary contact method) and additional information (phone number, email, social networks, etc.). 
    - Data validation ensures the correctness of the input, and a confirmation message is displayed upon successful saving.

- **Edit Contact**:
    - The user can edit an existing contact by opening a pre-filled form. After making changes, the user must validate or cancel the changes.

- **Delete Contact**:
    - User can delete a contact with confirmation recieved before deleting to avoid accidental actions.

- **Search Through Contact List**:
    - User can find the desired contact via the search bar, which filters data in real time. 
    - The search is performed by matches of the search query and substrings in the names of contacts.


## Potential implementations:
- Filtering by multiple parameters
- Adding specific contacts to favorites
- Adding an avatar field for a contact
- Grouping contacts by tags
