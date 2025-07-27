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
        
    def get_contact_by_id(self, contact_id: int) -> Contact:
        """Retrieves a complete contact record by its ID.
        
        Args:
            contact_id (int): The ID of contact to retrieve
            
        Returns:
            Contact: Fully populated Contact object with all related data
            None: If no contact with specified ID exists
            
        Note:
            Performs 3 separate queries to get:
            1. Main contact info
            2. Contact methods
            3. Additional info
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Get main contact info
            cursor.execute("SELECT id, name FROM contacts WHERE id = ?", (contact_id,))
            row = cursor.fetchone()
            if not row:
                return None
            contact_id, name = row
            
            # Get contact methods
            cursor.execute("""
                SELECT id, contact_id, way_of_contact, way_of_contact_data 
                FROM ways_of_contact 
                WHERE contact_id = ?
            """, (contact_id,))
            ways_rows = cursor.fetchall()
            ways_of_contact = [
                WayOfContact(
                    id=w[0], 
                    contact_id=w[1], 
                    way_of_contact=w[2], 
                    way_of_contact_data=w[3]
                ) for w in ways_rows
            ]
            
            # Get additional info
            cursor.execute("""
                SELECT id, contact_id, birth_date, address, notes 
                FROM additional_info 
                WHERE contact_id = ?
            """, (contact_id,))
            add_row = cursor.fetchone()
            additional_info = None
            if add_row:
                additional_info = AdditionalInfo(
                    id=add_row[0],
                    contact_id=add_row[1],
                    birth_date=add_row[2],
                    address=add_row[3],
                    notes=add_row[4]
                )
                
            return Contact(
                id=contact_id,
                name=name,
                ways_of_contact=ways_of_contact,
                additional_info=additional_info
            )