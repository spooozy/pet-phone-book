# Project Architecture

The document describes an architecture of the project and high-level details about how the app works.


## Overview

The app is cut into virtual layers. Each layer has a unique responsibility:
- UI Layer: renders UI elements and handles interaction from a user (touches, clicks, input from a keyboard). Here lies all elements that depends on a UI framework. The UI layer contains `UI triggers` which trigger logic and/or navigation events.
- Controller Layer + Navigation: glues `UI` and `Logic` layers. Here should be performed all calls to the UI and logic. Navigation is responsible for routing between screens when something happens in the app (update in database or user interaction). The layer is optional and depends on implementation.
- Logic Layer: contains business logic and entities. Also communicates with relational DB storage and performs CRUD operations over the storage. The DB is a relational DB with an ability to make a full-text search to meet feature requirements.

## Architecture scheme

See the high-level architecture below (as a diagram):

![architecture scheme](./architecture.png)

The diagram (scheme) shows the data flow (how the data is passed between layers and components) and navigation flow (dependencies between UI views).
The data flow for the specific use case is coloured with its own colour to simplify tracking and improve readability of the scheme.

If you have to edit/update the architecture, use the [`draw.io`](https://draw.io) service and the [raw XML file](./architecture.drawio).

## Use cases and its flows

Sections below contain description and details of the architecture for specific use cases. The details complement the scheme and should be used as a helper to the visual diagram above.
Each flow corresponds to the visual path on a scheme with a specific colour (see notes in paranthesis).

### Navigation

The subsection describes the relations between UI views (screens) and their dependencies.
Given the navigation flow you have to understand what screen can open another one.

- Upon opening, the app shows the “Contact List” screen.
- Description of the navigation flow for the use case: a user can open the app and see the list of stored contacts (follow dashed light green arrows on scheme):
    - pre-requisites: App is launched.
    - action (trigger): The application finishes loading.
    - result: The `"Contact List"` screen is displayed.
- Description of the navigation flow for the use case: a user can close the app:
    - pre-requisites: The app is open.
    - action (trigger): User performs a system action to close the app (e.g., swipes it away from the recent apps list).
    - result: The application process is terminated.
- Description of the navigation flow for the use case: a user can open a screen where they can edit information about a specific contact (follow light purple arrows on scheme):
    - pre-requisites: User is on the `"Contact details"` screen.
    - action (trigger): Press the `"Edit Contact"` button.
    - result: Navigate to the `"Edit contact"` screen, which shows a form pre-filled with the current contact's data.
- Description of the navigation flow for the use case: while looking at contact details, a user can go back to the full list of contacts (follow green arrows on scheme):
    - pre-requisites: User is on the `"Contact details"` screen.
    - action (trigger): Press the `"Back"` button.
    - result: Navigate to the `"Contact List"` screen.
- Description of the navigation flow for the use case: a user can open a screen where they can add info about a new contact (follow yellow arrows on scheme):
    - pre-requisites: navigate to `"Contact List"` screen.
    - action (trigger): press the `"Create New Contact"` button.
    - result: navigate to the `"New Contact"` screen and show the screen with empty UI fields.
- Description of the navigation flow for the use case: a user can cancel the process of creating of a new contact (follow purple arrows on scheme):
    - pre-requisites: User is on the `"New contact"` screen.
    - action (trigger): Press the `"Cancel"` button and confirm the cancellation.
    - result: Navigate back to the `"Contact List"` screen.
- Description of the navigation flow for the use case: after the successful creation of a new contact, a user can see the details about the contact (follow orange arrows on scheme):
    - pre-requisites: User is on the `"New contact"` screen and has filled in the required fields.
    - action (trigger): Press the `"Save Contact"` button.
    - result: After the data is saved, navigate to the `"Contact details"` screen to show the information for the newly created contact.
- Description of the navigation flow for the use case: a user can open a screen to see a details about the specific contact (follow red arrows on scheme):
    - pre-requisites: User is on the `"Contact List"` screen.
    - action (trigger): Tap on a specific contact in the list.
    - result: Navigate to the `"Contact details"` screen to show all stored information for the selected contact.
- Description of the navigation flow for the use case: after the successful removing of existing contact, a user can see the full list of stored contacts [without the contact that was deleted] (follow light blue arrows on scheme):
    - pre-requisites: User is on the `"Contact details"` screen.
    - action (trigger): Press the `"Delete Contact"` button and confirm the deletion.
    - result: Navigate to the `"Contact List"` screen. The list is updated and no longer shows the deleted contact.
- Description of the navigation flow for the use case: a user can cancel a process of a deletion of the existing contact and open the contact details (follow yellow arrows on scheme):
    - pre-requisites: User has pressed the `"Delete Contact"` button on the `"Contact details"` screen and a confirmation dialog is shown.
    - action (trigger): Press the button to cancel the deletion (e.g., `"Cancel"` or `"No"`).
    - result: The confirmation dialog is dismissed, and the user remains on the `"Contact details"` screen.
- Description of the navigation flow for the use case: a user can update an existing contact and open the contact details with the updated info (follow dashed magenta arrows on scheme):
    - pre-requisites: User is on the `"Edit contact"` screen and has changed some information.
    - action (trigger): Press the `"Save Contact"` button.
    - result: After the data is saved, navigate to the `"Contact details"` screen to show the updated information for the contact.
- Description of the navigation flow for the use case: a user can cancel the process of updating of an existing contact (follow dark blue arrows on scheme):
    - pre-requisites: User is on the `"Edit contact"` screen.
    - action (trigger): Press the `"Cancel"` button and confirm the cancellation.
    - result: Navigate back to the `"Contact details"` screen without saving any changes.

### Data flow

The subsection describes how the data should be passed between layers and components in order to make the app works.
To pass the data within the app, the following models should be used:

```
ContactFullDetails struct:

- id (UUID string or unique integer)
- id_contact (UUID unique integer)
- name (String)
- phone (String)
- additional\_contact ([String])
- birthday (Date)
- address (String)
- workplace (String)
- notes (String)
```

```
ContactShortDescription struct:

- id (UUID string or unique integer)
- name (String)
```


-   Description of the data flow for the use case: a user can see all stored contacts (follow dashed light green arrows on scheme):
    -   pre-requisites: navigate to “Contact List” screen
    -   action (trigger): the "Contact List" appears on the screen.
    -   result:
        -   call `GetAllContacts() -> [ContactShortDescription]` method in the controller layer
            -   pass data received from the `GetAllContacts()` method into the “Contact List” screen or display "No contacts" text, if result array is empty
        -   the `GetAllContacts` method in the logic layer do the following:
            -   perform `SELECT` operation over the DB;
            -   extract all rows with the fields: id, name to form `ContactShortDescription` struct later;
            -   sort results alphabetically by the `name` field;
-   Description of the data flow for the use case: a user can fill the info about a new contact and store it (follow orange arrows on scheme):
    -   pre-requisites: User is on the "New contact" screen.
    -   action (trigger): User fills the form fields and presses the “Save Contact” button.
    -   result:
        -   The UI Layer gathers data from the form into a `ContactFullDetails` object (the `id` field is empty at this point).
        -   Call the `AddNewContact(ContactFullDetails)` method in the controller layer.
        -   The controller layer calls the `CreateNewContact(ContactFullDetails)` method in the logic layer.
        -   The logic layer generates a unique `id`, validates the data, and performs an `INSERT` operation in the DB. It then returns the complete `ContactFullDetails` object (with the new `id`) to the controller, which passes it to the UI.
-   Description of the data flow for the use case: a user can get all the stored details about a specific contact (follow lime or light green arrows):
    -   pre-requisites: User is on the "Contact List" screen.
    -   action (trigger): User taps on a specific contact from the list.
    -   result:
        -   The UI layer captures the `id` of the selected contact.
        -   Call the `Get contact details(id)` method in the controller layer.
        -   The controller layer calls the `Get contact details(id)` method in the logic layer.
        -   The logic layer performs a `SELECT *` operation over the DB for the given `id`, populates a `ContactFullDetails` struct with the retrieved data, and returns it.
        -   The UI layer receives the `ContactFullDetails` object and displays its data on the "Contact details" screen.
-   Description of the data flow for the use case: a user can find contacts by their name (follow blue arrows):
    -   pre-requisites: User is on the "Contact List" screen.
    -   action (trigger): User types a search query into the "Find Contact" field.
    -   result:
        -   With each change in the input field, the UI layer calls the `Filter contacts(searchQuery)` method in the controller layer.
        -   The controller layer calls the `Filter contacts(searchQuery)` method in the logic layer.
        -   The logic layer performs a `SELECT id, name` operation over the DB with a `WHERE` clause to find matches (e.g., using `LIKE '%searchQuery%'`).
        -   The results are sorted alphabetically and returned as an array of `ContactShortDescription` objects.
        -   The UI layer updates the contact list on the screen to show only the filtered results.
-   Description of the data flow for the use case: a user can edit/update info about stored contact and save the changes (follow dashed magenta line):
    -   pre-requisites: User is on the "Edit contact" screen.
    -   action (trigger): User modifies the form fields and presses the “Save Contact” button.
    -   result:
        -   The UI layer gathers all data from the form into a `ContactFullDetails` object.
        -   Call the `Update contact details(ContactFullDetails)` method in the controller layer.
        -   The controller layer calls the `Update contact details(ContactFullDetails)` method in the logic layer.
        -   The logic layer performs an `UPDATE` operation over the DB for the record with the matching `id`.
        -   The UI layer receives the updated `ContactFullDetails` object and displays it on the "Contact details" screen.
-   Description of the data flow for the use case: a user can remove a stored contact (follow light blue arrows):
    -   pre-requisites: User is on the "Contact details" screen.
    -   action (trigger): User presses the “Delete Contact” button and confirms the action.
    -   result:
        -   The UI layer gets the `id` of the contact being viewed.
        -   It calls a `DeleteContact(id)` method (not explicitly named but implied by the flow) in the controller layer.
        -   The controller layer calls the corresponding `DeleteContact(id)` method in the logic layer.
        -   The logic layer performs a `DELETE` operation over the DB for the record with the given `id`.
        -   After successful deletion, the app navigates to the "Contact List" screen, which then triggers a new `GetAllContacts` flow to display the updated list.


### Backend API for Frontend

This section provides a high-level overview of the backend API endpoints required for the frontend application to function. The API follows RESTful principles.

#### Base URL
All endpoints are prefixed with `/api`. For example: `https://yourdomain.com/api/contacts`.

#### Data Models
The API uses the same data models described in the "Data flow" section: `ContactFullDetails` and `ContactShortDescription`.

---

#### 1. Get All Contacts

Retrieves a simple list of all contacts, sorted alphabetically.

-   **Endpoint:** `GET /contacts`
-   **Success Response (200 OK):**
    -   **Content:** An array of `ContactShortDescription` objects.
    -   **Example:**
        ```json
        [
          { "id": "1", "name": "Maks Kozlov" },
        ]
        ```

---

#### 2. Get Contact Details

Retrieves the full details for a single, specific contact.

-   **Endpoint:** `GET /contacts/{id}`
-   **URL Parameters:**
    -   `id` (required, String): The unique identifier of the contact.
-   **Success Response (200 OK):**
    -   **Content:** A single `ContactFullDetails` object.
-   **Error Response (404 Not Found):**
    -   Returned if a contact with the specified `id` does not exist.

---

#### 3. Create a New Contact

Adds a new contact to the database.

-   **Endpoint:** `POST /contacts`
-   **Request Body:**
    -   **Content:** A `ContactFullDetails` object without the `id` field.
-   **Success Response (201 Created):**
    -   **Content:** The full `ContactFullDetails` object of the newly created contact, including the server-generated `id`.
-   **Error Response (400 Bad Request):**
    -   Returned if the request body fails validation (e.g., missing a required `name`).

---

#### 4. Update an Existing Contact

Updates all information for a specific contact.

-   **Endpoint:** `PUT /contacts/{id}`
-   **URL Parameters:**
    -   `id` (required, String): The unique identifier of the contact to update.
-   **Request Body:**
    -   **Content:** A `ContactFullDetails` object containing the new data for the contact.
-   **Success Response (200 OK):**
    -   **Content:** The updated `ContactFullDetails` object.
-   **Error Responses:**
    -   `400 Bad Request`: If the request body is invalid.
    -   `404 Not Found`: If a contact with the specified `id` does not exist.

---

#### 5. Delete a Contact

Permanently removes a contact from the database.

-   **Endpoint:** `DELETE /contacts/{id}`
-   **URL Parameters:**
    -   `id` (required, String): The unique identifier of the contact to delete.
-   **Success Response (204 No Content):**
    -   An empty response body indicating successful deletion.
-   **Error Response (404 Not Found):**
    -   Returned if a contact with the specified `id` does not exist.

---

#### 6. Search Contacts (Full-Text Search)

Performs a full-text search across all contacts and returns matching results.

-   **Endpoint:** `GET /contacts/search`
-   **Query Parameters:**
    -   `q` (required, String): The search query. The backend will use its full-text search capabilities to find matches across key fields like `name`, `phone`, `workplace`, `notes`, etc.
-   **Success Response (200 OK):**
    -   **Content:** An array of `ContactShortDescription` objects that match the search query, sorted alphabetically.
    -   **Example Request:** `GET /api/contacts/search?q=корпорация`
    -   **Example Response:**
        ```json
        [
          { "id": "1", "name": "Maks Kozlov" }
        ]
        ```
-   **Error Response (400 Bad Request):**
    -   Returned if the query parameter `q` is missing or empty.