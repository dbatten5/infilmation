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
  imdb_id: string;
  id?: number;
  year?: number;
  runtime?: number;
  plot?: string;
  imdb_rating?: number;
  mtc_rating?: number;
  rt_tomato_rating?: number;
  cast?: number | Actor | Array<Actor>;
  directors?: number | Director | Array<Director>;
  genres?: number | Genre | Array<Genre>;
  loading: boolean;
}
