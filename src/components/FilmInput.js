import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles((theme) => ({
  input: {
    height: '100%',
    alignItems: 'flex-start',
  },
  field: {
    height: '100%',
  }
}));

const FilmInput = () => {
  const classes = useStyles();

  const [films, setFilms] = React.useState('');

  const handleChange = (event) => setFilms(event.target.value);

  return (
    <TextField
      id="films-input"
      label="Films"
      placeholder="Write your films here (1 per line please)"
      fullWidth
      multiline
      value={films}
      onChange={handleChange}
      variant="outlined"
      className={classes.field}
      InputProps={{ className: classes.input }}
    />
  );
};

export default FilmInput;
