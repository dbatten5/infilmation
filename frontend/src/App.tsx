import React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Results from './Results';
import { StateProvider } from './state';

function App() {
  return (
    <>
      <CssBaseline />
      <StateProvider>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </StateProvider>
    </>
  );
}

export default App;
