
import time

def pow(x,n):
    half=n//2
    if n==1 :
        return x
    
    
    return pow(x,half) * pow(x,half) 


timer1=time.time()
print(pow(2,1000000))
timer2=time.time()
print("Time:", timer2-timer1)
print(4/2)
print(7//2)


at all i like green apples

