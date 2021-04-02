import React from 'react';
import { Link } from "react-router-dom";
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  title: {
    fontFamily: 'HelveticaNeue-Light,HelveticaNeue,Helvetica,Arial,sans-serif',
    color: 'black',
    fontSize: '4rem',
    fontWeight: '100',
    fontStyle: 'italic',
    letterSpacing: '0.15rem',
    '&:hover': {
      opacity: 0.5,
      transition: '0.3s',
    }
  },
  link: {
    textDecoration: 'none',
  }
}));

const Logo = () => {
  const classes = useStyles();

  return (
    <Link to="/" className={classes.link}>
      <Typography 
        variant="h1" 
        className={classes.title} 
        display="inline" 
        gutterBottom
      >
        Infilmation
      </Typography>
    </Link>
  );
};

export default Logo;
