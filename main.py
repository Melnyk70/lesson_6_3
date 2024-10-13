#ДЗ ДЗ 6.3. Добуток чисел
#Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
#поки воно не стане менше або дорівнювати 9.
#Користувач вводить число з клавіатури.
#999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
#1000 -> 0
#423 -> 8
#33 -> 9
#25 -> 0
#1 -> 1
var=423
rez=1
i=0
lst=str(var)
print(var,"=> ", end="")
while i < len(lst):
   rez=int(lst[i])*rez
   i=i+1
#    print("while",rez)
lst=str(rez)
i=0
rez1=1
if rez>9:
   while i < len(lst):
       rez1=int(lst[i])*rez1
       i=i+1
#        print("1if",rez1)
lst=str(rez1)
i=0
rez2=1
if rez1>9:
   while i < len(lst):
       rez2=int(lst[i])*rez2
       i=i+1
#        print("2if",rez2)
lst=str(rez2)
i=0
rez3=1
if rez2>9:
   while i < len(lst):
       rez3=int(lst[i])*rez3
       i=i+1
#        print("3if",rez3)
if rez<=9:
   print(rez)
elif rez1<=9:
   print(rez1)
elif rez2<=9:
   print(rez2)
elif rez3<=9:
   print(rez3)