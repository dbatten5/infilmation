import { Configuration, FilmsApi, UtilsApi } from '../generated';

// prettier-ignore
export const basePath = " ";

const apiConfig: Configuration = new Configuration({
  basePath,
});

export const filmsApi: FilmsApi = new FilmsApi(apiConfig);

export const utilsApi: UtilsApi = new UtilsApi(apiConfig);
