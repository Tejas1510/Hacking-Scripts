## Document Summarizer
Document Summarization Python helps in summarizing and shortening the text in the user feedback. It can be done with the help of an algorithm that can help in reducing the text bodies while keeping their original meaning intact or by giving insights into their original text.
### Steps used
1 - Importing required libraries<br>
2 - Removing Stop Words and storing them in a separate array of words.

Stop Word

Any word like (is, a, an, the, for) that does not add value to the meaning of a sentence.<br>
3 - Create a frequency table of words
A python dictionary that’ll keep a record of how many times each word appears in the feedback after removing the stop words.we can use the dictionary over every sentence to know which sentences have the most relevant content in the overall text.<br>
4 - Assign score to each sentence depending on the words it contains and the frequency table

We can use the sent_tokenize() method to create the array of sentences. Secondly, we will need a dictionary to keep the score of each sentence, we will later go through the dictionary to generate the summary.<br>
5 - Assign a certain score to compare the sentences within the feedback.
A simple approach to compare our scores would be to find the average score of a sentence. The average itself can be a good threshold.<br>