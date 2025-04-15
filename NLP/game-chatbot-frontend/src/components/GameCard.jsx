import React from 'react';
import {
  Card, CardContent, Typography, CardActions, Button, Chip, Stack
} from '@mui/material';

const GameCard = ({ game }) => {
  return (
    <Card sx={{ bgcolor: '#1e1e1e', color: '#00ffcc', mb: 2, width: '100%' }}>
      <CardContent>
        <Typography variant="h6" sx={{ color: '#00ffff' }}>{game.title}</Typography>
        <Typography variant="body2" sx={{ mb: 1 }}>{game.summary}</Typography>
        <Stack direction="row" spacing={1} sx={{ flexWrap: 'wrap', mb: 1 }}>
          {Array.isArray(game.genre) && game.genre.map((tag, i) => (
            <Chip key={i} label={tag} size="small" sx={{ bgcolor: '#00ffcc', color: '#000' }} />
          ))}
        </Stack>
        <Typography variant="body2">
          <strong>Price:</strong> {game.price || 'N/A'} <br />
          <strong>Metacritic:</strong> {game.metacritic} <br />
          <strong>Reviews:</strong> {game.review}
        </Typography>
      </CardContent>
      <CardActions>
      {game.store_url ? (
  <Button
    size="small"
    href={game.store_url}
    target="_blank"
    rel="noopener noreferrer"
    sx={{ color: '#00ffcc' }}
  >
    View Game
  </Button>
) : (
  <Typography variant="body2" sx={{ color: '#888', fontStyle: 'italic' }}>
    No store link available
  </Typography>
)}
      </CardActions>
    </Card>
  );
};

export default GameCard;
