import React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridRowsProp, GridColDef } from '@mui/x-data-grid';
import Page from './Page';
import { useStateContext } from './state';
import { Film } from './generated';

const createRow = ({
  id,
  title,
  year,
  runtime,
  imdb_rating,
  mtc_rating,
  rt_tomato_rating,
}: Film) => ({
  id,
  title,
  year,
  runtime,
  imdb_rating,
  mtc_rating,
  rt_tomato_rating,
});

const columns: GridColDef[] = [
  {
    field: 'title',
    headerName: 'Title',
    width: 150,
  },
  { field: 'year', headerName: 'Year', width: 70 },
  { field: 'runtime', headerName: 'Runtime', type: 'number', width: 90 },
  {
    field: 'imdb_rating',
    headerName: 'IMDb',
    description: 'IMDb Score',
    width: 70,
  },
  {
    field: 'mtc_rating',
    headerName: 'Mtc',
    description: 'Metacritic Score',
    width: 70,
  },
  {
    field: 'rt_tomato_rating',
    headerName: 'RTT',
    description: 'Rotten Tomatoes Tomatometer Score',
    width: 70,
  },
];

const Results = () => {
  const { state } = useStateContext();

  const filmList: GridRowsProp = state.filmList.map((film) => createRow(film));

  return (
    <Page>
      <Box sx={{ flexGrow: 1 }}>
        <DataGrid
          rows={filmList}
          columns={columns}
          checkboxSelection={false}
          disableColumnMenu
          disableSelectionOnClick
          hideFooter
          autoHeight
        />
      </Box>
    </Page>
  );
};

export default Results;
