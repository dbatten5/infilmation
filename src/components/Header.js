import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

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
}));

const Header = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Container maxWidth="lg">
        <Typography variant="h1" className={classes.title} gutterBottom>
          Infilmation
        </Typography>
      </Container>
    </div>
  );
};

export default Header;
