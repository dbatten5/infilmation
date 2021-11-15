import React from 'react';
import Box from '@mui/material/Box';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import CircularProgress from '@mui/material/CircularProgress';
import debounce from 'lodash.debounce';
import { SearchResult } from './generated/models';
import { filmsApi } from './providers/env';
import { FilmListItem } from './types';

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
      console.error(error);
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
          <TextField {...params} placeholder="Type a film name..." fullWidth />
        )}
      />
    </Box>
  );
};

export default Search;
