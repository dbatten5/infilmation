import React from 'react';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import { makeStyles } from '@material-ui/core/styles';
import { useTheme } from '@material-ui/core/styles';
import useMediaQuery from '@material-ui/core/useMediaQuery';

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
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.down('sm'));

  return (
    <Box mb={3}>
      <Typography variant="body2" gutterBottom className={classes.step}>
        {matches && <>&#94;</>}
        {!matches && <>&lt;</>}
        &nbsp;&nbsp;Enter films (1 per line)
      </Typography>
    </Box>
  );
};

export default Guide;
