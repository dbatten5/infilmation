import React from 'react';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  title: {
    color: 'black',
    fontSize: '1.1rem',
    fontWeight: '200',
  },
}));

const InfoBar = () => {
  const classes = useStyles();

  return (
    <Typography 
      variant="h6"
      display="inline" 
      className={classes.title} 
      gutterBottom
    >
      Aggregate data for films from various sources around the web
    </Typography>
  );
};

export default InfoBar;
