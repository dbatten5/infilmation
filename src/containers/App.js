import React from 'react';
import Header from '../components/Header/Header';
import Home from './Home';
import Results from './Results';
import { Switch, Route } from 'react-router-dom';

function App() {
  return (
    <>
      <Header />
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/results" component={Results} />
      </Switch>
    </>
  );
}

export default App;
