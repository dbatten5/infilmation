import { Dispatch } from 'react';
import { SearchResult } from './generated/models';

export interface StateContext {
  filmList: SearchResult[];
}

export type ActionType = {
  type: string;
  payload?: any;
};

export interface Store {
  state: StateContext;
  dispatch: Dispatch<ActionType>;
}
