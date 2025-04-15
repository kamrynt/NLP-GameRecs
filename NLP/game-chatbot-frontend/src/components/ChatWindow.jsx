import GameCard from './GameCard';
import React, { useState } from 'react';
import {
  Paper, TextField, IconButton, List, ListItem, ListItemText, CircularProgress, Box
} from '@mui/material';
import SendIcon from '@mui/icons-material/Send';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
  
    const newMessages = [...messages, { from: 'user', text: input }];
    setMessages(newMessages);
    setInput('');
    setLoading(true);
  
    try {
      const res = await fetch('http://127.0.0.1:5000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
  
      const data = await res.json();
  
      setMessages([...newMessages, { from: 'bot', text: data }]);
    } catch (err) {
      setMessages([...newMessages, { from: 'bot', text: '⚠️ Could not connect to backend.' }]);
    }
  
    setLoading(false);
  };
  

  return (
    <Paper
      elevation={5}
      sx={{
        p: 2,
        height: '400px',
        display: 'flex',
        flexDirection: 'column',
        bgcolor: '#202020',
        borderRadius: 2,
      }}
    >
      <List sx={{ flexGrow: 1, overflowY: 'auto' }}>
        {messages.map((msg, i) => (
          <ListItem
            key={i}
            sx={{
              justifyContent: msg.from === 'user' ? 'flex-end' : 'flex-start',
            }}
          >
            <ListItemText
              primary={
              Array.isArray(msg.text) ? (
             msg.text.map((game, i) => <GameCard key={i} game={game} />)
            ) : (
             msg.text
           )
           }
            />
          </ListItem>
        ))}
        {loading && (
          <ListItem>
            <CircularProgress size={20} sx={{ color: '#00ffcc' }} />
          </ListItem>
        )}
      </List>

      <Box sx={{ mt: 2, display: 'flex', gap: 1 }}>
        <TextField
          fullWidth
          variant="outlined"
          placeholder="Ask for a game recommendation..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' ? sendMessage() : null}
          sx={{
            input: { color: '#00ffcc' },
            fieldset: { borderColor: '#00ffcc' },
          }}
        />
        <IconButton onClick={sendMessage} sx={{ color: '#00ffcc' }}>
          <SendIcon />
        </IconButton>
      </Box>
    </Paper>
  );
};

export default ChatWindow;
