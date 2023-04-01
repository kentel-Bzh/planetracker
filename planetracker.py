import math
import json
from datetime import datetime

from opposition_calculator import Oppositions
from common_variables import datetime_date, day_number
from planet_day_converter import planet_day_calculator


planet = str(input("planet (Mercury, Venus, Earth, Mars, Ceres, Vesta, Pallas): "))

class distance_from_sun:

    #orbits of the planets
    #a = semi-major axis
    #e = excentricity
    #n = angular velocity
    #t = day
    #t0 = apsis day
    #M = mean anomaly in degrees
    #M_rad = mean anomaly in radians

    def __init__(self,a,e,n,t,t0):
        self.a = a
        self.e = e
        self.n = n
        self.t = t
        self.t0 = t0
    
    def kepler_law(self):

        self.M = self.n *(self.t - self.t0)
        M_rad = self.M * (math.pi / 180)

        distance_UA = float(self.a *(1 - self.e**2) / (1 + self.e * math.cos(M_rad)))
        self.distance_km = int(distance_UA * 149597870)
    
    def __repr__(self):
         return "The {}/{}/{}, {} will be at: {} km from the Sun.\nThis is day nr {} on {}\nmean anomaly = {} degrees".format(datetime_date.day, datetime_date.month, datetime_date.year, planet, f"{self.distance_km:,},", self.t, planet, self.M)


#objects instanciations

mercury_day = planet_day_calculator(86, 88)
mercury_day.day_calculator()
mercury_day_nr = mercury_day.planet_day_nr

venus_day = planet_day_calculator(118, 225)
venus_day.day_calculator()
venus_day_nr = venus_day.planet_day_nr

mars_day = planet_day_calculator(193, 687)
mars_day.day_calculator()
mars_day_nr = mars_day.planet_day_nr

ceres_day = planet_day_calculator(21, 1680)
ceres_day.day_calculator()
ceres_day_nr = ceres_day.planet_day_nr

pallas_day = planet_day_calculator(1608, 1686)
pallas_day.day_calculator()
pallas_day_nr = pallas_day.planet_day_nr

vesta_day = planet_day_calculator(370, 1326)
vesta_day.day_calculator()
vesta_day_nr = vesta_day.planet_day_nr


mercury = distance_from_sun(0.387098, 0.2056, 4.1539, mercury_day_nr, 0)
mercury.kepler_law()

venus = distance_from_sun(0.723336, 0.00678, 1.6251, venus_day_nr, 0)
venus.kepler_law()

earth = distance_from_sun(1, 0.01672, 0.9856, day_number, 4)
earth.kepler_law()

mars = distance_from_sun(1.52371, 0.09339, 0.5240, mars_day_nr, 0)
mars.kepler_law()

ceres = distance_from_sun(2.768134, 0.0757051, 0.214004, ceres_day_nr, 0)
ceres.kepler_law()

pallas = distance_from_sun(2.7724, 0.231, 0.21353, pallas_day_nr, 0)
pallas.kepler_law()

vesta = distance_from_sun(2.36179, 0.089366, 0.2752, vesta_day_nr, 0)
vesta.kepler_law()

mars_synodic_period = Oppositions(datetime(2022,12,7), 780)
mars_synodic_period.oppositions()

#planet_distance_from_sun:

sun_mars = mars.distance_km
sun_earth = earth.distance_km
sun_ceres = ceres.distance_km

#not sure json or cvc could help clearing the ground here, but could try...
with open("planet_data.json") as data:
    data = json.load(data)
#print(data["planet"]["mars"])

class Distance_from_Earth:
    #return an erroneous result: the perihelion (smallest distance from Sun) coincide with the smallest distance from Earth

    def __init__(self,planet, sun_earth, sun_planet, planet_day, planet_ang_velocity):

        self.planet = planet
        self.sun_earth = sun_earth
        self.sun_planet = sun_planet
        self.planet_day = planet_day
        self.planet_ang_velocity = planet_ang_velocity

    def earth_distance(self):

        earth_ang_velocity = 0.9856
        #angles beta (Earth), delta (planet), alpha (Earth-planet) in radians, see drawing
        beta = earth_ang_velocity * self.planet_day
        beta_rad = beta * (math.pi / 180)
        delta = self.planet_ang_velocity * self.planet_day
        delta_rad = delta * (math.pi / 180)
        alpha = beta_rad - delta_rad
        

        self.earth_planet = int(math.sqrt(math.pow(self.sun_earth * math.sin(alpha),2) + math.pow(self.sun_planet - (self.sun_earth * math.cos(alpha)),2)))

    def __repr__(self):

        return "this is day nr {} on {}. It is {} km away from Earth today".format(self.planet_day, self.planet, f"{self.earth_planet:,}")

#objects:

mars_distance = Distance_from_Earth(str("Mars"), sun_earth, sun_mars, mars_day_nr, 0.5313)
mars_distance.earth_distance()
ceres_distance = Distance_from_Earth(str("Ceres"), sun_earth, sun_ceres, ceres_day_nr, 0.214004)
ceres_distance.earth_distance()

#forks

if planet == str("Mercury"):
    print(mercury)
if planet == str("Venus"):
    print(venus)
if planet == str("Earth"):
    print(earth)
if planet == str("Mars"):
    print(mars)
    print(mars_synodic_period)
    print(mars_distance)
if planet == str("Ceres"):
    print(ceres)
    print(ceres_distance)
if planet == str("Pallas"):
    print(pallas)
if planet == str("Vesta"):
    print(vesta)