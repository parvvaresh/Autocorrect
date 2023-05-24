# Autocorrect Text using NLP in Python

**Introduction to Autocorrect**

Have you ever wondered about how the Autocorrect features work on the keyboard of a Smartphone? Now almost every smartphone brand regardless of its price provides an autocorrect feature in their keyboards today. 

The main purpose of this notebook, as you have seen the title so you can guess that is to build an Autocorrect Feature. Yes, it’s some kind of similar, but not the exact copy, to that of the smartphone we are using now, but this would be an implementation of Natural Language Processing on a smaller dataset like a book.

Okay, let’s understand how these autocorrect features work. In this notebook, I am going to take you through “How to build Autocorrect with Python”.


**Autocorrect using NLP With Python- How it works?**
![image](https://github.com/parvvaresh/Autocorrect-Feature-using-NLP-in-Python/assets/89921883/7f4a5121-f0a1-4527-ada1-72e68bb5a343)

So let us understand the algorithm.

There are 4 key steps to building an autocorrect model that corrects spelling errors:

1. Identify Misspelled Word — Let us consider an example, how would we get to know the word “drea” is spelled incorrectly or correctly? If a word is spelled correctly then the word will be found in a dictionary and if it is not there then it is probably a Misspelled Word. Hence, when a word is not found in a dictionary then we will flag it for correction.

2. Find ‘n’ Strings Edit distance away — An edit is one of the operations which is performed on a string in order to transform it into another String, and n is nothing but the edit distance that is an edit distance like- 1, 2, 3, so on… which will count the number of edit operations that to be performed. Hence, the edit distance n tells us that how many operations are away from one string to another. Following are the different types of edits:-


              * Insert (will add a letter)
              * Delete (will remove a letter)
              * Switch (it will swap two nearby letters)
              * Replace (exchange one letter to another one)


With these four edits, we are proficient in modifying any string. So the combination of edits allows us to find a list of all possible strings that are n edits to perform.

IMPORTANT Note: For autocorrect, we take n  usually between 1 to 3 edits.

3. Filtering of Candidates — Here we want to consider only correctly spelled real words from our generated candidate list so we can compare the words to a known dictionary (like we did in the first step) and then filter out the words in our generated candidate list that do not appear in the known “dictionary”.

4. Calculate Probabilities of Words — We can calculate the probabilities of words and then find the most likely word from our generated candidates with our list of actual words. This requires word frequencies that we know and the total number of words in the corpus (also known as dictionary).



**Build an Autocorrect Text using NLP with Python**

I hope you are now clear about what autocorrect is and how it works. Now let us see how we can build an autocorrect feature with Python for smartphones. As our smartphone uses past history to match the typed words whether it is correct or not. So here we are required to use some words to run the functionality in our Autocorrect.

So I am going to use the text from a **poetry Farsi** and **wikipedia farsi** and... to understand it practically which you can easily download from here. Now let’s get started with the task to build an autocorrect model with Python.

Note: You can use any kind of text data.

Email to access datasets : [![Email Badge](https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:yaronhuang@foxmail.com)](mailto:parvvaresh@gmail.com)

To run this task, we are required some libraries. I am going to use libraries that are very general for machine learning. So you should be having all these libraries already installed in your system except one library. You need to install one library known as “text distance”, which can be easily installed by using the pip command.
