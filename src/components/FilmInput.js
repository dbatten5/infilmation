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

const FilmInput = ({ films, onChange }) => {
  const classes = useStyles();

  return (
    <TextField
      id="films-input"
      label="Films"
      placeholder="Write your films here (1 per line please)"
      fullWidth
      multiline
      value={films}
      onChange={onChange}
      variant="outlined"
      className={classes.field}
      InputProps={{ className: classes.input }}
    />
  );
};

export default FilmInput;
