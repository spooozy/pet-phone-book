from models import Contact, ShortContact, WayOfContact
from datetime import datetime
from ContactRepository import ContactRepository
from config import BaseConfig
from typing import List
import sqlite3

class ContactService:
    def __init__(self, config = BaseConfig ()):
        self.repository = ContactRepository(config)
    
    def add_contact(self, contact_data: Contact) -> Contact:
        try: 
            if contact_data.additional_info and contact_data.additional_info.birth_date:
                if not self.is_valid_date(contact_data.additional_info.birth_date):
                    raise Exception("The specified date of birth does not exist")
            self.normalize_contact_methods(contact_data.ways_of_contact)
            return self.repository.add_contact(contact_data)       
        except Exception as e:
            print(f"Error saving contact: {e}")
            raise
        
    def delete_contact(self, contact_id: int) -> bool:
        try:
            if not isinstance(contact_id, int) or contact_id <= 0:
                raise ValueError("Invalid contact ID")
                
            if self.repository.delete_contact(contact_id):
                return (True, contact_id)
            else:
                return (False, "Not Found")
            
        except sqlite3.Error as e:
            return (False, f"Database error: {e}")
        
        except Exception as e:
            return (False, "Server Error")
        
    def find_contact(self, search_query: str) -> List[ShortContact]:
        try: 
            if not search_query.strip():
                return []
            if any(char in search_query for char in [';', '--']):
                raise ValueError("The search query contains invalid characters.")
            normalized_query = search_query.lower().strip()
            return self.repository.find_contact(normalized_query)
        except ValueError as e:
            raise
        except sqlite3.Error as e:
            raise RuntimeError("Error while searching contacts")

    def is_valid_date(self, date_str: str) -> bool:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def normalize_contact_methods(self, contact_methods: List[WayOfContact]):
        for way in contact_methods:
            way.way_of_contact = way.way_of_contact.strip().capitalize()
            way.way_of_contact_data = way.way_of_contact_data.strip()

    def close(self):
        self.repository.close()
            
    def __del__(self):
        self.repository.close()
