import React from 'react';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Header from '../components/Header';
import Home from './Home';
import Results from './Results';
import { Switch, Route } from 'react-router-dom';

const useStyles = makeStyles({
  root: {
    height: '100vh',
  },
  body: {
    flexGrow: 1,
  },
  container: {
    height: '100%',
  },
});

function App() {
  const classes = useStyles();

  return (
    <>
      <CssBaseline />
      <Grid container direction="column" className={classes.root}>
        <Grid item>
          <Header />
        </Grid>
        <Grid item className={classes.body}>
          <Container maxWidth="lg" className={classes.container}>
            <Switch>
              <Route path="/" component={Home} exact />
              <Route path="/results" component={Results} />
            </Switch>
          </Container>
        </Grid>
      </Grid>
    </>
  );
}

export default App;
