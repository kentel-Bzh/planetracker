from datetime import datetime 
from datetime import timedelta

from common_variables import datetime_date

class Oppositions:

    def __init__(self, first_opposition, synodic_period):
        self.first_opposition = first_opposition
        self.synodic_period = synodic_period
        
        
    def oppositions(self):

        # calculating end date by adding days
        self.next_opposition = self.first_opposition + timedelta(days = self.synodic_period)
        next_opposition_year = int(self.next_opposition.year)
        next_opposition_month = int(self.next_opposition.month)
        next_opposition_day = int(self.next_opposition.day)
        input_year_date = int(datetime_date.year)
        input_month_date = int(datetime_date.month)
        input_day_date = int(datetime_date.day)

        #loop
        while next_opposition_year < input_year_date:
        
            #setting next_opposition date as a counter incremented by n * synodic periods
            self.next_opposition = self.next_opposition + timedelta(days = self.synodic_period)
            #updating the date
            next_opposition_year = int(self.next_opposition.year)
            next_opposition_month = int(self.next_opposition.month)
        
            if next_opposition_year == int(self.next_opposition.year) and next_opposition_month < input_month_date:

                #avoids returning a date earlier in the year    
                self.next_opposition = self.next_opposition + timedelta(days=780)
                next_opposition_year = int(self.next_opposition.year)
                next_opposition_month = int(self.next_opposition.month)

            if next_opposition_year == int(self.next_opposition.year) and next_opposition_month == input_month_date and next_opposition_day < input_day_date:

                #avoids returning a date earlier in the month
                self.next_opposition = self.next_opposition + timedelta(days=780)
                next_opposition_year = int(self.next_opposition.year)
                next_opposition_month = int(self.next_opposition.month)
        
    def __repr__(self):

        return "next opposition the: {}/{}/{} ".format(self.next_opposition.day, self.next_opposition.month, self.next_opposition.year)
