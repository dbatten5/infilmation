import React from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import { useStateContext } from './state';

const FilmList = () => {
  const { state } = useStateContext();

  return (
    <Box sx={{ width: '100%' }}>
      <Stack spacing={2}>
        {state.filmList.map((film) => (
          <p>{film.title}</p>
        ))}
      </Stack>
    </Box>
  );
};

export default FilmList;
