import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import FilmForm from '../components/FilmForm';
import InfoBar from '../components/InfoBar';
import Grid from '@material-ui/core/Grid';
import Header from '../components/Header';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100vh',
  },
  body: {
    flexGrow: 1,
  },
  container: {
    height: '100%',
  },
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
    <Grid container direction="column" className={classes.root}>
      <Grid item>
        <Header />
      </Grid>
      <Grid item className={classes.body}>
        <Container maxWidth="lg" className={classes.container}>
          <Grid container direction="column" className={classes.grid}>
            <Grid item>
              <InfoBar />
            </Grid>
            <Grid item className={classes.form}>
              <FilmForm />
            </Grid>
          </Grid>
        </Container>
      </Grid>
    </Grid>
  );
};

export default Home;
