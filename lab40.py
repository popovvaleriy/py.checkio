import datetime

def time_converter(date_d):
    # '1998y11d-12m'  ->  "Dec 11th 1998"

    format = '%Yy%dd-%mm'
    date_formatted = datetime.datetime.strptime(date_d, format)
    print(date_formatted.strftime("%b %dth %Y"))
   

time_converter('1998y11d-12m')
