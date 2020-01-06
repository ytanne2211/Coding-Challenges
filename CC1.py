#Run-length encoding is a fast and simple method of encoding strings.
#The basic idea is to represent repeated successive characters as a single count and character.
#For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
#You can assume the string to be decoded is valid.

def encodeDecode(string):
    if string[0].isdigit() :
        decode(string)
    else:
        encode(string)

def encode(string):

    encoded = ""
    i = 0 # i starts with the first element
    while i < len(string): #while i does not go over the length of the string
        letter = string[i]
        count = 0 # initial count for first letter
        j = i
        while string[j]== letter:
            count = count+1
            j = j+1
            if j >= len(string):
                break
        encoded = encoded + str(count)+ str(string[i])
        i = i + count  
        
    print(encoded)
    

def decode(string):
    decoded = ""
    for i in range (0,len(string),2):
        number= eval(string[i])
        
        for j in range (0,number):
            decoded = decoded + string[i+1]
        
    print(decoded)
    
def main():
    encodeDecode("AAAABBBCCDAA")
    encodeDecode("4A3B2C1D2A")

main()
