import math
from datetime import datetime

from opposition_calculator import Oppositions
import common_variables
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
mars = distance_from_sun(1.52371, 0.09339, 0.5240, mars_day_nr, 0)
mars.kepler_law()

mars_synodic_period = Oppositions(datetime(2022,12,7), 780)
mars_synodic_period.oppositions()

#planet_distance_from_sun:

sun_mars = mars.distance_km
sun_earth = earth.distance_km

class Distance_from_Earth:

    def __init__(self,planet, sun_earth, sun_planet, planet_day, planet_ang_velocity):

        self.planet = planet
        self.sun_earth = sun_earth
        self.sun_planet = sun_planet
        self.planet_day = planet_day
        self.planet_ang_velocity = planet_ang_velocity

    def earth_distance(self):

        earth_ang_velocity = 0.9856
        #angles beta (Earth), delta (planet), alpha (Earth-planet), see drawing
        beta = earth_ang_velocity * self.planet_day
        delta = self.planet_ang_velocity * self.planet_day
        alpha = beta - delta
        

        self.earth_planet = int(math.sqrt(math.pow(self.sun_earth * math.sin(alpha),2) + math.pow(self.sun_planet - (self.sun_earth * math.cos(alpha)),2)))

    def __repr__(self):

        return "this is day nr {} on {}. It is {} km away from Earth today".format(self.planet_day, self.planet, f"{self.earth_planet:,}")

#objects:

mars_distance = Distance_from_Earth(str("Mars"), sun_earth, sun_mars, mars_day_nr, 0.5313)
mars_distance.earth_distance()

#forks

if planet == str("venus"):
    print(venus)
if planet == str("earth"):
    print(earth)
if planet == str("mars"):
    print(mars)
    print(mars_synodic_period)
    print(mars_distance)
