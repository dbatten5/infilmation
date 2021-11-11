import { Configuration, FilmsApi } from '../generated';

// prettier-ignore
export const basePath = process.env.REACT_APP_API_BASE || "http://localhost:8000";

const apiConfig: Configuration = new Configuration({
  basePath,
});

export const filmsApi: FilmsApi = new FilmsApi(apiConfig);
