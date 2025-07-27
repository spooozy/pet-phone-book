"""
logic.py

This module implements the business logic layer for contact operations.
It acts as an intermediary between the API layer and data repository,
enforcing business rules while delegating data access to the repository.
"""

from typing import List
from models import Contact, ShortContact
from database import ContactRepository

class ContactService:
    """Service layer encapsulating all business logic for contact operations.
    
    Responsibilities:
    - Enforcing business rules and validations
    - Orchestrating data operations through the repository
    - Abstracting repository implementation from API consumers
    """

    def __init__(self, repository: ContactRepository):
        """Initializes the service with a data repository dependency.
        
        Args:
            repository (ContactRepository): The data access repository instance
                                          that will handle all database operations.
        """
        self.repository = repository

    def get_all_contacts(self) -> List[ShortContact]:
        """Retrieves all contacts in abbreviated form.
        
        Returns:
            List[ShortContact]: A list of contact objects containing only
                              basic information (id and name).
        """
        return self.repository.get_all_contacts()
