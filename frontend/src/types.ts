import { Dispatch } from 'react';
import { Film } from './generated/models';

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
