#Using a function rand5() that returns an integer from 1 to 5 (inclusive)
#with uniform probability,
#implement a function rand7() that returns an integer from 1 to 7 (inclusive).
#not done accurately may cause some random zeroes

import time

def rand5():
    seconds = time.time()
    seconds2 = int(time.time())
    random = seconds-seconds2
    random4 = int(random * 10)+1

    if (random4>5):
        random4 = int((random4/10) * 5) 
    return(random4)

def rand7():
    random7 = int((rand5()/5)*7)
    print(random7)

def main():
    print(rand5())

main()
