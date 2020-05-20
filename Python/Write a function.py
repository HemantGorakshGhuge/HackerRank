def is_leap(year):
    leap = False
    
    # Write your logic here
    #The year can be evenly divided by 4, is a leap year, unless:
    #The year can be evenly divided by 100, it is NOT a leap year, unless:
    #The year is also evenly divisible by 400. Then it is a leap year.
    if not(year%4):
        leap=True
        if not(year%100):
            leap=False
            if not(year%400):
                leap=True

    return leap

