import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import FilmForm from '../components/FilmForm';

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100%',
  },
}));

const Home = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <FilmForm />
    </div>
  );
};

export default Home;
