# Operators
#== 
# !=
# <
# > 
# if
#  
# ex 1
print("############# EX 1 #############")
color = input("Enter a color: ")
name = 'Juan Intriago'
age = 55
adult_age = 18
continent = 'Europe'
city = 'Madrid'
if age >= adult_age:
    print(f"{name} was adult ✅")
    if( continent == 'Europe'):
        print(f"was European and was from {city}")
    else:
        print("was not European")
else:
    print(" was a child ❌")

