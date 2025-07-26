"""
database.py

This module provides a repository class for accessing and manipulating contact data 
in a SQLite database. It handles the conversion between database records and Pydantic models.
"""

import sqlite3
import os
from typing import List
from models import Contact, ShortContact, WayOfContact, AdditionalInfo

class ContactRepository:
    """Repository class for performing CRUD operations on contacts in SQLite database.
    
    Responsibilities:
    - Managing database connections
    - Creating required tables on initialization
    - Converting database records to Pydantic models
    - Handling all SQL operations
    """

    def __init__(self, db_path: str = os.path.curdir + "../db/contacts.db"):
        """Initializes the repository and creates required tables if they don't exist.

        Args:
            db_path (str): Path to SQLite database file. 
                          Defaults to '../db/contacts.db' relative to current directory.
        """
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Creates the 'contacts' table if it doesn't exist.
        
        Table schema:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - name: TEXT
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )
            """)
            conn.commit()

    def get_all_contacts(self) -> List[ShortContact]:
        """Retrieves all contacts from database as ShortContact objects.
        
        Returns:
            List[ShortContact]: List of contacts containing only id and name fields
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts")
            rows = cursor.fetchall()
            return [ShortContact(id=row[0], name=row[1]) for row in rows]
