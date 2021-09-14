a = 1622570583

m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m_b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 60 * 60 * 24
days_calc = a // days
full_years = days_calc // 365
v_d = full_years // 4 + 1
full_days_to_years = full_years * 365 + v_d
current_year = 1970 + full_years

rest_year = a - full_days_to_years * days
rest_days = rest_year // (60 * 60 * 24)

print(current_year)
c = rest_days
if (current_year % 100) % 4 == 0:
    for i in range(0,len(m_b)):
        temp = c - m_b[i]
        if temp < 0:
            print(i, c)
            break
        else:
            c -= m_b[i]
else:
    for i in range(0,len(m)):
        temp = c - m[i]
        if temp < 0:
            print(i + 1, c)
            break
        else:
            c -= m[i]
rest_day = rest_year - (rest_days * 60 * 60 * 24)

hours = rest_day // 3600
minutes = (rest_day - (hours * 3600)) // 60
seconds = rest_day - (hours * 3600) - (minutes * 60)
print(hours, minutes, seconds)
