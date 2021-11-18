import { Dispatch } from 'react';
import { Film, Actor, Director, Genre } from './generated/models';

export interface StateContext {
  filmList: Film[];
}

export type ActionType = {
  type: string;
  payload?: any;
};

export interface Store {
  state: StateContext;
  dispatch: Dispatch<ActionType>;
}

export interface FilmListItem {
  title: string;
  imdb_id?: string;
  tmdb_id?: string;
  id?: number;
  year?: number;
  runtime?: number;
  plot?: string;
  imdb_rating?: number;
  mtc_rating?: string;
  rt_tomato_rating?: string;
  cast?: Array<Actor>;
  directors?: Array<Director>;
  genres?: Array<Genre>;
  loading: boolean;
  human_readable_runtime?: string;
}
