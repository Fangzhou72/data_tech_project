Part A 

1. Set your environment in your terminal run the following line: 
export ‘BEARER_TOKEN’ = ‘<your_bearer_token>’

For example: 
export 'BEARER_TOKEN'='AAAAAAAAAAAAAAAAAAAAAIVpVAEAAAAAm%2BxS5JHZlbgJ40MtHcpG%2FDWG6fA%3DJSDGtviJIu4q69N1OxT7AxGTEfomM7IreXNc5mOoMwAnztcEMd'

2. Run the server.py file 
Enter the following line to open the file:
python server.py

If it shows 200 and starts to print Datetime, then we successfully execute the file.

3. Run the server.py file with json file
Enter the following line to open the file:
python server.py <your_jsonfile >

For example:
python server.py test.json

By doing so, the python file will copy the content in json file to tweets.txt.

Part B

4. Run the word_count.py file
Enter the following line to execute the file code:
python word_count.py '<your_word_or_phrase>'

For example (to count instance of single word):
python word_count.py 'hello' 

For example (to count instances of multi-word phrase):
python word_count.py 'different check'

Part C

5. Run the vocabulary_size.py file:
Enter the following line to execute the file code:
python vocabulary_size.py

It will print out a number indicating the number of unique words in tweets.txt
