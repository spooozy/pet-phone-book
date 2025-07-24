CREATE TABLE IF NOT EXISTS Contacts (
    id_contact INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Additional_information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_contact INTEGER NOT NULL,
    birthday TEXT,
    workplace TEXT,
    address TEXT,
    notes TEXT,
    FOREIGN KEY (id_contact) REFERENCES Contacts(id_contact) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Communication_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_contact INTEGER NOT NULL,
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
    FOREIGN KEY (id_contact) REFERENCES Contacts(id_contact) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS contacts_fts USING fts5(
    name,
    content='Contacts',
    content_rowid='id_contact'
);

CREATE TRIGGER IF NOT EXISTS contacts_ai AFTER INSERT ON Contacts
BEGIN
    INSERT INTO contacts_fts(rowid, name) VALUES (new.id_contact, new.name);
END;

CREATE TRIGGER IF NOT EXISTS contacts_ad AFTER DELETE ON Contacts
BEGIN
    DELETE FROM contacts_fts WHERE rowid = old.id_contact;
END;

CREATE TRIGGER IF NOT EXISTS contacts_au AFTER UPDATE ON Contacts
BEGIN
    DELETE FROM contacts_fts WHERE rowid = old.id_contact;
    INSERT INTO contacts_fts(rowid, name) VALUES (new.id_contact, new.name);
END;