import pytest
from models import Contact, WayOfContact, AdditionalInfo
from ContactService import ContactService
from config import TestConfig
from typing import List

# Fixture to create ContactService instance before each test
@pytest.fixture
def service():
    service = ContactService(TestConfig())
    yield service
    service.repository.close()

# Fixture providing a sample contact for various tests
@pytest.fixture
def sample_contact():
    return Contact(
        name=" Zeleboba jr.",
        ways_of_contact=[
            WayOfContact(
                way_of_contact="email",
                way_of_contact_data="hannibal@fbi-most-wanted.com"
            )
        ],
        additional_info=AdditionalInfo(
            birth_date="1933-01-01",
            address="In the same place as the elder one",
            notes="VIP-client"
        )
    )

class TestContactService:
     # Test successful contact creation - should return ID and saved contact info
    def test_add_contact_success(self, service, sample_contact):
        added_contact = service.add_contact(sample_contact)
        assert added_contact.id is not None
        assert added_contact.name == sample_contact.name
        assert len(added_contact.ways_of_contact) == 1
        assert added_contact.ways_of_contact[0].way_of_contact == "Email"
        assert added_contact.additional_info.birth_date == "1933-01-01"

    # Test that invalid dates (Feb 30th) raise Exception
    def test_add_contact_invalid_date(self, service, sample_contact):
        sample_contact.additional_info.birth_date = "2023-02-30"
        with pytest.raises(Exception, match="does not exist"):
            service.add_contact(sample_contact)

    # Test successful deletion - should return (True, deleted_id)
    def test_delete_contact_success(self, service, sample_contact):
        added_contact = service.add_contact(sample_contact)
        result = service.delete_contact(added_contact.id)
        assert result == (True, added_contact.id)

    # Test deleting non-existent contact - should return (False, "Not Found")
    def test_delete_nonexistent_contact(self, service):
        result = service.delete_contact(999)
        assert result == (False, "Not Found")

    # Test invalid ID handling - negative IDs return (False, "Server Error")
    def test_delete_contact_invalid_id(self, service):
        result = service.delete_contact(-1)
        assert result == (False, "Server Error")

    # Test contact method normalization - should trim spaces and capitalize
    def test_normalize_contact_methods(self, service, sample_contact):
        sample_contact.ways_of_contact.append(
            WayOfContact(
                way_of_contact="  phone  ",
                way_of_contact_data="  +123456789  "
            )
        )
        service.add_contact(sample_contact)
        assert sample_contact.ways_of_contact[1].way_of_contact == "Phone"
        assert sample_contact.ways_of_contact[1].way_of_contact_data == "+123456789"

    # Test exact name search - should find exactly one matching contact
    def test_find_contact_by_name(self, service, sample_contact):
        results = service.find_contact(" Zeleboba jr.")
        assert len(results) == 1

    # Test partial matching - should work with name parts (case insensitive)
    def test_find_contact_partial_match(self, service, sample_contact):
        results = service.find_contact(" zeleboba")
        assert len(results) == 1
        results = service.find_contact("jr.")
        assert len(results) == 1

    # Test multi-term search - should find all contacts matching any term
    def test_find_contact_multiple_terms(self, service):
        contacts = [
            Contact(name="Иван Иванов", ways_of_contact=[WayOfContact(way_of_contact="phone", way_of_contact_data="123")]),
            Contact(name="Петр Петров", ways_of_contact=[WayOfContact(way_of_contact="phone", way_of_contact_data="456")])
        ]
        
        for contact in contacts:
            service.add_contact(contact)
        
        results = service.find_contact("Иван Петр")
        assert len(results) == 2

    # Test empty query - should return empty list (not all contacts)
    def test_find_contact_empty_query(self, service, sample_contact):
        service.add_contact(sample_contact)
        results = service.find_contact("   ")
        assert results == []

    # Test SQL injection protection - should reject suspicious characters
    def test_find_contact_special_chars(self, service):
        with pytest.raises(ValueError, match="invalid characters"):
            service.find_contact("'; DROP TABLE phonebook;--")

    # Test no-results case - should return empty list for non-matching queries
    def test_find_contact_no_results(self, service):
        results = service.find_contact("NoName")
        assert results == []
