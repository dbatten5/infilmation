import React from 'react';
import Button from '@material-ui/core/Button';

const FilmSubmit = () => {
  return (
    <Button 
      variant="contained" 
      color="primary" 
      size="large" 
      disableElevation 
      fullWidth
    >
      Submit
    </Button>
  );
};

export default FilmSubmit;
