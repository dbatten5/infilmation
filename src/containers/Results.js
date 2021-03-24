import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import Box from '@material-ui/core/Box';
import qs from 'query-string'
import DataTable from '../components/DataTable';
import LinearProgressWithLabel from '../components/LinearProgressWithLabel';


const Results = ({ location }) => {
  const { batch } = qs.parse(location.search);

  const [films, setFilms] = useState([]);
  const [completion, setCompletion] = useState(0);
  const [status, setStatus] = useState('started');
  const [isPaused, setPause] = useState(false)

  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(`ws://localhost:8000/batches/${batch}/ws`);
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
      const { status, completion } = message;
      setCompletion(completion);
      setStatus(status);
    };
  }, [isPaused]);

  useEffect(() => {
    axios.get(`/batches/${batch}`)
      .then(res => {
        const films = res.data.films;
        setFilms(films);
      });
  }, [batch, completion]);

  return (
    <>
      {status !== 'finished' && (
        <Box mb={5}>
          <LinearProgressWithLabel variant="determinate" value={completion} />
        </Box>
      )}
      <DataTable films={films} />
    </>
  );
};

export default Results;
