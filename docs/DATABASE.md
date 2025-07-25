# Contacts Database

This document describes the database schema used for storing contacts and their related information.

## Tables Overview

### 1. `contacts`

The main table for storing basic contact information.

| Field | Type | Description |
|------------|---------------|------------------------------------------------|
| `id_contact` | `INTEGER` | Primary key, unique identifier for the contact. |
| `name` | `TEXT NOT NULL` | The contact's name (required field). |

### 2. `additional_information`

Stores additional, optional information about contacts. Each record is linked to a contact via `id_contact`.

| Field | Type | Description |
|-------------|---------------|----------------------------------------------------------|
| `id_info` | `INTEGER` | Primary key, unique identifier for the record. |
| `id_contact` | `INTEGER` | Foreign key referencing `contacts(id_contact)`. |
| `birthday` | `TEXT` | The contact’s birth date (e.g., `YYYY-MM-DD`). |
| `workplace` | `TEXT` | Company or job title. |
| `address` | `TEXT` | Physical address. |
| `notes` | `TEXT` | Free-text notes about the contact. |

### 3. `communication_methods`

Stores various communication methods for a contact. A single contact can have an unlimited number of communication methods.

| Field | Type | Description |
|-------------|---------------|----------------------------------------------------------------------|
| `id_method` | `INTEGER` | Primary key, unique identifier for the record. |
| `id_contact` | `INTEGER` | Foreign key referencing `contacts(id_contact)`. |
| `type` | `TEXT NOT NULL` | The type of communication method (e.g., 'Email', 'Phone', 'Telegram'). |
| `value` | `TEXT NOT NULL` | The value for the method (e.g., 'user@example.com', '+1234567890'). |

## Full-Text Search

To provide fast searching by contact names, the `contacts_fts` virtual table is used.

Triggers (`contacts_ai`, `contacts_ad`, `contacts_au`) automatically synchronize data between the `contacts` table and the `contacts_fts` search index when records are inserted, deleted, or updated.