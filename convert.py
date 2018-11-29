'''
convert from f to c, and from c to f
'''
degree = input("enter c for celsius, o f for fahreinheit :")
temperature = int(input("enter the temperature value: "))

if degree == 'f':
    c = (temperature - 32)*5/9
    print("the temperature in celsuis is ",round(c))
elif degree == 'c':
    f = temperature*9/5 + 32
    print("the temperature in fahreinheit is : ",round(f))
else :
    print("there is no such type of degree like:",degree)

exit()