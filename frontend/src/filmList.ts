import { useState, useCallback } from 'react';
import { Film } from './generated';

/**
 * @returns {[<Film[]>, (Film) => void]}
 */
const useFilmList = () => {
  const [filmList, setFilmList] = useState<Film[]>([]);

  const addFilm = useCallback((film: Film) => {
    const index = filmList.findIndex((f) => f.imdb_id === film.imdb_id);
    if (index === -1) {
      setFilmList([...filmList, film]);
    }
  }, []);

  return [filmList, addFilm];
};

export default useFilmList;
