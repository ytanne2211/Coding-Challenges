#Given a string of round, curly, and square open and closing brackets,
#return whether the brackets are balanced (well-formed).
#For example, given the string "([])[]({})", you should return true.
#Given the string "([)]" or "([)]", you should return false.


#What about (([])), if we use this solution it becomes false
#but the brackets are balanced,how do we tackle this?

def isItBalanced(string):
    balanced = True
    for i in range (0,len(string)):
        letter = string[i]
        for j in range (i,len(string)):
            if letter == '(':
                if string[j] == ')' :
                    if (j-i)%2 == 0  :
                        balanced = False
                    break            
            if letter == '[':
                if string[j] == ']' :
                    if (j-i)%2 == 0 :
                        balanced = False
                    break           
            if letter == '{':
                if string[j] == '}' :
                    if (j-i)%2 == 0 :
                        balanced = False
                    break
            
    return balanced

def main():
    print(isItBalanced("([])[]({})"))
    print(isItBalanced("([)]"))
    print(isItBalanced("([)]"))
    

main()
