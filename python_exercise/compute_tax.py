
year_salary = int(input("請輸入年所得: "))
print(year_salary)

if year_salary <= 540000:
    tax = round(year_salary*0.05)
elif year_salary >= 540001 and year_salary  < 1210000:
    tax = round(year_salary*0.12)
elif year_salary > 1210001 and year_salary < 2420000:
    tax = round(year_salary*0.20)
elif year_salary > 2420001 and year_salary < 4530000:
    tax = round(year_salary*0.30)
elif year_salary > 4530001 and year_salary < 10310000:
    tax = round(year_salary*0.40)
# elif year_salary > 10310001:
#     tax = round(year_salary*0.45)
else:
    tax = round(year_salary*0.45)

print("需繳納稅額: ", tax)
