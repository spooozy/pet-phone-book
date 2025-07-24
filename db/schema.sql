CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS additional_information (
    id_contact INTEGER PRIMARY KEY,
    birthday TEXT,
    workplace TEXT,
    address TEXT,
    notes TEXT,
    FOREIGN KEY (id_contact) REFERENCES contacts(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS communication_methods (
    id_contact INTEGER PRIMARY KEY,
    way_1 TEXT,
    way_2 TEXT,
    way_3 TEXT,
    way_4 TEXT,
    way_5 TEXT,
    way_6 TEXT,
    way_7 TEXT,
    way_8 TEXT,
    way_9 TEXT,
    way_10 TEXT,
    FOREIGN KEY (id_contact) REFERENCES contacts(id) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS contacts_fts USING fts5(
    name UNINDEXED, 
    content='contacts',
    content_rowid='id'
);

CREATE TRIGGER IF NOT EXISTS contacts_ai AFTER INSERT ON contacts
BEGIN
    INSERT INTO contacts_fts(rowid, name) VALUES (new.id, new.name);
END;

CREATE TRIGGER IF NOT EXISTS contacts_ad AFTER DELETE ON contacts
BEGIN
    DELETE FROM contacts_fts WHERE rowid = old.id;
END;

CREATE TRIGGER IF NOT EXISTS contacts_au AFTER UPDATE ON Contacts
BEGIN
    DELETE FROM contacts_fts WHERE rowid = old.id;
    INSERT INTO ontacts_fts(rowid, name) VALUES (new.id, new.name);
END;