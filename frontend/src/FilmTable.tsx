import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Skeleton from '@mui/material/Skeleton';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { FilmListItem } from './types';

const createRow = ({
  id,
  title,
  imdb_id,
  year,
  runtime,
  imdb_rating,
  mtc_rating,
  rt_tomato_rating,
  loading,
}: FilmListItem) => ({
  id,
  title,
  imdb_id,
  year,
  runtime,
  imdb_rating,
  mtc_rating,
  rt_tomato_rating,
  loading,
});

type Props = {
  films: FilmListItem[];
};

const FilmTable = ({ films }: Props) => {
  if (!films.length) {
    return (
      <Box sx={{ width: '100%' }}>
        <Typography variant="h6">
          Start typing the name of a film in the search bar
        </Typography>
      </Box>
    );
  }

  const rows = films.map((film) => createRow(film));

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Title</TableCell>
            <TableCell align="right">Year</TableCell>
            <TableCell align="right">Runtime</TableCell>
            <TableCell align="right">IMDb</TableCell>
            <TableCell align="right">Metacritic</TableCell>
            <TableCell align="right">Rotten Tomatoes</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.imdb_id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.title}
              </TableCell>
              <TableCell align="right">{row.year}</TableCell>
              <TableCell align="right">
                {row.loading ? (
                  <Skeleton animation="wave" variant="text" />
                ) : (
                  row.runtime
                )}
              </TableCell>
              <TableCell align="right">
                {row.loading ? (
                  <Skeleton animation="wave" variant="text" />
                ) : (
                  row.imdb_rating
                )}
              </TableCell>
              <TableCell align="right">
                {row.loading ? (
                  <Skeleton animation="wave" variant="text" />
                ) : (
                  row.mtc_rating
                )}
              </TableCell>
              <TableCell align="right">
                {row.loading ? (
                  <Skeleton animation="wave" variant="text" />
                ) : (
                  row.rt_tomato_rating
                )}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default FilmTable;
