# README

# Create PostgreSQL tables

- Run the command in your terminal: `psql`
- Then run the SQL command: `create database twitter;`
- Then run the SQL command: `psql twitter < schema_postgres.sql`

# Read tweets and load into database

- Read-in tweets by set the file name as **tweets.txt** and place it in the same path
- Then run the Python code in your terminal: `python server_postgres.py`

# Compute the frequency of words in the current minute

- Run the Python code in your terminal: `python word_count_postgres.py`

# Compute the number of unique words in the current minute

- Run the Python code in your terminal: `python vocabulary_size_postgres.py`

# Compute the trendiness score

- Run the Python code in your terminal: `python trendiness_postgres.py`
