from models import Contact
from ContactService import ContactService
from config import TestConfig

def test_add():
    json_data = {
            "name": "Зелебоба младший",
            "ways_of_contact": [
               {
                    "way_of_contact": "email",
                    "way_of_contact_data": "hannibal@fbi-most-wanted.com"
                }
            ],
            "additional_info": {
                "birth_date": "1933-12-01",
                "address": "Там же, где и старший",
                "notes": "Клиент VIP"
            }
        }
    contact_data = Contact(**json_data)
    service = ContactService()
    created_contact = service.add_contact(contact_data)
    print(created_contact)

def test_delete():
    contact_id = 18
    service = ContactService()
    print(service.delete_contact(contact_id))

def test_search():
    search_query = "Зелебоба младший"
    service = ContactService()
    print(service.find_contact(search_query))

if __name__ == "__main__":
    test_add()