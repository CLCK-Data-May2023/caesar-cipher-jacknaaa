# Caesar Cipher Exercise
Code Louisville Python programming exercise.

## Overview

> In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift 
cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely 
known encryption techniques. It is a type of substitution cipher in which each 
letter in the plaintext is replaced by a letter some fixed number of positions 
down the alphabet. For example, with a left shift of 3, D would be replaced by 
A, E would become B, and so on. The method is named after Julius Caesar, who 
used it in his private correspondence.

From: [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) on wikipedia.org

In this exercise we will implement a Caesar cipher with a right shift of 5. This 
exercise is based on the Caesar cipher exersise in the openSAP Python for 
Beginners course. If you have already solved it as part of the Learn Python 
course you can re-use your code here.

Write a Python program that encrypts text given by the user. The program should 
ask the user for a plain text sentence and print the encrypted text. The text 
should be encrypted using a caesar cipher with a right shift of 5.

Here is an example execution of the program:

```
Please enter a senctence: python is fun!
The encrypted sentence is: udymts nx kzs!
```

Note that the program should not replace special characters like spaces or exclamation marks.

## Instructions

1. GitHub Classroom will send you an email asking you to accept the assignment.
1. Once you've accepted, it will create a repo for you to add your code.
1. Clone your repo, add your code, and Commit/Push your changes to Github.
1. Mentors will review your submissions and provide feedback.

### Optional: Automated Code Testing

This repo contains a small testing program that is automatically run by GitHub
to validate your code. This testing program is contained in the tests.py 
file. You don't have to do anything with this file to complete the exercise, 
but you can follow these steps if you would like to run the tests on your 
machine.

1. Open GitBash in Windows or the Terminal in Mac and navigate to the project 
folder.
1. Install the `pytest` packages. This program uses a python package called 
pytest. We'll be covering packages later in the course, so for now you can 
just run the following command  without getting into the details of how it
works: `pip install pytest`.
1. Run the tests. We won't be covering testing with python in this course. Use 
the following command to run the tests: `pytest tests.py`. You can read more 
about it [here](https://realpython.com/python-testing/).
1. Review the output from running the test. This will let you know whether your
code produces the expected results. 



