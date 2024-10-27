import random
import string

m=input("Enter message: ")
lst=m.split()

def encode():
    en=" "
    for s in lst:
        if len(s)<=2:
            en=en+s[::-1]+" "
        
        else:
            a=s[0]
            str1="".join(random.choices(string.ascii_letters, k=3))
            str1=str1+s[1:]+a
            str2="".join(random.choices(string.ascii_letters, k=3))
            en=en+str1+str2+" "
            
    print(en)


def decode():
    de=" "
    for s in lst:
        if len(s)<=2:
            de=de+s[::-1]+" "
        
        else:
            str3=s[3:-3]
            str4=str3[-1] + str3[:-1]
            de=de+str4+" "
    
    print(de)
    
x=int(input("""                           WEATHER YOU WANT TO ENCODE OR DECODE A MESSAGE:
        
                                                    PRESS 1 TO ENCODE
                                                    PRESS 2 FOR DECODE\n
                                                    """))

if x==1:
    encode()
elif x==2:
    decode()
else:
    print("Wrong Input...")
       
            
            
            




