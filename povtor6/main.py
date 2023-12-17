a=int(input("Введіть Ваш вік: "))
if a<12:
    print("дитина")
elif a>=12 and a<=17:
    print("підліток")
elif a>=18 and a<=65:
    print("дорослий")
elif a>=66:
    print("пенсіонер")
