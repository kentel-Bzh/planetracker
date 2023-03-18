from datetime import datetime
from common_variables import day_number, year_number


class planet_day_calculator:

    #calculates planet date equivalent (day number in the planet year) to earth date given in input
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