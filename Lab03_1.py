primeCount = 0
number =2
n=50
while primeCount < n:
    divisorCount=0
    for i in range (1,number+1):
        if number%i == 0:
            divisorCount+=1
        
    if divisorCount== 2:
        print number,   
        primeCount+=1
            
        if primeCount%10==0:
            print 
    number+=1
