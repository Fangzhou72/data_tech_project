CREATE TABLE WORD_STREAM (
  stream_id int Primary Key, 
  word varchar(255) NOT NULL, 
  timestamp datetime NOT NULL, 
  minute datetime NOT NULL
);

CREATE TABLE MINUTE_SUMMARY (
  minute datetime Primary Key,
  total_word_count int NOT NULL, 
  vocab_size int NOT NULL
);

CREATE TABLE WORD_TRENDINESS (
  word varchar(255) NOT NULL, 
  minute datetime NOT NULL,
  word_count int NOT NULL, 
  trendiness int NOT NULL,
  Primary Key (word, minute)
);
