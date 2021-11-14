import React from 'react';
import ReactDOM from 'react-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import './index.css';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';
import '@fontsource/eb-garamond';

const theme = createTheme({
  typography: {
    fontFamily: ['EB Garamond', 'serif'].join(','),
  },
});

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <App />
      </ThemeProvider>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
