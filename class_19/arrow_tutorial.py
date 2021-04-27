import arrow

data = arrow.get('9/9/2014', 'M/D/YYYY')
print(data)

data_1 = arrow.get('July-2017', 'MMMM-YYYY')
print(data_1)

# 5th May 2017 
data_2 = arrow.get('5th May 2017', 'Do MMMM YYYY')
print(data_2)
# 14/8/2020
data_3 = arrow.get('14/8/2020', 'DD/M/YYYY')
print(data_3)
# 15;5;2020
def convert_date(date_):
    new_date = arrow.get(date_, 'M/D/YYYY')
    return new_date


print(data_4.date().day)
print(data_4.date().month)
print(data_4.date().year)

print(data_4 - data_3)