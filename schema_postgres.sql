DROP TABLE IF EXISTS WORD_STREAM;
DROP TABLE IF EXISTS MINUTE_SUMMARY;
DROP TABLE IF EXISTS WORD_TRENDINESS;

CREATE TABLE WORD_STREAM (
  stream_id SERIAL PRIMARY KEY, 
  word varchar(255) NOT NULL, 
  timestamp varchar(50) NOT NULL
);

CREATE TABLE MINUTE_SUMMARY (
  minute varchar(50) Primary Key,
  total_word_count int NOT NULL, 
  vocab_size int NOT NULL
);

CREATE TABLE WORD_TRENDINESS (
  word varchar(255) NOT NULL, 
  minute varchar(50) NOT NULL,
  word_count int NOT NULL, 
  trendiness int NOT NULL,
  Primary Key (word, minute)
);
