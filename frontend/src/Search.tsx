import React from 'react';
import Box from '@mui/material/Box';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import debounce from 'lodash.debounce';
import { SearchResult } from './generated/models';
import { filmsApi } from './providers/env';
import { FilmListItem } from './types';

const renderOptionLabel = (option: string | SearchResult) =>
  typeof option === 'string' ? option : `${option.title} (${option.year})`;

type Props = {
  addFilm: (option: FilmListItem) => void;
};

const Search = ({ addFilm }: Props) => {
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
        getOptionLabel={renderOptionLabel}
        filterOptions={(x) => x}
        options={options}
        open={!!inputValue && options.length > 0}
        includeInputInList
        selectOnFocus
        popupIcon={false}
        value={value}
        onInputChange={(event, newInputValue) => {
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
