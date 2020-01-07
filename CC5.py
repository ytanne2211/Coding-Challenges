#Highest Common Factor

def findHCF(num, array):
    
    mintemp = 10000
    size = len(array)
    maxtemp =0


    if (num == 0):
        maxtemp =0 
        
    if (num == 1):
        for i in (0, size):
            if (array[i] > 0):
                maxtemp = array[i]
            
    if (num > 1 ):
        for j in range(0,len(array)):
            
            if (array[j]< mintemp and array[j]>1):
                mintemp = array[j]
                
        for i in range(0, size):
            if (array[i]>1):
                length = (array[i])
                for j in range(1,mintemp+1):
                    if (length % j ==0):
                        maxtemp =j
                        
                        
                        
        
            
        
    
    return maxtemp


def main():
    a= [3, -1, 1, 3, 21]
    num = 4
    print(len(a))
    print (findHCF(num,a))
    
    
main()
