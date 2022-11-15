from itertools import repeat
import unittest
plus = 1
hold = ""
out = ""



def obratit(vstup):
   out = ""
   
   for i in range(len(vstup)):

      out = out + vstup[len(vstup)-i-1]    

   return out  

x = input("zadejte číslo co chcete převést do bin soustavy ")
 


loop = int(x)

#print("x je ",loop)
while loop > 0 :
    hold = loop % 2
    out = out + str(hold)
    #print(hold)

    #print("smička jede ",plus)
    plus = plus + 1
    
    loop = loop//2
    #print("x//2 je ",loop)
    
#print("smyčka ukončena")
print("číslo v bin. je",obratit(out))


    