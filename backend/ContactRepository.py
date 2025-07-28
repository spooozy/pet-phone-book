import sqlite3
import os
from models import Contact, ShortContact, WayOfContact, AdditionalInfo
from typing import List
from config import BaseConfig, TestConfig
from pathlib import Path

class ContactRepository:
    def __init__(self, config = BaseConfig ()):
        self.config = config
        self._ensure_db_ready()
        self.connection = sqlite3.connect(self.config.db_path)
        self.cursor = self.connection.cursor()
    
    def add_contact(self, contact: Contact) -> Contact:
        try:

            self.connection.execute("BEGIN TRANSACTION")

            self.cursor.execute(
                "INSERT INTO phonebook (name) VALUES (?)",
                (contact.name, )
            )
            contact_id = self.cursor.lastrowid
            contact.id = contact_id

            additional_info = contact.additional_info
            if additional_info is not None:
                self.cursor.execute(
                    """INSERT INTO contact_details 
                    (id_contact, birthday, workplace, address, notes) 
                    VALUES (?, ?, ?, ?, ?)""",
                    (
                        contact_id,
                        additional_info.birth_date,
                        additional_info.workplace, 
                        additional_info.address,
                        additional_info.notes,
                    )
                )
                contact.additional_info.contact_id = contact_id
                contact.additional_info.id = self.cursor.lastrowid

            ways_of_contact = contact.ways_of_contact
            for way in ways_of_contact:
                self.cursor.execute(
                    """INSERT INTO communication_methods 
                    (id_contact, type, value) 
                    VALUES (?, ?, ?)""",
                    (contact_id, way.way_of_contact, way.way_of_contact_data)
                )
                way.id = self.cursor.lastrowid
                way.contact_id = contact_id

            self.connection.commit()
            return contact
        
        except Exception as e:
                self.connection.rollback()
                raise e

    def delete_contact(self, contact_id: int) -> bool:
        try:
            self.connection.execute("BEGIN TRANSACTION")
            self.cursor.execute("PRAGMA foreign_keys = ON")
            self.cursor.execute("SELECT 1 FROM phonebook WHERE id_contact = ?", (contact_id,))
            
            if not self.cursor.fetchone():
                return False
            
            self.cursor.execute("DELETE FROM communication_methods WHERE id_contact = ?", (contact_id,))
            self.cursor.execute("DELETE FROM contact_details WHERE id_contact = ?", (contact_id,))
            self.cursor.execute("DELETE FROM phonebook WHERE id_contact = ?", (contact_id,))
            
            self.connection.commit()
            return True

        except sqlite3.Error as e:
            self.connection.rollback()
            raise e
    
    def find_contact(self, normalized_query: str) -> List[ShortContact]:
        try:

            if not normalized_query:
                return []    

            terms = [f'{term.strip()}*' for term in normalized_query.split() if term.strip()]
            if not terms:
                return []
            print(f"Terms: {terms}")
            fts_query = " OR ".join(terms)

            self.cursor.execute(
                """SELECT p.id_contact, p.name 
                FROM phonebook p
                JOIN phonebook_fts fts ON p.id_contact = fts.rowid
                WHERE fts.name MATCH ? COLLATE NOCASE
                ORDER BY p.name ASC """,
                (fts_query,)
            )
            return [ShortContact(id=row[0], name=row[1]) for row in self.cursor.fetchall()]
        
        except sqlite3.Error as e:
            print(f"Search error: {e}")
            raise

    def _ensure_db_ready(self):
        self.config.ensure_db_dir_exists()
        if not Path(self.config.db_path).exists() or os.path.getsize(self.config.db_path) == 0:
            self._init_db_schema()
    
    def _init_db_schema(self):
        with sqlite3.connect(self.config.db_path) as conn:
            sql_file = Path(__file__).parent / "initialize_bd.sql"
            with open(sql_file, "r") as f:
                conn.executescript(f.read())
    
    def close(self):
        self.connection.close()
        if isinstance(self.config, TestConfig):
            try:
                db_file = Path(self.config.db_path)
                if db_file.exists():
                    os.unlink(db_file)
            except Exception as e:
                print(f"Error cleaning up test database: {e}")
        
            
    def __del__(self):
        self.connection.close()
