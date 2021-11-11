import React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import { StateProvider } from './state';

function App() {
  return (
    <>
      <CssBaseline />
      <StateProvider>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </StateProvider>
    </>
  );
}

export default App;
