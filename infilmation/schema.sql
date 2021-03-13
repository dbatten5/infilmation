DROP TABLE IF EXISTS movie;

CREATE TABLE movie (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  year INTEGER,
  genres TEXT,
  runtime TEXT,
  cast TEXT,
  directors TEXT,
  plot TEXT,
  imdb_title TEXT,
  imdb_year INTEGER,
  imdb_score TEXT,
  imdb_low_confidence INTEGER,
  mtc_title TEXT,
  mtc_year INTEGER,
  mtc_score TEXT,
  mtc_low_confidence INTEGER,
  rt_title TEXT,
  rt_year INTEGER,
  rt_tomato_score TEXT,
  rt_audience_score TEXT,
  rt_low_confidence INTEGER
);
