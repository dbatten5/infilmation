import React from 'react';
import Box from '@mui/material/Box';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import debounce from 'lodash.debounce';
import axios from 'axios';
import { SearchResult } from './generated/models';

const renderOptionLabel = (option: string | SearchResult) =>
  typeof option === 'string' ? option : `${option.title} (${option.year})`;

const Search = () => {
  const [selectedFilms, setSelectedFilms] = React.useState<SearchResult[]>([]);
  const [value, setValue] = React.useState<SearchResult | null>(null);
  const [inputValue, setInputValue] = React.useState('');
  const [options, setOptions] = React.useState<SearchResult[]>([]);

  const fetchOptions = async (query: string) => {
    const encodedQuery = encodeURI(query);
    const url = `http://localhost:8000/api/v1/films/search?query=${encodedQuery}`;
    try {
      const response = await axios.get<SearchResult[]>(url);
      setOptions(response.data);
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
  }, [inputValue]);

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
            setSelectedFilms([...selectedFilms, newValue]);
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
