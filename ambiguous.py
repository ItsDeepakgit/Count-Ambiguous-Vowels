import string
str=input("Please enter a string as you wish: ");
ambiguous_count = 0
a = e = i = o = u = 0
for k in str:
    if(k=='a'):
        a = a+1;
    elif(k=='e'):
        e = e+1;
    elif(k=='i'):
        i = i+1;
    elif(k=='o'):
        o = o+1;
    elif(k=='u'):
        u = u+1;
print("a:",a)
print("e:",e)
print("i:",i)
print("o:",o)
print("u:",u)
if(a>0):
    ambiguous_count += 1
if(e>0):
    ambiguous_count += 1
if(i>0):
    ambiguous_count += 1
if(o>0):
    ambiguous_count += 1
if(u>0):
    ambiguous_count += 1
print("Ambiguous count of vowels is: ", ambiguous_count)   
    



