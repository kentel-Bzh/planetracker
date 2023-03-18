import math
from datetime import datetime

from opposition_calculator import Oppositions
from common_variables import datetime_date, day_number
from planet_day_converter import planet_day_calculator


planet = str(input("planet: "))

class distance_from_sun:

    #orbits of the planets
    #a = semi-major axis
    #e = excentricity
    #n = angular velocity
    #t = day
    #t0 = apsis day

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
        return "The {}/{}/{}, {} will be at: {} km from the Sun.".format(datetime_date.day, datetime_date.month, datetime_date.year, planet, f"{self.distance_km:,}")


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

mars_synodic_period = Oppositions(datetime(2022,12,7), 780)
mars_synodic_period.oppositions()

#forks

if planet == str("venus"):
    print(venus)
if planet == str("earth"):
    print(earth)
if planet == str("mars"):
    print(mars)
    print(mars_synodic_period)