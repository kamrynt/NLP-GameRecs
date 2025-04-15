import React from 'react';
import { Box, Container, Typography } from '@mui/material';
import ChatWindow from './components/ChatWindow';

const App = () => {
  return (
    <Box
      sx={{
        minHeight: '100vh',
        background: 'linear-gradient(to right, #1f1f1f, #2b2b2b)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        p: 2,
      }}
    >
      <Container maxWidth="sm" sx={{ p: 3, borderRadius: 2, bgcolor: '#161616', boxShadow: 8 }}>
        <Typography
          variant="h4"
          align="center"
          gutterBottom
          sx={{
            fontFamily: 'Orbitron',
            color: '#00ffcc',
            textShadow: '0 0 10px #00ffcc',
          }}
        >
          🎮 Game Recommender Bot
        </Typography>
        <ChatWindow />
      </Container>
    </Box>
  );
};

export default App;
