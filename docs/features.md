# Features Overview

### 1. Contact list displaying:
- After entering the application, a whole list of contacts is displaying  
- List shows in alphabetical order  
- If there are no contacts, message about this must be shown  

### 2. Add contact ability:
- After pressing “add contact” button are displaying:  
  - required field for the name of the contact  
  - required field for specifying the way of communication(telephone number field is shown, other fields available with pressing “Alternative ways of communication” button)  
  - Optional fields are below  
- When you click the save button, fields validate and data saves in db  
- Before contact is saved, user sees mistaken field and message specifying the mistake  
- After contact is saved, user sees the message about successful saving and is taken to the list of contacts  
- Clicking the cancel button will reset the form and return an user to the contact list  

### 3. Edit contact ability:
- When you click the edit button, all contact fields are displayed (with the information inside the filled fields)  
- If a field is filled in incorrectly, it is highlighted and a message is displayed specifying the error  
- When you click the save button, the fields are validated and the data is saved to the database. The user is then shown a message about the successful saving of the contact  
- After saving the contact, the user sees a message about the successful saving of the contact  
- When clicking cancel save, the user is shown a message that all changes will be lost. The user must agree or decline this  
  - After agreeing to the loss of data, the form is reset and you return to the contact list  
  - After refusing to lose data, a form is displayed taking into account the entered changes, editing of the contact continues  

### 4. Delete contact ability:
- When the delete button is pressed, the user is notified that the contact information will be lost  
  - If you agree to delete, the contact data is deleted from the database, a message about successful deletion is displayed, and then you are taken to the contact list  
  - If rejected, the contact list is returned  

### 5. View contact ability:
- When viewing additional information about a contact, all filled fields of the contact are displayed  

### 6. Contact search:
- The search is a window for entering some information about a contact  
- The search is carried out by the name of the contact  
- If the contact you are looking for is missing, you will see a message that nothing was found for the request/no contacts  

### Features that are out of scope:
1. Filtering by multiple parameters  
2. Adding specific contacts to favorites  
3. Adding an avatar field for a contact  
4. Grouping contacts by tags  