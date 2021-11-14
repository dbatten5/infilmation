/* tslint:disable */
/* eslint-disable */
/**
 * infilmation
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import { MovieTypeEnum } from './movie-type-enum';

/**
 * Schema for a film search result.
 * @export
 * @interface SearchResult
 */
export interface SearchResult {
    /**
     * 
     * @type {string}
     * @memberof SearchResult
     */
    'title': string;
    /**
     * 
     * @type {MovieTypeEnum}
     * @memberof SearchResult
     */
    'kind': MovieTypeEnum;
    /**
     * 
     * @type {number}
     * @memberof SearchResult
     */
    'year'?: number;
    /**
     * 
     * @type {string}
     * @memberof SearchResult
     */
    'imdb_id': string;
}
