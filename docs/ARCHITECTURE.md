# Project Architecture

This document outlines the planned architecture for the project and provides high-level details about the system's design.

## Overview

The application will be developed using a layered architecture. This approach separates the application's concerns into three distinct layers, each with a unique responsibility. This separation is chosen to improve maintainability, allow for independent development and testing of each part, and make the overall system easier to understand as it grows.

The three layers are:
- **UI Layer:** Renders UI elements and handles all user interaction (touches, clicks, keyboard input). This layer will contain all components dependent on a specific UI framework and will hold UI triggers that initiate logic and/or navigation events.
- **Controller Layer + Navigation:** Acts as an intermediary, connecting the `UI` and `Logic` layers. It processes requests from the UI, calls the appropriate business logic, and returns the results to the UI for display. Navigation is responsible for routing between screens based on events in the app.
- **Logic Layer:** Contains the core business logic and data entities. It will communicate with the database to perform CRUD (Create, Read, Update, Delete) operations. The database will be a relational SQLite database with full-text search capabilities.

## Architecture Scheme

See the high-level architecture diagram below:

![architecture scheme](./architecture.png)

The diagram shows both the data flow (how data is passed between layers) and the navigation flow (dependencies between UI views). To improve readability, the flow for each specific use case is colored uniquely.

If you need to edit or update the architecture diagram, use the [`draw.io`](https://draw.io) service and the [raw XML file](./architecture.drawio).

## Use Cases and Flows

The sections below contain descriptions for specific use cases. This information accompanies the scheme and should be used as a reference for the visual diagram above.

### Navigation

This subsection describes the relationships between UI views (screens) and their dependencies.

- Upon opening, the app shows the `Contact List` screen.
- Description of the navigation flow for opening the app (follow dashed light green arrows on the scheme):
    - Pre-requisites: The app is launched.
    - Action (trigger): The application finishes loading.
    - Result: The `Contact List` screen is displayed.
- Description of the navigation flow for closing the app:
    - Pre-requisites: The app is open.
    - Action (trigger): The user performs a system action to close the app.
    - Result: The application process is terminated.
- Description of the navigation flow for opening the contact editing screen (follow light purple arrows on the scheme):
    - Pre-requisites: The user is on the `Contact Details` screen.
    - Action (trigger): The user presses the `Edit Contact` button.
    - Result: Navigate to the `Edit Contact` screen, which shows a form pre-filled with the current contact's data.
- Description of the navigation flow for returning to the contact list (follow green arrows on the scheme):
    - Pre-requisites: The user is on the `Contact Details` screen.
    - Action (trigger): The user presses the `Back` button.
    - Result: Navigate to the `Contact List` screen.
- Description of the navigation flow for adding a new contact (follow yellow arrows on the scheme):
    - Pre-requisites: The user is on the `Contact List` screen.
    - Action (trigger): The user presses the `Create New Contact` button.
    - Result: Navigate to the `New Contact` screen with empty input fields.
- Description of the navigation flow for canceling the creation of a new contact (follow purple arrows on the scheme):
    - Pre-requisites: The user is on the `New Contact` screen.
    - Action (trigger): The user presses the `Cancel` button and confirms the action.
    - Result: Navigate back to the `Contact List` screen.
- Description of the navigation flow for viewing a newly created contact (follow orange arrows on the scheme):
    - Pre-requisites: The user is on the `New Contact` screen and has filled in the required fields.
    - Action (trigger): The user presses the `Save Contact` button.
    - Result: After the data is saved, navigate to the `Contact Details` screen to show the information for the newly created contact.
- Description of the navigation flow for viewing a specific contact's details (follow red arrows on the scheme):
    - Pre-requisites: The user is on the `Contact List` screen.
    - Action (trigger): The user taps on a specific contact in the list.
    - Result: Navigate to the `Contact Details` screen to show all stored information for the selected contact.
- Description of the navigation flow for deleting a contact (follow light blue arrows on the scheme):
    - Pre-requisites: The user is on the `Contact Details` screen.
    - Action (trigger): The user presses the `Delete Contact` button and confirms the deletion.
    - Result: Navigate to the `Contact List` screen. The list is updated and no longer shows the deleted contact.
- Description of the navigation flow for canceling the deletion of a contact (follow yellow arrows on the scheme):
    - Pre-requisites: A confirmation dialog for deletion is shown.
    - Action (trigger): The user presses the button to cancel the deletion.
    - Result: The confirmation dialog is dismissed, and the user remains on the `Contact Details` screen.
- Description of the navigation flow for saving an updated contact (follow dashed magenta arrows on the scheme):
    - Pre-requisites: The user is on the `Edit Contact` screen and has changed some information.
    - Action (trigger): The user presses the `Save Contact` button.
    - Result: After the data is saved, navigate to the `Contact Details` screen to show the updated information.
- Description of the navigation flow for canceling an update (follow dark blue arrows on the scheme):
    - Pre-requisites: The user is on the `Edit Contact` screen.
    - Action (trigger): The user presses the `Cancel` button and confirms the action.
    - Result: Navigate back to the `Contact Details` screen without saving any changes.

### Data Flow

This subsection describes how data is passed between layers and components.

#### Data Models
The following data models, which correspond to the database schema, will be used.

- `CommunicationMethod` struct:
    - id_contact (Integer)
    - type (String)
    - value (String)
- `ContactFullDetails` struct:
    - id_contact (Integer)
    - name (String)
    - birthday (String, format "YYYY-MM-DD")
    - workplace (String)
    - address (String)
    - notes (String)
- `ContactShortDetails` struct:
    - id_contact (Integer)
    - name (String)

#### Data Flow Descriptions

- Description of the data flow for displaying all contacts (follow dashed light green arrows on the scheme):
    - Pre-requisites: The user navigates to the `Contact List` screen.
    - Action (trigger): The `Contact List` screen appears.
    - Result:
        - The UI calls a method in the controller to get all contacts, expecting a list of `ContactShortDetails` objects.
        - The logic layer retrieves a sorted list of all contacts from the database.
        - The logic layer maps the results to an array of `ContactShortDetails` structs and returns it.
        - The UI layer receives the data and displays the list of contacts or a "No contacts" message.
- Description of the data flow for creating a new contact (follow orange arrows on the scheme):
    - Pre-requisites: The user is on the `New Contact` screen.
    - Action (trigger): The user fills out the form and presses the `Save Contact` button.
    - Result:
        - The UI layer gathers the data into a `ContactFullDetails` object.
        - The UI calls the controller to add a new contact, passing the object.
        - The logic layer validates the data and performs the necessary `INSERT` operations into the database.
        - The logic layer returns the complete `ContactFullDetails` object, which is then passed to the `Contact Details` screen for display.
- Description of the data flow for viewing contact details (follow lime or light green arrows on the scheme):
    - Pre-requisites: The user is on the `Contact List` screen.
    - Action (trigger): The user taps on a contact.
    - Result:
        - The UI layer gets the `id_contact` of the selected item.
        - The UI calls the controller to get details for the specified contact ID.
        - The logic layer performs `SELECT` operations to gather all information for the given contact.
        - The logic layer assembles the data into a single `ContactFullDetails` struct and returns it.
        - The UI layer receives the object and displays its data on the `Contact Details` screen.
- Description of the data flow for finding contacts by name (follow blue arrows on the scheme):
    - Pre-requisites: The user is on the `Contact List` screen.
    - Action (trigger): The user types a search query into the search field.
    - Result:
        - With each change, the UI calls the controller to filter contacts by the search query.
        - The logic layer queries the full-text search index of the database.
        - The results are returned as an array of `ContactShortDetails` and displayed in the UI.
- Description of the data flow for updating a contact (follow dashed magenta arrows on the scheme):
    - Pre-requisites: The user is on the `Edit Contact` screen.
    - Action (trigger): The user modifies the form and presses the `Save Contact` button.
    - Result:
        - The UI layer gathers all data into a `ContactFullDetails` object.
        - The UI calls the controller to update the contact with the new data.
        - The logic layer performs the necessary `UPDATE`, `DELETE`, and `INSERT` operations on the database to reflect the changes.
        - The updated `ContactFullDetails` object is returned and displayed on the `Contact Details` screen.
- Description of the data flow for removing a contact (follow light blue arrows on the scheme):
    - Pre-requisites: The user is on the `Contact Details` screen.
    - Action (trigger): The user presses the `Delete Contact` button and confirms the action.
    - Result:
        - The UI layer gets the `id_contact` of the current contact.
        - The UI calls the controller to delete the contact.
        - The logic layer performs a `DELETE` operation for the contact.
        - Related records are automatically deleted by the database due to the `ON DELETE CASCADE` constraint.
        - The app navigates to the `Contact List` screen, which refreshes to show the updated list.