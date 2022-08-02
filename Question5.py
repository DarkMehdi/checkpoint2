x=int(input())
s=1
if x==0 :
    print("Factoriel est égale à 1 ")
elif x>0 :    
    for i in range(x) :
        s=s+s*i
    print("Factoriel est égale à ",s)
else :
    print("ce nombre est négative , il faut répéter ")
    
