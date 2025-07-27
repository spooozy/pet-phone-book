"""
test_backend.py

Unit tests for the database and logic layers of the contacts application.
"""
import os
import sqlite3
import pytest
from models import Contact, ShortContact, WayOfContact, AdditionalInfo
from database import ContactRepository
from logic import ContactService

TEST_DB_PATH = "test_contacts.db"

@pytest.fixture(scope="module")
def setup_test_db():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    repo = ContactRepository(db_path=TEST_DB_PATH)
    with sqlite3.connect(TEST_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS ways_of_contact (id INTEGER PRIMARY KEY, contact_id INTEGER, way_of_contact TEXT, way_of_contact_data TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS additional_info (id INTEGER PRIMARY KEY, contact_id INTEGER, birth_date TEXT, address TEXT, notes TEXT)")
        cursor.execute("INSERT INTO contacts (name) VALUES ('Alice')")
        cursor.execute("INSERT INTO contacts (name) VALUES ('Bob')")
        cursor.execute("INSERT INTO ways_of_contact (contact_id, way_of_contact, way_of_contact_data) VALUES (1, 'email', 'alice@example.com')")
        cursor.execute("INSERT INTO ways_of_contact (contact_id, way_of_contact, way_of_contact_data) VALUES (1, 'phone', '+123456789')")
        cursor.execute("INSERT INTO ways_of_contact (contact_id, way_of_contact, way_of_contact_data) VALUES (2, 'phone', '+123456789')")
        cursor.execute("INSERT INTO additional_info (contact_id, birth_date, address, notes) VALUES (1, '1990-01-01', '123 Main St', 'Test note')")
        conn.commit()
    yield repo
    os.remove(TEST_DB_PATH)

def test_get_all_contacts(setup_test_db):
    repo = setup_test_db
    contacts = repo.get_all_contacts()
    assert len(contacts) == 2
    assert contacts[0].name == 'Alice'
    assert contacts[1].name == 'Bob'
    assert contacts[0].id == 1
    assert contacts[1].id == 2

def test_get_contact_by_id_full_data(setup_test_db):
    repo = setup_test_db
    contact = repo.get_contact_by_id(1)
    assert isinstance(contact, Contact)
    assert contact.id == 1
    assert contact.name == 'Alice'
    assert isinstance(contact.ways_of_contact, list)
    assert len(contact.ways_of_contact) == 2
    assert any(w.way_of_contact == 'email' for w in contact.ways_of_contact)
    assert any(w.way_of_contact == 'phone' for w in contact.ways_of_contact)
    assert isinstance(contact.additional_info, AdditionalInfo)
    assert contact.additional_info.birth_date == '1990-01-01'
    assert contact.additional_info.address == '123 Main St'
    assert contact.additional_info.notes == 'Test note'

def test_get_contact_by_id_no_info(setup_test_db):
    repo = setup_test_db
    contact = repo.get_contact_by_id(2)
    assert isinstance(contact, Contact)
    assert contact.id == 2
    assert contact.name == 'Bob'
    assert contact.ways_of_contact != []
    assert contact.additional_info is None

def test_get_contact_by_id_not_found(setup_test_db):
    repo = setup_test_db
    contact = repo.get_contact_by_id(999)
    assert contact is None

def test_contact_service_get_all_contacts(setup_test_db):
    service = ContactService(setup_test_db)
    contacts = service.get_all_contacts()
    assert len(contacts) == 2
    assert contacts[0].name == 'Alice'
    assert contacts[1].name == 'Bob'

def test_contact_service_get_contact_by_id_full_data(setup_test_db):
    service = ContactService(setup_test_db)
    contact = service.get_contact_by_id(1)
    assert isinstance(contact, Contact)
    assert contact.id == 1
    assert contact.name == 'Alice'
    assert len(contact.ways_of_contact) == 2
    assert contact.additional_info is not None

def test_contact_service_get_contact_by_id_no_ways_or_info(setup_test_db):
    service = ContactService(setup_test_db)
    contact = service.get_contact_by_id(2)
    assert isinstance(contact, Contact)
    assert contact.id == 2
    assert contact.ways_of_contact == []
    assert contact.additional_info is None

def test_contact_service_get_contact_by_id_not_found(setup_test_db):
    service = ContactService(setup_test_db)
    contact = service.get_contact_by_id(999)
    assert contact is None

def test_contact_service_get_contact_by_id_invalid(setup_test_db):
    service = ContactService(setup_test_db)
    with pytest.raises(ValueError):
        service.get_contact_by_id(None) 