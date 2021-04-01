const env = process.env.NODE_ENV

let httpProtocol = 'http';
let wsProtocol = 'ws';

if (env === 'production') {
    httpProtocol = 'https';
    wsProtocol = 'wss';
}

export const apiUrl = `${httpProtocol}://${process.env.REACT_APP_API_URL}`
export const wsUrl = `${wsProtocol}://${process.env.REACT_APP_API_URL}`
