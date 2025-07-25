# Database Schema

This document describes the database schema used for storing contacts and their related information.

## Tables Overview

### 1. `contacts`

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
| `id_contact` | `INTEGER NOT NULL` | Foreign key referencing `contacts(id_contact)`. |
| `birthday` | `TEXT` | The contact’s birth date (e.g., `YYYY-MM-DD`). |
| `workplace` | `TEXT` | Company or job title. |
| `address` | `TEXT` | Physical address. |
| `notes` | `TEXT` | Free-text notes about the contact. |

### 3. `communication_methods`

Stores various communication methods for a contact. A single contact can have multiple communication methods.

| Field | Type | Description |
|---|---|---|
| `id` | `INTEGER NOT NULL` | Primary key, unique identifier for the record. |
| `id_contact` | `INTEGER NOT NULL` | Foreign key referencing `contacts(id_contact)`. |
| `type` | `TEXT NOT NULL` | The type of communication method (e.g., 'Email', 'Phone', 'Telegram'). |
| `value` | `TEXT NOT NULL` | The value for the method (e.g., 'user@example.com', '+1234567890'). |

## Full-Text Search

To provide fast searching by contact names, a virtual table `contacts_fts` is used. This table is an extension of SQLite called FTS5, which indexes the `name` column from the `contacts` table for efficient text-based queries.

Queries against this table should use the `MATCH` operator instead of `LIKE`. For more detailed information, refer to the [official SQLite FTS5 documentation](https://www.sqlite.org/fts5.html).

