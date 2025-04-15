import React from 'react';
import {
  Card, CardContent, Typography, CardActions, Button, Chip, Stack
} from '@mui/material';

const GameCard = ({ game }) => {
  return (
    <Card sx={{ bgcolor: '#1e1e1e', color: '#00ffcc', mb: 2 }}>
      <CardContent>
        <Typography variant="h6" component="div" sx={{ color: '#00ffff' }}>
          {game.title}
        </Typography>
        <Typography variant="body2" sx={{ mb: 1 }}>
          {game.summary}
        </Typography>
        <Stack direction="row" spacing={1} sx={{ flexWrap: 'wrap' }}>
          {Array.isArray(game.genre) && game.genre.map((tag, i) => (
            <Chip key={i} label={tag} size="small" sx={{ bgcolor: '#00ffcc', color: '#000' }} />
          ))}
        </Stack>
        <Typography variant="body2" sx={{ mt: 1 }}>
          <strong>Price:</strong> {game.price} <br />
          <strong>Reviews:</strong> {game.review}
        </Typography>
      </CardContent>
      <CardActions>
        {game.store_url && (
          <Button
            size="small"
            href={game.store_url}
            target="_blank"
            rel="noopener noreferrer"
            sx={{ color: '#00ffcc' }}
          >
            View Game
          </Button>
        )}
      </CardActions>
    </Card>
  );
};

export default GameCard;
