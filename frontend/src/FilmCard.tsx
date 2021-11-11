import React from 'react';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

type Props = {
  title: string;
  year?: number;
};

const FilmCard = ({ title, year }: Props) => (
  <Paper elevation={3} sx={{ width: '100%', p: '1rem' }}>
    <Typography variant="h6" component="div">
      {title}
    </Typography>
    <Typography variant="subtitle2" gutterBottom component="div">
      {year}
    </Typography>
  </Paper>
);

FilmCard.defaultProps = {
  year: null,
};

export default FilmCard;
