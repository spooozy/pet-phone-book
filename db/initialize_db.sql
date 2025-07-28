CREATE TABLE IF NOT EXISTS phonebook (
    id_contact INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS contact_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_contact INTEGER NOT NULL,
    birthday TEXT,
    workplace TEXT,
    address TEXT,
    notes TEXT,
    FOREIGN KEY (id_contact) REFERENCES phonebook(id_contact) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS communication_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_contact INTEGER NOT NULL,
    type TEXT NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (id_contact) REFERENCES phonebook(id_contact) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS phonebook_fts USING fts5(
    name,
    content='phonebook',
    content_rowid='id_contact'
);

CREATE TRIGGER IF NOT EXISTS phonebook_ai AFTER INSERT ON phonebook
BEGIN
    INSERT INTO phonebook_fts(rowid, name) VALUES (new.id_contact, new.name);
END;

CREATE TRIGGER IF NOT EXISTS phonebook_ad AFTER DELETE ON phonebook
BEGIN
    DELETE FROM phonebook_fts WHERE rowid = old.id_contact;
END;

CREATE TRIGGER IF NOT EXISTS phonebook_au AFTER UPDATE ON phonebook
BEGIN
    DELETE FROM phonebook_fts WHERE rowid = old.id_contact;
    INSERT INTO phonebook_fts(rowid, name) VALUES (new.id_contact, new.name);
END;
