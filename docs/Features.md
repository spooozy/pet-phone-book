# Features Overview

This document provides an overview of the application's functionality, including features that have already been implemented and features in the development process.

## Core Features:

### Done:

### In Development:

- **Contact List Overview**:
    - User can view all saved contacts in alphabetical order. If contacts are not saved, a corresponding message is displayed.

- **View Contact Details**:
    - User can view all saved details about the selected contact in read-only format.

- **Add Contact**:
    - User can create a new contact by filling a name and at least one method of communication (phone number, email or Telegram, Instagram, VK and Facebook nickname).
    - User can also save info for all provided methods as well as some additional information (last name, birthday, address, place of work and notes).
    - Data validation ensures that the input is correct, and accompanying messages inform User about successful saving or errors that have occurred.

- **Edit Contact**:
    - User can edit an existing contact by changing a form with the contact data already saved. 
    - Same validation rules and messaging behavior as "Add Contact" apply.
    - After making changes User must confirm or cancel them.

- **Delete Contact**:
    - User can delete all contact data. This action also requires User's confirmation to avoid accidental actions and is accompanied by notification messages.

- **Search Through Contact List**:
    - User can find the desired contact via the search bar, which filters data in real time. 
    - The search is performed by matches of the search query and substrings in the names of contacts.