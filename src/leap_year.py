def is_leap_year()-> bool:
    Año: int = int(input("Ingrese un año: "))

    if (Año % 400 == 0) or (Año % 4 == 0 and Año % 100 != 0):
        print(f"El año {Año} es bisiesto")
        return True
    else:
        print(f"El año {Año} no es bisiesto")
        return False
