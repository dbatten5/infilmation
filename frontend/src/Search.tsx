import React from 'react';
import Box from '@mui/material/Box';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import CircularProgress from '@mui/material/CircularProgress';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert, { AlertProps } from '@mui/material/Alert';
import debounce from 'lodash.debounce';
import { SearchResult } from './generated/models';
import { filmsApi } from './providers/env';
import { FilmListItem } from './types';

/* eslint-disable prefer-arrow-callback */
const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(
  props,
  ref
) {
  /* eslint-disable react/jsx-props-no-spreading */
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const renderOptionLabel = (option: string | SearchResult) =>
  typeof option === 'string' ? option : `${option.title} (${option.year})`;

type Props = {
  addFilm: (option: FilmListItem) => void;
};

const SearchingText = () => (
  <Stack direction="row" alignItems="center">
    <Typography variant="body1">Searching...</Typography>
    <CircularProgress size="1rem" sx={{ ml: '1rem' }} />
  </Stack>
);

const Search = ({ addFilm }: Props) => {
  const [value, setValue] = React.useState<SearchResult | null>(null);
  const [inputValue, setInputValue] = React.useState('');
  const [options, setOptions] = React.useState<SearchResult[]>([]);
  const [loading, setLoading] = React.useState<boolean>(false);
  const [alertOpen, setAlertOpen] = React.useState<boolean>(false);

  const handleAlertClose = (
    event: React.SyntheticEvent | Event,
    reason?: string,
  ) => {
    if (reason === 'clickaway') {
      return;
    }

    setAlertOpen(false);
  };

  const fetchOptions = async (query: string) => {
    if (query) {
      try {
        const response = await filmsApi.searchFilms({ query });
        setOptions(response.data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }
  };

  const postFilm = async (film: SearchResult) => {
    try {
      const newFilmResponse = await filmsApi.createFilm({ filmIn: film });
      addFilm({ ...newFilmResponse.data, loading: false });
    } catch (error) {
      addFilm({ ...film, loading: false });
      setAlertOpen(true);
    }
  };

  const handleSelect = (option: SearchResult) => {
    setInputValue('');
    addFilm({ ...option, loading: true });
    postFilm(option);
    setOptions([]);
  };

  const debouncedFetchOptions = React.useMemo(
    () => debounce(fetchOptions, 500),
    []
  );

  React.useEffect(() => {
    debouncedFetchOptions(inputValue);
  }, [inputValue, debouncedFetchOptions]);

  return (
    <Box>
      <Autocomplete
        id="film-search-bar"
        getOptionLabel={renderOptionLabel}
        filterOptions={(x) => x}
        options={options}
        open={!!inputValue}
        loading={loading}
        loadingText={<SearchingText />}
        selectOnFocus
        autoHighlight
        sx={{
          '& .MuiAutocomplete-inputRoot': {
            bgcolor: 'white',
            boxShadow: 1,
          },
        }}
        popupIcon={false}
        value={value}
        onInputChange={(event, newInputValue) => {
          setLoading(true);
          setInputValue(newInputValue);
        }}
        onClose={() => {
          setInputValue('');
          setValue(null);
        }}
        onChange={(event: any, newValue: SearchResult | null) => {
          if (newValue) {
            handleSelect(newValue);
          }
        }}
        renderInput={(params) => (
          /* eslint-disable react/jsx-props-no-spreading */
          <TextField
            {...params}
            placeholder="Start typing a film name..."
            fullWidth
          />
        )}
      />
      <Snackbar
        open={alertOpen}
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        autoHideDuration={6000}
        onClose={handleAlertClose}
      >
        <Alert
          onClose={handleAlertClose}
          severity="error"
          sx={{ width: '100%' }}
        >
          Whoops! Something went wrong
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default Search;
