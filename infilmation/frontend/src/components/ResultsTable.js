import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Tooltip from '@material-ui/core/Tooltip';

const joinList = (list, elements = 2) => (
  list.slice(0, elements).map(e => e.name).join(', ')
)

const useStyles = makeStyles((theme) => ({
  paper: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    width: 'max-content'
  }
}));

const ResultsTable = ({ films }) => {
  const classes = useStyles();

  return (
    <TableContainer component={Paper} className={classes.paper}>
      <Table aria-label="infilmation results table">
        <TableHead>
          <TableRow>
            <TableCell width="10%">Title</TableCell>
            <TableCell>Year</TableCell>
            <TableCell>Genres</TableCell>
            <TableCell>Runtime</TableCell>
            <TableCell>Cast</TableCell>
            <TableCell>Director(s)</TableCell>
            <TableCell>Plot</TableCell>
            <Tooltip title="IMDb Score"><TableCell>IMDb</TableCell></Tooltip>
            <Tooltip title="Metacritic Score"><TableCell>Mtc</TableCell></Tooltip>
            <Tooltip title="Rotten Tomatoes Tomatometer Score"><TableCell>RTT</TableCell></Tooltip>
            <Tooltip title="Rotten Tomatoes Audience Score"><TableCell>RTA</TableCell></Tooltip>
          </TableRow>
        </TableHead>
        <TableBody>
          {films.map((row) => (
            <TableRow key={row.key}>
              <TableCell> {row.imdb_title} </TableCell>
              <TableCell>{row.imdb_year}</TableCell>
              <TableCell>{joinList(row.genres)}</TableCell>
              <TableCell>{row.runtime}</TableCell>
              <TableCell>{joinList(row.cast, 3)}</TableCell>
              <TableCell>{joinList(row.directors)}</TableCell>
              <TableCell>{row.plot}</TableCell>
              <TableCell>{row.imdb_score}</TableCell>
              <TableCell>{row.mtc_score}</TableCell>
              <TableCell>{row.rt_tomato_score}</TableCell>
              <TableCell>{row.rt_audience_score}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ResultsTable;
