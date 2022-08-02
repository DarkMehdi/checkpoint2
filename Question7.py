print("Give your price: ")
x=int(input())
if x<0 : 
    print("error")
else :
    if x<200 :
        p=x-x/10
    if (x>=200) and (x<500) :
        p=x-x*0.3
    if x>=500 :
        p=x/2
print(p)        