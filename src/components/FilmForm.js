import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import FilmInput from '../components/FilmInput';
import FilmSubmit from '../components/FilmSubmit';

const useStyles = makeStyles((theme) => ({
  grid: {
    height: '100%',
  },
}));

const FilmForm = () => {
  const classes = useStyles();

  const [films, setFilms] = React.useState('');

  const handleChange = (event) => setFilms(event.target.value);

  return (
    <Grid container spacing={3} direction="row" className={classes.grid}>
      <Grid item xs={12} md={9}>
        <FilmInput films={films} onChange={handleChange} />
      </Grid>
      <Grid item xs={12} md={3}>
        <FilmSubmit films={films} />
      </Grid>
    </Grid>
  );
};

export default FilmForm;
