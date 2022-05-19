# Key Libraries 
import json

# Project #1: Letter Frequency
word_input = input()
letter_input = input()

def letter_freq(word, letter):
  per = (((word.count(letter)) / (len(word))) * 100)

  print(int(per))

letter_freq(word_input, letter_input)

# Project #2: Average Word Length
def word_length():
  text = input()
  
  z = text.split()
  y = len(z)
  x = 0
  
  for i in z:
    x += len(i)
  
  print(x / y)

word_length()

# Project #3: Revenue Growth Analysis
with open('/docs/data.json') as data:
  data = json.loads(data)

def revenue_growth(data):
  age = int(input())
  list = list(data.values())

  def revenue(age):
    sal = 0

    for i in list:
      if i < age:
        sal = sal + 5
      else:
        sal = sal + 20
    return sal
  
  curr_revenue = revenue(18)
  pred_revenue = revenue(age)
  growth = int((pred_revenue - curr_revenue ) * 100 / curr_revenue)
  
  print(growth)

revenue_growth(data)

# Project #4: Balanced Parentheses
class Stack:
	def __init__(self):
		self.items = []  
  
	def is_empty(self):
		return self.items == []
  
	def push(self, item):
		self.items.insert(0, item)
	
	def pop(self):
		return self.items.pop(0)
	
	def stack(self):
		return self.items

def balanced(expression):
	s = Stack()
	for i in expression:
		if i == '(':
			s.push(i)
		if i == ')':
			if '(' in s.stack():
				s.pop()
			else:
				return False

	if not s.stack():
		return True
	else:
		return False
		
print(balanced(input()))
