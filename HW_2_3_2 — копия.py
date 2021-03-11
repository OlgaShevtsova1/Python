# Задача 3 list
Year=["ЗИМА", "ВЕСНА","ЛЕТО", "ОСЕНЬ","ЗИМА"]
Mounth=int(input ("Введите месяц, от 1 до 12: "))
if (Mounth==1) or (Mounth==2) or (Mounth==12):
    print("Время года- ",Year [0])
elif (Mounth==3) or (Mounth==4) or (Mounth==5):
    print("Время года-", Year [1])
elif (Mounth==6) or (Mounth==7) or (Mounth==8):
    print("Время года-", Year [2])
elif (Mounth==9) or (Mounth==10) or (Mounth==11):
    print("Время года-", Year [3])


