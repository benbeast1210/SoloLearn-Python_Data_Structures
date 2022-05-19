# SoloLearn-Python_Data_Structures

The projects in this repo were completed towards earning the Python Data Structures certificate from SoloLearn.

From SoloLearn: 
>Almost no program can work properly without data. Python has a number of built-in data structures, which allow you to store, organize, and manage your data. In this course, we will learn about different Python Data Structures such as strings, lists, dictionaries, tuples, sets, and much more.

---

## Project #1: Letter Frequency

From SoloLearn:
>You are making a program to analyze text.
>Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.
>
>Sample Input:
>hello
>l
>
>Sample Output:
>40
>
>Explanation : The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
>Division result is a float. Use the int() function to convert the result to an integer.

---

## Project #2: Average Word Length

From SoloLearn:
>Given a sentence as input, calculate and output the average word length of that sentence.
>To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.
>
>Sample Input:
>this is some text
>
>Sample Output:
>3.5
>
>Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5
>Strings have a split() method, which returns the string split into a list, with the given separator. By default, the separator is a space, so calling split() will return a list containing the words of the string as items.

---

## Project #3: Revenue Growth Analysis

From SoloLearn:
>You are analyzing sales data from a ticket office.
>The ticket for an adult is $20, while the ticket for a child under 18 is $5.
>The data you are given is in a dictionary format, where the keys are the sold ticket numbers, and the values are the customer ages.
>
>For example, "123-08": 24 means that the ticket was bought a 24 year old.
>Your goal is to calculate how much more money the office would make if it would change the ticket discount age to the given input.
>So, your program needs to take an integer as input and output the percentage of revenue growth, if the discount was given to people under that age.
>
>For example, if the office made $15000 with the original discount age, and would make $18000 with 14 as the discount age, then the growth would be ((18000-15000)/15000)>*100 = 20%
>
>So, for the input 14, your program should output 20. The output should be an integer (use int() to convert the result).
>
>To iterate over the values of a dictionary, you can use the .values() function:
>for value in data.values()

---

## Project #4: Balanced Parentheses

From SoloLearn:
>Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.
>
>Given an expression as input, we need to find out whether the parentheses are balanced or not.
>For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.
>
>The problem can be solved using a stack.
>Push each opening parenthesis to the stack and pop the last inserted opening parenthesis whenever a closing parenthesis is encountered.
>If the closing bracket does not correspond to the opening bracket, then stop and say that the brackets are not balanced.
>Also, after checking all the parentheses, we need to check the stack to be empty -- if it's not empty, then the parentheses are not balanced.
>
>Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not.
>
>Sample Input:
>(a( ) eee) )
>
>Sample Output:
>False
>You can use a simple list for a stack. Use list.insert(0, item) to push on the stack, and list.pop(0) to pop the top item. You can access the top element of the stack using list[0].
