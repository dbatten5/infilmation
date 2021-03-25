import React from 'react';
import Button from '@material-ui/core/Button';
import { useHistory } from "react-router-dom";

import axios from 'axios';

const FilmSubmit = ({ films }) => {
  const history = useHistory();

  const onSubmit = () => {
    axios.post('/batches/', { raw_titles: films })
      .then(res => {
        const key = res.data.key;
        history.push(`/results?batch=${key}`);
      })
  }

  return (
    <Button 
      variant="contained" 
      size="large" 
      onClick={onSubmit}
      disableElevation 
      fullWidth
    >
      Get Results
    </Button>
  );
};

export default FilmSubmit;
