# Database Schema

This document describes the database schema used for storing contacts and their related information.

## Tables Overview

### 1. `phonebook`

The main table for storing basic contact information.

| Field | Type | Description |
|---|---|---|
| `id_contact` | `INTEGER NOT NULL` | Primary key, unique identifier for the contact. |
| `name` | `TEXT NOT NULL` | The contact's name (required field). |

### 2. `contact_details`

Stores additional, optional information about contacts. Each record is linked to a contact via `id_contact`.

| Field | Type | Description |
|---|---|---|
| `id` | `INTEGER NOT NULL` | Primary key, unique identifier for the record. |
| `id_contact` | `INTEGER NOT NULL` | Foreign key referencing `phonebook(id_contact)`. |
| `birthday` | `TEXT` | The contact’s birth date. See Data Formats and Conventions. |
| `workplace` | `TEXT` | Company or job title. |
| `address` | `TEXT` | Physical address. |
| `notes` | `TEXT` | Free-text notes about the contact. |

### 3. `communication_methods`

Stores various communication methods for a contact. A single contact can have multiple communication methods.

| Field | Type | Description |
|---|---|---|
| `id` | `INTEGER NOT NULL` | Primary key, unique identifier for the record. |
| `id_contact` | `INTEGER NOT NULL` | Foreign key referencing `phonebook(id_contact)`. |
| `type` | `TEXT NOT NULL` | The type of communication method. See Data Formats and Conventions. |
| `value` | `TEXT NOT NULL` | The value for the method. See Data Formats and Conventions. |

## Data Formats and Conventions

This section is the single source of truth for data format requirements. While the database uses flexible types like `TEXT`, the application logic must enforce these rules to ensure data consistency and predictable behavior.

| Field | Format / Convention | Rules & Examples |
|---|---|---|
| **Primary Keys** (`id`, `id_contact`) | `INTEGER` | - **Not Nullable**<br>- Auto-incrementing, managed by SQLite. |
| `phonebook.name` | `TEXT` | - **Not Nullable**<br>- Must be a non-empty string.<br>- Recommended length: 1-255 characters. |
| `contact_details.birthday` | `TEXT (YYYY-MM-DD)` | - **Nullable**<br>- Must be a valid date in ISO 8601 format.<br>- **Example:** `1995-08-23` |
| `communication_methods.type` | `TEXT (Enum)` | - **Not Nullable**<br>- Must be one of the predefined values recognized by the application.<br>- **Allowed values:** `'Phone'`, `'Mobile'`, `'Email'`, `'Telegram'`, `'Website'`, `'Work'` |
| `communication_methods.value` | `TEXT (Conditional)` | - **Not Nullable**<br>- The format strictly depends on the corresponding `type` value:<ul><li>**If type is `Phone`, `Mobile`, or `Work`:** Must be a phone number, recommended in E.164 format (e.g., `+14155552671`).</li><li>**If type is `Email`:** Must be a valid email address (e.g., `user@example.com`).</li><li>**If type is `Telegram`:** Must be a username starting with `@` (e.g., `@username`).</li><li>**If type is `Website`:** Must be a full, valid URL (e.g., `https://example.com`).</li></ul> |
| `workplace`, `address`, `notes` | `TEXT` | - **Nullable**<br>- Free-form text. No strict format is enforced. Can be an empty string. |

## Full-Text Search

To provide fast searching by contact names, a virtual table `phonebook_fts` is used. This table is an extension of SQLite called FTS5, which indexes the `name` column from the `phonebook` table for efficient text-based queries.

Queries against this table should use the `MATCH` operator instead of `LIKE`. For more detailed information, refer to the [official SQLite FTS5 documentation](https://www.sqlite.org/fts5.html).

## Database Setup

This section explains how to create and initialize the database from the [initialize_db.sql](../db/initialize_db.sql) script. This is necessary for:
-   **Local Development:** Each developer can quickly set up their own instance of the database.
-   **Testing:** Automated tests can create a clean database before each run.
-   **Initial Deployment:** To set up the database for the first time in a new environment.

### Prerequisites: SQLite3 Installation

SQLite3 must be installed on your system.

-   **Debian/Ubuntu:** `sudo apt-get install sqlite3`
-   **macOS (with Homebrew):** `brew install sqlite3`
-   **Windows:** Download precompiled binaries from the [official SQLite website](https://www.sqlite.org/download.html).

### Execution

To create the database, navigate to the root directory of the project and run the following command in your terminal:

```bash
sqlite3 db/contacts.db < db/initialize_db.sql
```