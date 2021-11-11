import { ActionType, StateContext } from './types';
import { Film } from './generated';

const reducer = (state: StateContext, action: ActionType): any => {
  switch (action.type) {
    case 'ADD_FILM': {
      const index = state.filmList.findIndex(
        (f: Film) => f.imdb_id === action.payload.imdb_id
      );
      if (index === -1) {
        return {
          ...state,
          filmList: state.filmList.concat(action.payload),
        };
      }
      return state;
    }
    default:
      return state;
  }
};

export default reducer;
