#Assign a message to a variable, and then print that message.
#TASK 1
print("""   
task N1""")
task1="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam gravida gravida nisl vel convallis."
print(task1)

#Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
#TASK 2
print("""   
task N2""")
task2="old message"
print(task2)
task2="new message"
print(task2)

#Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case
#TASK 3
print("""   
task N3""")
task3="mariam abzianidze"
task3=task3.lower()
print(task3)
task3=task3.upper()
print(task3)
task3=task3.title()
print(task3)

#Print list of your favourite foods with tab indentation.
#TASK 7
print("""   
task N7""")
task7= '''My favorite food:
Khinkali
Burger
Pizza'''
print(task7)

#Remove whitespaces from folowing string.
#TASK 8
print("""   
task N8""")
task8='          I have white spaces                '
print(f'"{task8}"')
print(f'"{task8.strip()}"')

"""TASK 9
Remove only left white spaces in string from 8th Exercise"""
print("""   
task N9""")
print(f'"{task8.lstrip()}"')

"""TASK 10
Remove only right white spaces in string from 8th Exercise"""
print("""   
task N10""")
print(f'"{task8.rstrip()}"')

"""TASK 11
Create string with single quotes (') and include at least one additional single quote in it."""
print("""   
task N11""")
task11='''One of Python's strengths is its diverse community.'''
print(task11)
print(f'{task11}add new text in it.')

"""TASK 12
use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”"""
print("""   
task N12""")
task12="Mariam"
print(f'Hello {task12}, would you like to learn some Python today?')

"""TASK 13
Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:"""
print("""   
task N13""")
print(f'Franklin D.Roosevelt once said, "The only thing we have to fear is fear itself."')

"""TASK 14
Repeat Exercise 13, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message"""
print("""   
task N14""")
famous_person="Franklin D.Roosevelt"
print(f'{famous_person} once said, "The only thing we have to fear is fear itself."')

"""TASK 15
Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. Your output should simply be four lines with the number 8 appearing once on each line."""
print("""   
task N15""")
print(5+3)
print(10-2)
print(4*2)
print(24//3)

"""TASK 16
#Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message."""
print("""   
task N16""")
task16=24
print(task16)
print(f'My favorite number is {task16}.')