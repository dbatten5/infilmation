import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import Box from '@material-ui/core/Box';
import qs from 'query-string'
import DataTable from '../components/DataTable';
import ResultsToolbar from '../components/ResultsToolbar';
import Grid from '@material-ui/core/Grid';
import Header from '../components/Header';
import Container from '@material-ui/core/Container';

const Results = ({ location }) => {
  const { batch } = qs.parse(location.search);

  const [films, setFilms] = useState([]);
  const [completion, setCompletion] = useState(0);
  const [status, setStatus] = useState('started');
  const [isPaused, setPause] = useState(true);
  const [currentFilm, setCurrentFilm] = useState('');

  const ws = useRef(null);

  useEffect(() => {
    axios.get(`/batches/${batch}`)
      .then(res => {
        const { films, status } = res.data;
        setFilms(films);
        setStatus(status)
        if (status !== 'finished') {
          setPause(false);
        }
      });
  }, [batch, completion]);

  useEffect(() => {
    ws.current = new WebSocket(`${process.env.REACT_APP_WS_URL}/batches/${batch}/ws`);
    ws.current.onopen = () => console.log("ws opened");
    ws.current.onclose = () => console.log("ws closed");

    return () => {
      ws.current.close();
    };
  }, []);

  useEffect(() => {
    if (!ws.current) return;

    ws.current.onmessage = e => {
      if (isPaused) return;
      const message = JSON.parse(e.data);
      const { status, completion, current_film: currentFilm } = message;
      setCompletion(completion);
      setStatus(status)
      setCurrentFilm(currentFilm);
    };
  }, [isPaused]);

  return (
    <Grid container direction="column">
      <Grid item>
        <Header />
      </Grid>
      <Grid item>
        <Box pb={10}>
          <Container maxWidth="lg">
            <Box mt={3}>
              <ResultsToolbar status={status} currentFilm={currentFilm} />
            </Box>
            <Box mt={5}>
              <DataTable films={films} />
            </Box>
          </Container>
        </Box>
      </Grid>
    </Grid>
  );
};

export default Results;
