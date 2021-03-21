import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import FilmInput from '../components/FilmInput';
import FilmSubmit from '../components/FilmSubmit';

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100%',
  },
  grid: {
    height: '100%',
  },
}));

const Home = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3} direction="row" className={classes.grid}>
        <Grid item xs={12} md={9}>
          <FilmInput />
        </Grid>
        <Grid item xs={12} md={3}>
          <FilmSubmit />
        </Grid>
      </Grid>
    </div>
  );
};

export default Home;
