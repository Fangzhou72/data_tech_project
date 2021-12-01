DROP TABLE IF EXISTS WORD_STREAM;
DROP TABLE IF EXISTS WORD_TRENDINESS;

CREATE TABLE WORD_STREAM (
  stream_id SERIAL PRIMARY KEY, 
  word varchar(255) NOT NULL, 
  timestamp varchar(100) NOT NULL
);

CREATE TABLE WORD_TRENDINESS (
  stream_id SERIAL PRIMARY KEY, 
  word varchar(255) NOT NULL, 
  trendiness float
);

