# Date Validator (DD/MM/YYYY).

def is_leep(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(day, month, year):
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leep(year):
        days[1] = 29
        
    if month < 1 or month > 12:
        return False
    
    if day < 1 or day > days[month - 1]:
        return False
    
    return True

d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

print(valid_date(d, m, y))



   

   

   
   
   
   
   
   