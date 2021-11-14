import { Configuration, FilmsApi } from '../generated';

// prettier-ignore
export const basePath = " ";

const apiConfig: Configuration = new Configuration({
  basePath,
});

export const filmsApi: FilmsApi = new FilmsApi(apiConfig);
