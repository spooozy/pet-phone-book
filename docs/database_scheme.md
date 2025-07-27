# Database Schema

This document describes the database schema used for storing contacts and their related information.

## Tables Overview

### 1. `phonebook`

The main table for storing basic contact information.

| Field      | Type             | Description                                     |
|---|---|---|
| `id_contact` | `INTEGER NOT NULL` | Primary key, unique identifier for the contact. |
| `name`       | `TEXT NOT NULL`    | The contact's name (required field).            |

### 2. `contact_details`

Stores additional, optional information about contacts. Each record is linked to a contact via `id_contact`.

| Field       | Type             | Description                                                                                 |
|---|---|---|
| `id`          | `INTEGER NOT NULL` | Primary key, unique identifier for the record.                                              |
| `id_contact`  | `INTEGER NOT NULL` | Foreign key referencing `phonebook(id_contact)`.                                            |
| `birthday`    | `TEXT`             | The contact’s birth date. See [Data Formats and Conventions](#data-formats-and-conventions).  |
| `workplace`   | `TEXT`             | Company or job title.                                                                       |
| `address`     | `TEXT`             | Physical address.                                                                           |
| `notes`       | `TEXT`             | Free-text notes about the contact.                                                          |

### 3. `communication_methods`

Stores various communication methods for a contact. A single contact can have multiple communication methods. The schema does not impose a limit on their number; however, an application-level limit of 10 communication methods per contact will be enforced.

| Field      | Type             | Description                                                                                               |
|---|---|---|
| `id`         | `INTEGER NOT NULL` | Primary key, unique identifier for the record.                                                            |
| `id_contact` | `INTEGER NOT NULL` | Foreign key referencing `phonebook(id_contact)`.                                                          |
| `type`       | `TEXT NOT NULL`    | A user-defined label for the communication method. See [Data Formats and Conventions](#data-formats-and-conventions) for details. |
| `value`      | `TEXT NOT NULL`    | The value for the method. See [Data Formats and Conventions](#data-formats-and-conventions) for details.     |

## Data Formats and Conventions

To ensure data consistency and predictable behavior, the application logic must enforce the rules described in the table below. While the database uses flexible data types like `TEXT`, this section serves as the definitive guide for data format requirements.

| Field                             | Format / Convention | Rules & Examples                                                                                                                                                             |
|---|---|---|
| **Primary Keys** (`id`, `id_contact`) | `INTEGER`           | - **Not Nullable**<br>- Auto-incrementing, managed by SQLite.                                                                                                                |
| `phonebook.name`                  | `TEXT`              | - **Not Nullable**<br>- Must be a non-empty string.<br>- Required length: 1-255 characters.                                                                                    |
| `contact_details.birthday`        | `TEXT (YYYY-MM-DD)` | - **Nullable**<br>- Must be a valid date in ISO 8601 format (`DD-MM-YYYY`). This standard format is used for reliable sorting and querying.<br>- **Example:** `1995-08-23`      |
| `communication_methods.type`      | `TEXT`              | - **Not Nullable**<br>- A user-defined label for the communication method.<br>- The application may suggest standard types (e.g., 'Phone', 'Email') but allows users to enter custom ones.<br>- **Examples:** `'Work Phone'`, `'Social Media'`, `'Personal Website'` |
| `communication_methods.value`     | `TEXT`              | - **Not Nullable**<br>- The corresponding value for the `type`.<br>- The format is not validated by the database but must be a non-empty string.<br>- **Examples:** `'+14155552671'`, `'user@example.com'`, `'https://example.com'` |
| `workplace`, `address`, `notes`   | `TEXT`              | - **Nullable**<br>- Free-form text. No strict format is enforced. Can be an empty string.                                                                                       |

## Full-Text Search

To provide fast searching by contact names, a virtual table `phonebook_fts` is used. This table is an extension of SQLite called FTS5, which indexes the `name` column from the `phonebook` table for efficient text-based queries.

Queries against this table should use the `MATCH` operator instead of `LIKE`. For more detailed information, refer to the [official SQLite FTS5 documentation](https://www.sqlite.org/fts5.html).

## Database Setup

This section explains how to create and initialize the database from the [`initialize_db.sql`](../db/initialize_db.sql) script. This is necessary for:

- **Local Development:** Each developer can quickly set up their own instance of the database.
- **Testing:** Automated tests can create a clean database before each run.
- **Initial Deployment:** To set up the database for the first time in a new environment.

### Prerequisites: SQLite3 Installation

SQLite3 must be installed on your system.

- **Debian/Ubuntu:** `sudo apt-get install sqlite3`
- **macOS (with Homebrew):** `brew install sqlite3`
- **Windows:** Download precompiled binaries from the [official SQLite website](https://www.sqlite.org/download.html).

### Execution

To create the database, navigate to the root directory of the project and run the following command in your terminal:

```bash
sqlite3 db/contacts.db < db/initialize_db.sql
```
