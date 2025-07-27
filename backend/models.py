"""
Data models for Pet PhoneBook project.

This module defines Pydantic models that represent:
- Contact entities (both short and full versions)
- Contact methods (phone, email, etc.)
- Additional contact information

All models are validated automatically via Pydantic and support:
- Data serialization/deserialization
- Schema generation for OpenAPI documentation
- Input data validation for API endpoints
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class WayOfContact(BaseModel):
    """
    Contact method representation (communication channel).
    
    Attributes:
        id: Unique method identifier
        contact_id: Reference to parent contact
        way_of_contact: Contact type (e.g., 'phone', 'email', 'telegram')
        way_of_contact_data: Actual contact value
    """
    id: int = Field(..., gt=0)
    contact_id: int = Field(..., gt=0)
    way_of_contact: str = Field()
    way_of_contact_data: str = Field()


class AdditionalInfo(BaseModel):
    """
    Supplementary contact metadata.
    
    Attributes:
        id: Unique record identifier
        contact_id: Reference to parent contact
        birth_date: Date in YYYY-MM-DD format
        address: Physical address
        notes: Free-form notes about contact
    """
    id: int = Field(..., gt=0)
    contact_id: int = Field(..., gt=0)
    birth_date: str = Field(regex=r"^\d{4}-\d{2}-\d{2}$")
    address: str = Field(default="")
    notes: str = Field(default="")


class Contact(BaseModel):
    """
    Complete contact representation with all associated data.
    
    Attributes:
        id: Unique contact identifier
        name: Contact's full name
        ways_of_contact: List of communication methods
        additional_info: Optional extended metadata
    
    Relationships:
        - One-to-many with WayOfContact
        - One-to-one with AdditionalInfo
    """
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=100)
    ways_of_contact: List[WayOfContact]
    additional_info: Optional[AdditionalInfo] = None

class ShortContact(BaseModel):
    """
    Complete contact representation with all associated data.
    
    Attributes:
        id: Unique contact identifier
        name: Contact's full name
        ways_of_contact: List of communication methods
        additional_info: Optional extended metadata
    
    Relationships:
        - One-to-many with WayOfContact
        - One-to-one with AdditionalInfo
    """
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=100)