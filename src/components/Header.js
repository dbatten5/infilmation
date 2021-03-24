import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
    paddingTop: theme.spacing(8),
  },
  title: {
    fontFamily: 'HelveticaNeue-Light',
    color: 'black',
    fontSize: '3.5rem',
    fontWeight: '100',
    fontStyle: 'italic',
    letterSpacing: '0.15rem',
  },
  link: {
    textDecoration: 'none',
  }
}));

const Header = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Container maxWidth="lg">
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
      </Container>
    </div>
  );
};

export default Header;
