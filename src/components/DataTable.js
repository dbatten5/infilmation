import React from 'react';
import { DataGrid } from '@material-ui/data-grid';
import Typography from '@material-ui/core/Typography';
import Tooltip from '@material-ui/core/Tooltip';

const renderLargeCell = (params) => (
  <Tooltip title={params.value}>
    <Typography
      variant="body2"
      component="p"
      align="left"
      noWrap
    >
      {params.value}
    </Typography>
  </Tooltip>
);

const makeList = (list, elements = 2) => (
  list.slice(0, elements).map(e => e.name).join(', ')
);

const createRow = ({
  id,
  title,
  imdb_year,
  genres,
  runtime,
  cast,
  directors,
  plot,
  imdb_score,
  mtc_score,
  rt_tomato_score,
  rt_audience_score,
}) => (
  {
    id,
    title,
    imdb_year,
    genres: makeList(genres, 2),
    runtime,
    cast: makeList(cast, 3),
    directors: makeList(directors, 3),
    plot,
    imdb_score,
    mtc_score,
    rt_tomato_score,
    rt_audience_score,
  }
)

const columns = [
  {
    field: 'title',
    headerName: 'Title',
    renderCell: renderLargeCell,
    width: 150,
  },
  { field: 'imdb_year', headerName: 'Year', width: 70 },
  {
    field: 'genres',
    headerName: 'Genres',
    renderCell: renderLargeCell,
    sortable: false,
  },
  { field: 'runtime', headerName: 'Runtime', type: 'number', width: 90 },
  {
    field: 'cast',
    headerName: 'Cast',
    renderCell: renderLargeCell,
    width: 140,
    sortable: false,
  },
  {
    field: 'directors',
    headerName: 'Directors',
    renderCell: renderLargeCell,
    sortable: false,
  },
  {
    field: 'plot',
    headerName: 'Plot',
    width: 300,
    renderCell: renderLargeCell,
    sortable: false,
  },
  { field: 'imdb_score', headerName: 'IMDb', description: 'IMDb Score', width: 70 },
  { field: 'mtc_score', headerName: 'Mtc', description: 'Metacritic Score', width: 70 },
  { field: 'rt_tomato_score', headerName: 'RTT', description: 'Rotten Tomatoes Tomatometer Score', width: 70 },
  { field: 'rt_audience_score', headerName: 'RTA', description: 'Rotten Tomatoes Audience Score', width: 70 },
];

const DataTable = ({ films }) => {
  const filmsList = films.map(film => createRow(film));

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      <div style={{ flexGrow: 1 }}>
        <DataGrid 
          rows={filmsList} 
          columns={columns} 
          pageSize={5} 
          checkboxSelection={false} 
          disableColumnMenu
          disableSelectionOnClick
          hideFooter
          autoHeight
        />
      </div>
    </div>
  );
};

export default DataTable;
