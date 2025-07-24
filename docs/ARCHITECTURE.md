# Project Architecture

The document describes an architecture of the project and high-level details about how the main app works.


## Overview

The app is cut in virtual layers. Each layer has a unique responsibility:
- UI Layer: renders UI elements and handles interaction from a user (touches, clicks, input from a keyboard). Here lies all elements that depends on a UI framework. The UI layer contains `UI triggers` which trigger logic and/or navigation events.
- Controller Layer + Navigation: glues `UI` and `Logic` layers. Here should be performed all calls to the UI and logic. Navigation is responsible for routing between screens when something happens in the app (update in database or user interaction). The layer is optional and depends on implementation.
- Logic Layer: contains business logic and entities. Also communicates with relational DB storage and performs CRUD operations over the storage. The DB is a relational DB with an ability to make a full-text search to meet feature requirements.

## Architecture scheme

See the high-level architecture below (as a diagram):

[img]

The diagram (scheme) shows the data flow (how the data is passed between layers and components) and navigation flow (dependencies between UI views).
The data flow for the specific use case is coloured with its own colour to simplify tracking and improve readability of the scheme.
If you have to edit/update the architecture, use the [`draw.io`](https://draw.io) service and the [raw XML file]().

## Use cases and its flows

The section below contains description and details for the use cases. It accompnanies the scheme and should be used as a helper to the visual diagram above.
Each flow corresponds to the visual path on a scheme with a specific colour (see notes in paranthesis).

### Navigation

The subsection describes the relations between UI views (screens) and their dependencies.
Given the navigation flow you have to understand what screen can open another one.

- Upon opening, the app shows the “Contact List” screen.
- Description of the navigation flow for the use case: a user can open the app and see the list of stored contacts (follow dashed light green arrows on scheme).
    - TODO
- Description of the navigation flow for the use case: a user can close the app
    - TODO
- Description of the navigation flow for the use case: a user can open a screen where they can edit information about a specific contact (follow light purple arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: while looking at contact details, a user can go back to the full list of contacts (follow green arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: a user can open a screen where they can add info about a new contact (follow yellow arrows on scheme)
    - pre-requisites: navigate to “Contact List” screen.
    - action (trigger): press the “Create New Contact” button.
    - result: navigate to the “New Contact” screen and show the screen with empty UI fields.
- Description of the navigation flow for the use case: a user can cancel the process of creating of a new contact (follow purple arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: after the successful creation of a new contact, a user can see the details about the contact (follow orange arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: a user can open a screen to see a details about the specific contact (follow red arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: after the successful removing of existing contact, a user can see the full list of stored contacts \[without the contact that was deleted\] (follow light blue arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: a user can cancel a process of a deletion of the existing contact and open the contact details (follow yellow arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: a user can update an existing contact and open the contact details with the updated info (follow dashed magenta arrows on scheme)
    - TODO
- Description of the navigation flow for the use case: a user can cancel the process of updating of an existing contact (follow dark blue arrows on scheme)
    - TODO
- TODO: Add more if needed

### Data flow

The subsection describes how the data should be passed between layers and components in order to make the app works.
To pass the data within the app, the following models should be used:

```
ContactFullDetails struct:

- id (UUID string or unique integer)
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

- Description of the data flow for the use case: a user can see all stored contacts (follow dashed light green arrows on scheme)
    - pre-requisites: navigate to “Contact List” screen
    - action (trigger): the "Contact List" appears on the screen.
    - result:
        - call `GetAllContacts() -> [ContactShortDescription]` method in the controller layer
            - pass data received from the `GetAllContacts()` method into the “Contact List” screen or display "No contacts" text, if result array is empty
        - the `GetAllContacts` method in the logic layer do the following:
            - perform `SELECT` operation over the DB;
            - extract all rows with the fields: id, name to form `ContactShortDescription` struct later;
            - sort results alphabetically by the `name` field;
- Description of the data flow for the use case: a user can fill the info about a new contact and store it (follow orange arrows on scheme)
    - TODO
- Description of the data flow for the use case: a user can get all  the stored details about a specific contact (follow lime or light green arrows)
    - TODO
- Description of the data flow for the use case: a user can find contacts by their name (follow blue arrows)
    - TODO
- Description of the data flow for the use case: a user can edit/update info about stored contact and save the changes (follow dashed magenta line)
    - TODO
- Description of the data flow for the use case: a user can remove a stored contact ()
    - TODO
- TODO: add more flows if needed
