import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import FilmInput from '../components/FilmInput';
import FilmSubmit from '../components/FilmSubmit';
import Guide from '../components/Guide';

const useStyles = makeStyles((theme) => ({
  grid: {
    height: '100%',
    [theme.breakpoints.down(960)]: {
      flexDirection: 'column',
      flexWrap: 'nowrap',
    },
  },
  textField: {
    [theme.breakpoints.down(960)]: {
      flex: 1,
    },
  },
  submit: {
    [theme.breakpoints.down(960)]: {
      flex: 0,
    },
  }
}));

const FilmForm = () => {
  const classes = useStyles();

  const [films, setFilms] = React.useState('');

  const handleChange = (event) => setFilms(event.target.value);

  return (
    <Box pt={5} height="100%">
      <Grid container spacing={3} direction="row" className={classes.grid}>
        <Grid item xs={12} md={9} className={classes.textField}>
          <FilmInput films={films} onChange={handleChange} />
        </Grid>
        <Grid
          container
          direction="column"
          justify="space-between"
          item
          xs={12}
          md={3}
          className={classes.submit}
        >
          <Guide />
          <FilmSubmit films={films} />
        </Grid>
      </Grid>
    </Box>
  );
};

export default FilmForm;
