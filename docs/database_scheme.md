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
| `birthday` | `TEXT` | The contact’s birth date (e.g., `YYYY-MM-DD`). |
| `workplace` | `TEXT` | Company or job title. |
| `address` | `TEXT` | Physical address. |
| `notes` | `TEXT` | Free-text notes about the contact. |

### 3. `communication_methods`

Stores various communication methods for a contact. A single contact can have multiple communication methods.

| Field | Type | Description |
|---|---|---|
| `id` | `INTEGER NOT NULL` | Primary key, unique identifier for the record. |
| `id_contact` | `INTEGER NOT NULL` | Foreign key referencing `phonebook(id_contact)`. |
| `type` | `TEXT NOT NULL` | The type of communication method (e.g., 'Email', 'Phone', 'Telegram'). |
| `value` | `TEXT NOT NULL` | The value for the method (e.g., 'user@example.com', '+1234567890'). |

## Full-Text Search

To provide fast searching by contact names, a virtual table `phonebook_fts` is used. This table is an extension of SQLite called FTS5, which indexes the `name` column from the `phonebook` table for efficient text-based queries.
Queries against this table should use the `MATCH` operator instead of `LIKE`. For more detailed information, refer to the [official SQLite FTS5 documentation](https://www.sqlite.org/fts5.html).

## Database Setup

This section explains how to create and initialize the database from the `initialize_db.sql` script. This is necessary for:
-   **Local Development:** Each developer can quickly set up their own instance of the database.
-   **Testing:** Automated tests can create a clean database before each run.
-   **Initial Deployment:** To set up the database for the first time in a new environment.

### Prerequisites: SQLite3 Installation

SQLite3 must be installed on your system.

-   **Debian/Ubuntu:** `sudo apt-get install sqlite3`
-   **macOS (with Homebrew):** `brew install sqlite3`
-   **Windows:** Download precompiled binaries from the [official SQLite website](https://www.sqlite.org/download.html).

### Execution

To create the database, navigate to the directory containing `initialize_db.sql` and run the following command in your terminal:

```bash
sqlite3 contacts.db < schema.sql
```
This command will:
- Create a new file named phonebook.db (the database).
- Execute the SQL commands from [../db/initialize_db.sql]`initialize_db.sql` to create the tables, triggers, and indexes inside it.