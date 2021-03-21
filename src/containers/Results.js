import React, { useEffect, useState } from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Box from '@material-ui/core/Box';
import qs from 'query-string'
import axios from 'axios';
import ResultsTable from './ResultsTable';
import { useInterval } from '../utils';

const completed = (completion) => (
  parseInt(completion, 10) === 100
);

const Results = ({ location }) => {
  const { batch } = qs.parse(location.search);

  const [films, setFilms] = useState([]);
  const [completion, setCompletion] = useState(false);

  useEffect(() => {
    axios.get(`/batches/${batch}`)
      .then(res => {
        const { data: { films, completion } } = res;
        setFilms(films);
        setCompletion(completion)
      });
  }, [batch]);

  useInterval(() => {
    axios.get(`/batches/${batch}`)
      .then(res => {
        const { data: { films, completion } } = res;
        setFilms(films);
        setCompletion(completion)
      });
  }, 3000);

  return (
    <>
      <Box mb={5}>
        <LinearProgress variant="determinate" value={completion} />
      </Box>
      {completed(completion) && (
        <ResultsTable films={films} />
      )}
    </>
  );
};

export default Results;
