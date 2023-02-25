import math

planet = str(input("planet: "))
day = int(input("day: "))
month = str(input("month: "))
year = int(input("year: "))

#planet selection

#day in the year

if month == "01": 
    day = day
if month == "02":
    day = day + 31
if month == "03": 
    day = day + 59
if month == "04":
    day = day + 100 
if month == "05":
    day = day + 130
if month == "06":
    day = day + 161
if month == "07":
    day = day + 191
if month == "08":
    day = day + 222
if month == "09":
    day = day + 253
if month == "10":
    day = day + 283
if month == "11":
    day = day + 314
if month == "12":
    day = day + 344


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
        distance_km = int(distance_UA * 149597870)
    
    def __repr__(self):
        return "The {}/{}/{}, the {} will be at: {} km from the Sun.".format(day, month, year, planet, distance_km)

earth = distance_from_sun(1, 0.01672, 0.9856, 4, day)
earth.kepler_law()
