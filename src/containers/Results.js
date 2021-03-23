import React, { useEffect, useState, useRef } from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Box from '@material-ui/core/Box';
import qs from 'query-string'
import DataTable from '../components/DataTable';


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
      console.log("e", message);
    };
  }, [isPaused]);

  return (
    <>
      <Box mb={5}>
        <LinearProgress variant="determinate" value={completion} />
      </Box>
      <DataTable films={films} />
    </>
  );
};

export default Results;
