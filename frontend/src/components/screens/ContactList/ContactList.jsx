import { useState } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  TextField,
  List,
  ListItem,
  ListItemAvatar,
  Avatar,
  ListItemText,
  Fab,
  Box,
  InputAdornment,
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import PersonIcon from '@mui/icons-material/Person';
import SearchIcon from '@mui/icons-material/Search';
import ContactsIcon from '@mui/icons-material/Contacts'; 
import styles from './ContactList.module.scss';

const initialContacts = [
  { id: 1, name: 'Анастасия Вольф' },
  { id: 2, name: 'Максим Козлов' },
  { id: 3, name: 'Евгений Романов' },
  { id: 4, name: 'Дарья Соколова' },
];

const ContactList = () => {
  const [contacts] = useState(initialContacts);
  const [searchTerm, setSearchTerm] = useState('');

  const filteredContacts = contacts
    .filter((contact) =>
      contact.name.toLowerCase().includes(searchTerm.toLowerCase())
    )
    .sort((a, b) => a.name.localeCompare(b.name));

  return (
    <Box className={styles.pageContainer}>
      {/* Классический синий AppBar */}
      <AppBar position="sticky" elevation={2}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Телефонная книга
          </Typography>
        </Toolbar>
      </AppBar>

      <Container maxWidth="md" sx={{ py: 3 }}>
        <TextField
          fullWidth
          placeholder="Поиск по контактам"
          variant="outlined"
          onChange={(e) => setSearchTerm(e.target.value)}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon color="action" />
              </InputAdornment>
            ),
            sx: {
              borderRadius: '16px',
              backgroundColor: 'white',
            },
          }}
        />

        <Box sx={{ mt: 3 }}>
          {filteredContacts.length > 0 ? (
            <List>
              {filteredContacts.map((contact) => (
                <ListItem
                  button
                  key={contact.id}
                  className={styles.listItem}
                  sx={{ p: 2 }}
                >
                  <ListItemAvatar>
                    <Avatar sx={{ bgcolor: 'primary.main' }}>
                      <PersonIcon />
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText
                    primary={contact.name}
                    primaryTypographyProps={{
                      fontWeight: 500,
                      fontSize: '1.1rem',
                    }}
                  />
                </ListItem>
              ))}
            </List>
          ) : (
            <Box
              sx={{
                textAlign: 'center',
                mt: 8,
                color: 'text.secondary',
              }}
            >
              <ContactsIcon sx={{ fontSize: 80, mb: 2, color: '#bdbdbd' }} />
              <Typography variant="h6">Your contact list is empty</Typography>
              <Typography variant="body1">
                Click "+" to add your first contact
              </Typography>
            </Box>
          )}
        </Box>
      </Container>

      <Fab color="primary" aria-label="add" className={styles.fab}>
        <AddIcon />
      </Fab>
    </Box>
  );
};

export default ContactList;