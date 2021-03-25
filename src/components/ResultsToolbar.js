import React from 'react';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import CircularProgress from '@material-ui/core/CircularProgress';
import Button from '@material-ui/core/Button';

const ResultsToolbar = ({ status, currentFilm }) => {
  return (
    <Box mt={0}>
      <Grid container direction="row" justify="flex-end">
        <Grid item>
          <Box>
            {status === "started" && (
              <Grid alignItems="center" container direction="row" spacing={3}>
                <Grid item>
                  <Typography variant="body1">
                    Fetching {currentFilm}...
                  </Typography>
                </Grid>
                <Grid item>
                  <CircularProgress size={20} />
                </Grid>
              </Grid>
            )}
            {status === "finished" && (
              <Button variant="contained">Download CSV</Button>
            )}
          </Box>
        </Grid>
      </Grid>
    </Box>
  );
};

export default ResultsToolbar;
