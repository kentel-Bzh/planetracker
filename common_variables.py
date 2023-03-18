from datetime import datetime

#initial variables:
selected_date = str(input("date: day/month/year: "))
datetime_date = datetime.strptime(selected_date, "%d/%m/%Y")

#day number in the year and year date
day_number = datetime_date.timetuple().tm_yday
year_number = datetime_date.timetuple().tm_year