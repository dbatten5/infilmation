import React from 'react';
import Box from '@mui/material/Box';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import debounce from 'lodash.debounce';
import { SearchResult } from './generated/models';
import { filmsApi } from './providers/env';
import { useStateContext } from './state';

const renderOptionLabel = (option: string | SearchResult) =>
  typeof option === 'string' ? option : `${option.title} (${option.year})`;

const Search = () => {
  const { dispatch } = useStateContext();
  const [value, setValue] = React.useState<SearchResult | null>(null);
  const [inputValue, setInputValue] = React.useState('');
  const [options, setOptions] = React.useState<SearchResult[]>([]);

  const fetchOptions = async (query: string) => {
    if (query) {
      try {
        const response = await filmsApi.searchFilms({ query });
        setOptions(response.data);
      } catch (error) {
        console.error(error);
      }
    }
  };

  const postFilm = async (film: SearchResult) => {
    try {
      const createFilmResponse = await filmsApi.createFilm({ filmIn: film });
      dispatch({
        type: 'ADD_FILM',
        payload: createFilmResponse.data,
      });
    } catch (error) {
      console.error(error);
    }
  };

  const debouncedFetchOptions = React.useMemo(
    () => debounce(fetchOptions, 1000),
    []
  );

  React.useEffect(() => {
    debouncedFetchOptions(inputValue);
  }, [inputValue, debouncedFetchOptions]);

  return (
    <Box>
      <Autocomplete
        id="film-search-bar"
        sx={{ width: '100%' }}
        getOptionLabel={renderOptionLabel}
        filterOptions={(x) => x}
        options={options}
        includeInputInList
        clearOnEscape
        popupIcon={false}
        value={value}
        blurOnSelect
        onInputChange={(event, newInputValue) => {
          setInputValue(newInputValue);
        }}
        onClose={() => {
          setInputValue('');
          setValue(null);
        }}
        onChange={(event: any, newValue: SearchResult | null) => {
          if (newValue) {
            postFilm(newValue);
          }
        }}
        renderInput={(params) => (
          /* eslint-disable react/jsx-props-no-spreading */
          <TextField {...params} label="Start typing..." fullWidth />
        )}
      />
    </Box>
  );
};

export default Search;
