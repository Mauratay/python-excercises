def is_year_leap(year):
    if str(year)[-2:] == "00":
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False



def days_in_month(year, month):
    month_with_31 = [1,3,5,7,10,12]
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in month_with_31:
        return 31
    else:
        return 30


def day_of_year(year, month, day):
    def valid_val(val):
        if val > 0:
            return val
    if valid_val(year):
        if valid_val(month):
            if valid_val(day):
                if is_year_leap(year):
                    if month == 2 and day > 29:
                        return None
                    else:
                        return day
                elif day > days_in_month(year,month):
                    return None
                else:
                    return day
    
print(day_of_year(2000, 12, 31))
