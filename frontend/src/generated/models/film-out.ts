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


import { Actor } from './actor';
import { Director } from './director';
import { Genre } from './genre';

/**
 * Schema for create film requests.
 * @export
 * @interface FilmOut
 */
export interface FilmOut {
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'id': number;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'title': string;
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'year'?: number;
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'runtime'?: number;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'plot'?: string;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'imdb_id'?: string;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'imdb'?: string;
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'imdb_year'?: number;
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'imdb_rating'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof FilmOut
     */
    'imdb_low_confidence'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'mtc_title'?: string;
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'mtc_year'?: number;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'mtc_rating'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof FilmOut
     */
    'mtc_low_confidence'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'rt_title'?: string;
    /**
     * 
     * @type {number}
     * @memberof FilmOut
     */
    'rt_year'?: number;
    /**
     * 
     * @type {string}
     * @memberof FilmOut
     */
    'rt_tomato_rating'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof FilmOut
     */
    'rt_low_confidence'?: boolean;
    /**
     * 
     * @type {Array<Actor>}
     * @memberof FilmOut
     */
    'cast': Array<Actor>;
    /**
     * 
     * @type {Array<Director>}
     * @memberof FilmOut
     */
    'directors': Array<Director>;
    /**
     * 
     * @type {Array<Genre>}
     * @memberof FilmOut
     */
    'genres': Array<Genre>;
}

