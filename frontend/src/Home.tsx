import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Page from './Page';
import Search from './Search';
import FilmTable from './FilmTable';
import { FilmListItem } from './types';
import { utilsApi } from './providers/env';

const Home = () => {
  const [filmList, setFilmList] = React.useState<FilmListItem[]>([]);

  const addFilm = (option: FilmListItem) => {
    const index = filmList.findIndex((f) => f.tmdb_id === option.tmdb_id);
    if (index === -1) {
      setFilmList([...filmList, option]);
    }
  };

  React.useEffect(() => {
    const ping = async () => {
      await utilsApi.ping();
    };

    ping();
  }, []);

  return (
    <Page>
      <Box sx={{ flexGrow: 1 }}>
        <Grid container spacing={2}>
          <Grid item xs={12} md={4}>
            <Search addFilm={addFilm} />
          </Grid>
          <Grid item xs={12} md={8}>
            <FilmTable films={filmList} />
          </Grid>
        </Grid>
      </Box>
    </Page>
  );
};

export default Home;
