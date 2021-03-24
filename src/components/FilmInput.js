import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles((theme) => ({
  input: {
    height: '100%',
    alignItems: 'flex-start',
    fontSize: '2rem',
  },
  field: {
    height: '100%',
  },
  textarea: {
    height: '100% !important',
    overflowY: 'scroll !important',
  },
}));

const FilmInput = ({ films, onChange }) => {
  const classes = useStyles();

  return (
    <TextField
      id="films-input"
      fullWidth
      multiline
      value={films}
      onChange={onChange}
      variant="outlined"
      className={classes.field}
      InputProps={{
        className: classes.input,
        classes: {
          inputMultiline: classes.textarea,
        }
      }}
    />
  );
};

export default FilmInput;
