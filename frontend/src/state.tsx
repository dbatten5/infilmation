import React, { useContext, useReducer } from 'react';
import reducer from './reducer';
import { StateContext, Store } from './types';

const defaultState: StateContext = { filmList: [] };

const infilmationContext = React.createContext<Store>({} as Store);

export const useStateContext = () => useContext(infilmationContext);

type StateProviderProps = {
  children: React.ReactNode;
};

export const StateProvider = ({ children }: StateProviderProps) => {
  const [state, dispatch] = useReducer(reducer, defaultState);
  return (
    <infilmationContext.Provider value={{ state, dispatch }}>
      {children}
    </infilmationContext.Provider>
  );
};
