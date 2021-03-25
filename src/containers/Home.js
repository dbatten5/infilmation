import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import FilmForm from '../components/FilmForm';
import InfoBar from '../components/InfoBar';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles((theme) => ({
  grid: {
    height: '100%',
    [theme.breakpoints.up(400)]: {
      paddingBottom: '3rem', 
    }
  },
  form: {
    flex: 1,
  }
}));

const Home = () => {
  const classes = useStyles();

  return (
    <Grid container direction="column" className={classes.grid}>
      <Grid item>
        <InfoBar />
      </Grid>
      <Grid item className={classes.form}>
        <FilmForm />
      </Grid>
    </Grid>
  );
};

export default Home;
