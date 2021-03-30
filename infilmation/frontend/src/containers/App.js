import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Home from './Home';
import Results from './Results';
import { Switch, Route } from 'react-router-dom';

function App() {
  return (
    <>
      <CssBaseline />
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/results" component={Results} />
      </Switch>
    </>
  );
}

export default App;
