# celcius(C) fahrenite(F) kelvin(K)
value = 0.0
while True:
    temptype = int(input("what is your temp type (1/C , 2/F , 3/K): "))
    tempchangeto = int(input("which type you wanna change (1/C , 2/F , 3/K): "))
    value = float(input("how much it your temp 4 to exit): "))
    if value == 4:
        break
    else:
        match temptype,tempchangeto:
            case 1,2:
                total = value*1.8 + 32
                print(f"your temp is {total} F")
            case 1,3:
                total = value + 273
                print(f"your temp is {total} K")
            case 2,1:
                total = (value - 32)*(5/9) 
                print(f"your temp is {total} C")
            case 2,3:
                total = (value - 32)*(5/9) + 273
                print(f"your temp is {total} K")
            case 3,1:
                total = value - 273
                print(f"your temp is {total} C")
            case 3,2:
                total = (value - 273)*(9/5) + 32
                print(f"your temp is {total} F")
            case _ if temptype == tempchangeto:
                print("canntot be same")
            case _:
                print("invalid")
        print(" ")