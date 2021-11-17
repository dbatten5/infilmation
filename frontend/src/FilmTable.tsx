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
import SvgIcon from '@mui/material/SvgIcon';
import Stack from '@mui/material/Stack';
import Link from '@mui/material/Link';
import Collapse from '@mui/material/Collapse';
import Grid from '@mui/material/Grid';
import { FilmListItem } from './types';
import Imdb from './icons/IMDb';
import Mtc from './icons/mtc';
import Rt from './icons/rt';
import Play from './icons/play';
import FingerPoint from './icons/finger-point';

const createData = ({
  id,
  title,
  imdb_id,
  year,
  human_readable_runtime,
  imdb_rating,
  mtc_rating,
  rt_tomato_rating,
  loading,
  plot,
}: FilmListItem) => ({
  id,
  title,
  imdb_id,
  year,
  human_readable_runtime,
  imdb_rating,
  mtc_rating,
  rt_tomato_rating,
  loading,
  plot,
});

type Props = {
  films: FilmListItem[];
};

const Row = (props: { row: ReturnType<typeof createData> }) => {
  const { row } = props;
  const [open, setOpen] = React.useState(false);

  const toggleOpen = () => {
    setOpen(!open);
  };

  return (
    <>
      <TableRow
        key={row.imdb_id}
        sx={{
          '&:last-child td, &:last-child th': { border: 0 },
          cursor: 'pointer',
          '&:hover': { bgcolor: '#EEEDE7' },
        }}
        onClick={toggleOpen}
      >
        <TableCell component="th" scope="row">
          {row.title}
        </TableCell>
        <TableCell align="right">{row.year || '?'}</TableCell>
        <TableCell align="right">
          {row.loading ? (
            <Skeleton animation="wave" variant="text" />
          ) : (
            row.human_readable_runtime || '?'
          )}
        </TableCell>
        <TableCell align="right">
          {row.loading ? (
            <Skeleton animation="wave" variant="text" />
          ) : (
            row.imdb_rating || '?'
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
            row.rt_tomato_rating || '?'
          )}
        </TableCell>
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box sx={{ py: 2 }}>
              <Grid container spacing={1}>
                <Grid item xs={12}>
                  {row.plot}
                </Grid>
                <Grid item xs={4}>
                  <Link
                    href={`https://www.youtube.com/results?search_query=${row.title}+${row.year}+trailer`}
                    color="inherit"
                    target="_blank"
                    underline="none"
                  >
                    <Stack direction="row" alignItems="center">
                      <Box sx={{ mr: '0.35rem' }}>Trailer</Box>
                      <SvgIcon
                        component={Play}
                        sx={{
                          width: '20px',
                          height: '20px',
                          '&:hover': { opacity: 0.6, transition: '0.3s' },
                        }}
                        viewBox="-1 -1 24 24"
                      />
                    </Stack>
                  </Link>
                </Grid>
              </Grid>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </>
  );
};

const FilmTable = ({ films }: Props) => {
  const rows = films.map((film) => createData(film));

  return (
    <TableContainer component={Paper} sx={{ mb: '1rem' }}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Title</TableCell>
            <TableCell align="right">Year</TableCell>
            <TableCell align="right">Runtime</TableCell>
            <TableCell>
              <Stack justifyContent="center" alignItems="flex-end">
                <SvgIcon
                  component={Imdb}
                  sx={{
                    width: '40px',
                    height: '25px',
                  }}
                  viewBox="0 0 64 32"
                />
              </Stack>
            </TableCell>
            <TableCell align="right">
              <Stack justifyContent="center" alignItems="flex-end">
                <SvgIcon
                  component={Mtc}
                  sx={{
                    width: '25px',
                    height: '25px',
                  }}
                  viewBox="0 0 29.4 29.7"
                />
              </Stack>
            </TableCell>
            <TableCell align="right">
              <Stack justifyContent="center" alignItems="flex-end">
                <SvgIcon
                  component={Rt}
                  sx={{
                    width: '25px',
                    height: '25px',
                  }}
                  viewBox="0 0 80 80"
                />
              </Stack>
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <Row key={row.imdb_id} row={row} />
          ))}
        </TableBody>
      </Table>
      {rows.length === 0 && (
        <Box sx={{ width: '100%', p: '2rem' }}>
          <Stack
            alignItems="center"
            justifyContent="center"
            direction="column"
            sx={{ width: '100%' }}
          >
            <SvgIcon
              component={FingerPoint}
              sx={{
                width: '5rem',
                height: '5rem',
              }}
              viewBox="40 0 150 150"
            />
            <Typography variant="subtitle1">No films yet!</Typography>
          </Stack>
        </Box>
      )}
    </TableContainer>
  );
};

export default FilmTable;
