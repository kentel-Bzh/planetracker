import math
from datetime import datetime

planet = str(input("planet: "))
selected_date = str(input("date: day/month/year: "))
datetime_date = datetime.strptime(selected_date, "%d/%m/%Y")

#day number in the year and year date

day_number = datetime_date.timetuple().tm_yday
year_number = datetime_date.timetuple().tm_year

class planet_day_calculator:

    #calculate planet date equivalent (day number in the planet year) to earth date given in input
    #day_shift = number of days between the last perihelion and the 01/01/2023

    def __init__(self, day_shift, days_in_year):
        self.day_shift = day_shift
        self.days_in_year = days_in_year

    def day_calculator(self):
        
        #years after the last (before 2023) perihelion of the planet
        years_after_last_perihelion = year_number - 2023

        #total days since the last perihelion
        self.days_after_last_perihelion = day_number + self.day_shift + (365 * years_after_last_perihelion)

        #day nr in planet year
        self.planet_day_nr = self.days_after_last_perihelion % self.days_in_year

            

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

#objects

venus_day = planet_day_calculator(118, 225)
venus_day.day_calculator()
venus_day_nr = venus_day.planet_day_nr
mars_day = planet_day_calculator(224, 687)
mars_day.day_calculator()
mars_day_nr = mars_day.planet_day_nr


venus = distance_from_sun(0.71843, 0.00678, 1.6251, venus_day_nr, 0)
venus.kepler_law()
earth = distance_from_sun(1, 0.01672, 0.9856, day_number, 4)
earth.kepler_law()
mars = distance_from_sun(1.52371, 0.09339, 0.5313, mars_day_nr, 0)
mars.kepler_law()

#forks

if planet == str("venus"):
    print(venus)
if planet == str("earth"):
    print(earth)
if planet == str("mars"):
    print(mars)