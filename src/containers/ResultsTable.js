import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const ResultsTable = ({ films }) => {
  return (
    <TableContainer component={Paper}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Title</TableCell>
            <TableCell>Year</TableCell>
            <TableCell>Genres</TableCell>
            <TableCell>Runtime&nbsp;(m)</TableCell>
            <TableCell>Cast</TableCell>
            <TableCell>Director(s)</TableCell>
            <TableCell>Plot</TableCell>
            <TableCell>IMDb Score</TableCell>
            <TableCell>Metacritic Score</TableCell>
            <TableCell>RT Tomato Score</TableCell>
            <TableCell>RT Audience Score</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {films.map((row) => (
            <TableRow key={row.key}>
              <TableCell component="th" scope="row">
                {row.imdb_title}
              </TableCell>
              <TableCell align="right">{row.imdb_year}</TableCell>
              <TableCell align="right">{row.genres}</TableCell>
              <TableCell align="right">{row.runtime}</TableCell>
              <TableCell align="right">{row.cast}</TableCell>
              <TableCell align="right">{row.directors}</TableCell>
              <TableCell align="right">{row.plot}</TableCell>
              <TableCell align="right">{row.imdb_score}</TableCell>
              <TableCell align="right">{row.mtc_score}</TableCell>
              <TableCell align="right">{row.rt_tomato_score}</TableCell>
              <TableCell align="right">{row.rt_audience_score}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ResultsTable;
