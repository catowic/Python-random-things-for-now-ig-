# pounds(lbs) kilos(kg)
total = 0
while True:
    weighttype = int(input("select the type (1 for KG , 2 for lbs) : "))
    match weighttype:
        case 1 :
            weight = float(input("How much kg/lbs : "))
            total = weight / 0.45359237
            print(f"your weight is {total}")
            break
        case 2 :
            weight = float(input("How much kg/lbs : "))
            total = weight * 0.45359237
            print(f"your weight is {total}")
            break
        case _ :
            print("invalid")