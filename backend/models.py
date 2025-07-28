from pydantic import BaseModel, Field
from typing import Optional, List


class WayOfContact(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    contact_id: Optional[int] = Field(None, gt=0)
    way_of_contact: str = Field()
    way_of_contact_data: str = Field()


class AdditionalInfo(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    contact_id: Optional[int] = Field(None, gt=0)
    birth_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    address: str = Field(default="")
    workplace: str = Field(default="")
    notes: str = Field(default="")


class Contact(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    name: str = Field(..., min_length=1, max_length=256)
    ways_of_contact: List[WayOfContact]
    additional_info: Optional[AdditionalInfo] = None

class ShortContact(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    name: str = Field(..., min_length=1, max_length=256)