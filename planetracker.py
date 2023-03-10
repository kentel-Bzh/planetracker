import math
from datetime import datetime

planet = str(input("planet: "))
selected_date = str(input("date: day/month/year: "))
datetime_date = datetime.strptime(selected_date, "%d/%m/%Y")

#day number in the year

day_number = datetime_date.timetuple().tm_yday
year_number = datetime_date.timetuple().tm_year


#orbits of the planets
#a = semi-major axis
#e = excentricity
#n = angular velocity
#t = day
#t0 = apsis day

class distance_from_sun:

    def __init__(self,a,e,n,t,t0):
        self.a = a
        self.e = e
        self.n = n
        self.t = t
        self.t0 = t0
    
    def kepler_law(self):

        distance_UA = float(self.a *(1 - self.e**2) / (1 + self.e * math.cos(self.n * (self.t - self.t0))))
        self.distance_km = int(distance_UA * 149597870)
    
    def __repr__(self):
        return "The {}/{}/{}, {} will be at: {} km from the Sun.".format(datetime_date.day, datetime_date.month, datetime_date.year, planet, self.distance_km)

#calendars

def martian_day_calculator(earth_date):

    #day number in the year
    earth_day = day_number

    #periapsis on 21/06/2022, i.e. 224 days before the beginning of 2023
    #martian year = 686,9 days; see README for further data
    #mars_year = equivalent Earth's years calculated from the 21/06/2022

    mars_year = year_number - 2023

    #number of Mars days after 21/06/2022 periapsis

    absolute_mars_day = earth_day + 224 + (365 * mars_year)

    #number of days in the martian year after periapsis

    mars_day_nr = absolute_mars_day % 687

    return mars_day_nr

mars_day = martian_day_calculator(selected_date)


#planet objects

earth = distance_from_sun(1, 0.01672, 0.9856, day_number, 4)
mars = distance_from_sun(1.52371, 0.09339, 0.5313, mars_day, 0)

if planet == str("earth"):
    earth.kepler_law()
    print(earth)

if planet == str("mars"):
    mars.kepler_law()
    print(mars)