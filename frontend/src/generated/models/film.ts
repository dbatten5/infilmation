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
 * Schema for the `Film` model.
 * @export
 * @interface Film
 */
export interface Film {
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'id'?: number;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'title': string;
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'year'?: number;
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'runtime'?: number;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'plot'?: string;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'imdb_id'?: string;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'imdb_title'?: string;
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'imdb_year'?: number;
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'imdb_rating'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof Film
     */
    'imdb_low_confidence'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'mtc_title'?: string;
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'mtc_year'?: number;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'mtc_rating'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof Film
     */
    'mtc_low_confidence'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'rt_title'?: string;
    /**
     * 
     * @type {number}
     * @memberof Film
     */
    'rt_year'?: number;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'rt_tomato_rating'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof Film
     */
    'rt_low_confidence'?: boolean;
    /**
     * 
     * @type {number | Actor | Array<Actor>}
     * @memberof Film
     */
    'cast'?: number | Actor | Array<Actor>;
    /**
     * 
     * @type {number | Director | Array<Director>}
     * @memberof Film
     */
    'directors'?: number | Director | Array<Director>;
    /**
     * 
     * @type {number | Genre | Array<Genre>}
     * @memberof Film
     */
    'genres'?: number | Genre | Array<Genre>;
    /**
     * 
     * @type {string}
     * @memberof Film
     */
    'tmdb_id'?: string;
}

