import math
from datetime import datetime

planet = str(input("planet: "))
day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))


#day in the year

input_date = datetime(year, month, day)
day_number = input_date.timetuple().tm_yday


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

        distance_UA = float(self.a - self.e * math.cos(self.n * (self.t - self.t0)))
        self.distance_km = int(distance_UA * 149597870)
    
    def __repr__(self):
        return "The {}/{}/{}, the {} will be at: {} km from the Sun.".format(day, month, year, planet, self.distance_km)

earth = distance_from_sun(1, 0.01672, 0.9856, 4, day)
earth.kepler_law()
print(earth)
