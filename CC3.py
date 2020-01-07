def reverseWord(string):

    array = []
    for j in range (len(string)-1,-1,-1):
        array.append(string[j])

    newString = ""
    for i in range (0,len(string)):
        newString= newString + array[i]

    print(newString)
    
def main():
    reverseWord("alibaba")

main()
