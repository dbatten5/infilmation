import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Page from './Page';
import Search from './Search';
import FilmList from './FilmList';

const Home = () => (
  <Page>
    <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2}>
        <Grid item xs={4}>
          <Search />
        </Grid>
        <Grid item xs={4}>
          <FilmList />
        </Grid>
        <Grid item xs={4}>
          <p>third</p>
        </Grid>
      </Grid>
    </Box>
  </Page>
);

export default Home;
