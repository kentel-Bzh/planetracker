import math
import unittest

#a = semi-major axis
    #e = excentricity
    #n = angular velocity
    #t = day
    #t0 = apsis day

def kepler_law_mercury(t):
    distance_UA = float(0.387098 *(1 - 0.2056**2) / (1 + 0.2056 * math.cos(4.1477 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km

def kepler_law_earth(t):
      
    distance_UA = float(1 *(1 - 0.01671**2) / (1 + 0.01671 * math.cos(0.9856 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km

def kepler_law_venus(t):
    distance_UA = float(0.723336 *(1 - 0.00678**2) / (1 + 0.00678 * math.cos(1.6243 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km


def kepler_law_mars(t):

    distance_UA = float(1.52371 *(1 - 0.09339**2) / (1 + 0.09339 * math.cos(0.5240 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km

def kepler_law_ceres(t):

    distance_UA = float(2.768134 *(1 - 0.0757051**2) / (1 + 0.0757051 * math.cos(0.214004 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km

def kepler_law_vesta(t):
    distance_UA = float(2.36179 *(1 - 0.089366**2) / (1 + 0.089366 * math.cos(0.2752 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km

def kepler_law_pallas(t):
    distance_UA = float(2.7724 *(1 - 0.0231**2) / (1 + 0.231 * math.cos(0.21353 * (t))))
    distance_km = int(distance_UA * 149597870)
    return distance_km

class Test(unittest.TestCase):

    def test_kepler_mercury(self):
        for num in [1,88,1]:
            with self.subTest(num = num):
                self.assertLess(46001200, kepler_law_mercury(num))
                self.assertLess(kepler_law_mercury(num), 69816900) 

    
    def test_kepler_venus(self):
         for num in [1,365,1]:
               with self.subTest(num = num):
                    self.assertLess(107476000, kepler_law_venus(num))
                    self.assertLess(kepler_law_venus(num), 108943000)

    def test_kepler_earth(self):
         for num in [1,365,1]:
               with self.subTest(num = num):
                    self.assertLess(147097000, kepler_law_earth(num))
                    self.assertLess(kepler_law_earth(num), 152097000)

    def test_kepler_mars(self):
          
          for num in [1, 687, 1]:
                self.message = str("The value exceeds the maximum distance at perihelion")
                with self.subTest(num = num):
                      
                      self.assertLess(206000000, kepler_law_mars(num))
                      self.assertLess(kepler_law_mars(num), 249000000)
    
    def test_kepler_ceres(self):
        for num in [1,1679,1]:
            with self.subTest(num = num):
                self.assertLess(381419582, kepler_law_ceres(num))
                self.assertLess(kepler_law_ceres(num), 447838164)

    def test_kepler_vesta(self):
        for num in [1,1325,1]:
            with self.subTest(num = num):
                self.assertLess(321767047, kepler_law_vesta(num))
                self.assertLess(kepler_law_vesta(num), 384920740)           
                      
    def test_kepler_pallas(self):
        for num in [1,1686,1]:
            with self.subTest(num = num):
                self.assertLess(319358000, kepler_law_pallas(num))
                self.assertLess(kepler_law_pallas(num), 510077000)            

if __name__ == '__main__':
    unittest.main()

#mars = distance_from_sun(1.52371, 0.09339, 0.5240, mars_day_nr, 0)