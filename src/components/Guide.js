import React from 'react';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  step: {
    fontFamily: 'HelveticaNeue-Light',
    color: 'black',
    fontSize: '1.4rem',
    fontWeight: '300',
    fontStyle: 'italic',
  },
}));

const Guide = () => {
  const classes = useStyles();

  return (
    <Box mb={3}>
      <Typography variant="body2" gutterBottom className={classes.step}>
        > Enter films (1 per line)
      </Typography>
      <Typography variant="body2" gutterBottom className={classes.step}>
        > Get your data
      </Typography>
    </Box>
  );
};

export default Guide;
