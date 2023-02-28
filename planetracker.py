import math
from datetime import datetime

planet = str(input("planet: "))
selected_date = str(input("date: day/month/year: "))
datetime_date = datetime.strptime(selected_date, "%d/%m/%Y")

#day number in the year

day_number = datetime_date.timetuple().tm_yday


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
        return "The {}/{}/{}, the {} will be at: {} km from the Sun.".format(datetime_date.day, datetime_date.month, datetime_date.year, planet, self.distance_km)

earth = distance_from_sun(1, 0.01672, 0.9856, day_number, 4)
earth.kepler_law()
print(earth)
