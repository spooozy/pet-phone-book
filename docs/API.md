# API Documentation

## Why This Document Exists

To connect the user interface (UI) with the backend logic, a clear and consistent contract is necessary. This document serves as that contract, describing the API (Application Programming Interface) that the backend provides. It details every available endpoint, its purpose, the data it requires, and the responses it returns.

## Protocol and Versioning

The API is a RESTful service operating over HTTP/S. All requests and responses use the JSON data format.

API versioning is handled through the URL path. The current version is **v1**.

## Base Path

All endpoint paths described in this document are relative to the following base path:

`/api/v1`

## Data Models

### CommunicationMethod
Represents a single communication method. Corresponds to a row in the `communication_methods` table.
```json
{
  "type": "Phone",
  "value": "+1234567890"
}
```

### ContactShortDetails
A simplified model used for contact lists. Corresponds to the `phonebook` table.
```json
{
  "id_contact": 1,
  "name": "Alex Smith"
}
```


### ContactFullDetails
A complete model representing a contact with all associated data.
```json
{
  "id_contact": 1,
  "name": "Alex Smith",
  "birthday": "1990-05-15",
  "workplace": "Tech Solutions Inc.",
  "address": "123 Innovation Drive",
  "notes": "Key contact for the project.",
  "communication_methods": [
    {
      "type": "Email",
      "value": "alex.smith@example.com"
    },
    {
      "type": "Phone",
      "value": "+14155552671"
    }
  ]
}
```

---

## API Endpoints

### 1. Get All Contacts / Search Contacts

Retrieves a list of all contacts, optionally filtered by a search query.

-   **Endpoint Path:** `/contacts`
-   **Request Method:** `GET`
-   **Query Parameters:**
    -   `q` (optional, string): A search term to filter contacts by name. The search is performed using full-text search capabilities.
-   **Possible API Responses:**
    -   **`200 OK` (Success)**: Returns a JSON array of `ContactShortDetails` objects. If no contacts match the query or if the database is empty, an empty array `[]` is returned.
```json
[
  {
    "id_contact": 1,
    "name": "Alex Smith"
  },
  {
    "id_contact": 2,
    "name": "Maria Garcia"
  }
] 
```
-   **`500 Internal Server Error`**: Indicates a server-side problem.

### 2. Get a Specific Contact's Details

Retrieves the full details for a single contact by their ID.

-   **Endpoint Path:** `/contacts/{id_contact}`
-   **Request Method:** `GET`
-   **Path Parameters:**
    -   `id_contact` (integer): The unique identifier of the contact.
-   **Possible API Responses:**
    -   **`200 OK` (Success)**: Returns a single `ContactFullDetails` object.
    -   **`404 Not Found`**: Returned if a contact with the specified `id_contact` does not exist.

### 3. Create a New Contact

Creates a new contact with associated details.

-   **Endpoint Path:** `/contacts`
-   **Request Method:** `POST`
-   **Request Body:** A JSON object matching the `ContactFullDetails` structure. The `id_contact` field should be omitted. The `name` field is required.
-   **Possible API Responses:**
    -   **`201 Created` (Success)**: Returns the full `ContactFullDetails` object of the newly created contact, including the server-generated `id_contact`.
    -   **`400 Bad Request`**: Returned if the request body is malformed or if required fields (like `name`) are missing.

### 4. Update an Existing Contact

Updates all information for a specific contact. This is a full replacement (PUT).

-   **Endpoint Path:** `/contacts/{id_contact}`
-   **Request Method:** `PUT`
-   **Request Body:** A full `ContactFullDetails` JSON object. The `id_contact` in the body must match the `id_contact` in the path.
-   **Possible API Responses:**
    -   **`200 OK` (Success)**: Returns the updated `ContactFullDetails` object.
    -   **`400 Bad Request`**: For invalid or malformed data in the request body.
    -   **`404 Not Found`**: If the `id_contact` does not exist.

### 5. Delete a Contact

Removes a contact and all their associated information from the database.

-   **Endpoint Path:** `/contacts/{id_contact}`
-   **Request Method:** `DELETE`
-   **Possible API Responses:**
    -   **`204 No Content` (Success)**: Indicates successful deletion. The response will have no body.
    -   **`404 Not Found`**: If the `id_contact` does not exist.