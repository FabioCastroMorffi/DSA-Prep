from stack.Stack_ADT import Stack

'''Example 1: Overwrite a given file with its contents line-by-line \
    reversed using a stack. '''

with open('Reversed.txt', 'r') as input_file:
    stack = Stack()
    for line in input_file:
        if line != '\n':
            stack.push(line)
with open('Reversed.txt', 'w') as output_file:
    while not(stack.isEmpty()):
        output_file.write(stack.pop())

'''Example 2: 
Using a stack check if a given arithmetic expression has matching parenthese.  \
You may assume the expression only has: 
--> ( and )
--> { and }
--> [ and ]'''

def checkExpression(s:str)-> bool:
    stack = Stack()
    d = {')': '(', ']': '[', '}': '{'}
    for par in s:
        if par not in d:
            stack.push(par)
        else:
            if not stack.isEmpty() and d[par] != stack.pop():
                return False
    return True

#print(checkExpression('][((([]))]'))


'''Example 3:
Use a stack to match tags in a markup language such as html.  \
Check if a given html file has matching tags.  \
A simple opening html tag has the form <name> and the corresponding closing tag has the form </name>.\
Commonly used html tags are:
--> body: document body
--> h1: section header
--> center: center justify
--> p: paragraph
--> li: list item'''

def checkHTML(name):
    with open(name, 'r') as input_file:
        for line in input_file:
            lst_line = line.split()
            for word in lst_line:
                if word[0] == '<' and word[1] != '/':
                    stack.push(word)
                elif word[0] == '<' and word[1] == '/':
                    if stack.pop() != word[:1] + word[2:]:
                        return False
        return True            

print(checkHTML('Match_HTML.html'))              




    
        
        




