Planetracker is meant to help amateur astronomers in the observation of the planets. It calculates for each day of the selected year:

- the distance of the planets from the Sun
- the distance between Earth and the other planets
- the angles between the Earth and the other planets based on the Sun
- the dates of elongations, oppositions and quadratures

Sun/Earth
----------------
[distance_from_sun]

Kepler's Law:  r = a ((1 - e2)/(1 + e cos θ))

for:
r= radius (distance Sun/planet in UA)
a = semi-major axis (distance at the perihelion; 1UA for the Earth)
e = excentricity (in degrees)
θ = true anomaly

with M = mean anomaly instead of true anomaly

M = n (t - t0), where:
n = mean motion °/day (mean angular velocity = 360°/total year's days)
t = selected day
t0 = date of perihelion 

hence the formula:

r = a ((1 - e2)/(1 + e cos M))
r = a ((1 - e2)/(1 + e cos n (t - t0)))

-- date (t) conversion for the other planets: 
[planet_day_calculator]

The date given in input by the user is an Earth date dd/mm/yyyy which has to be converted into the day number within the selected planet year. F. ex. Mars' year has 686,9 days, starting at the date of the perihelion. 

We take the date of the last perihelion (from when I'm writing here, ie march 2023); Mars was last at perihelion on 21/06/2022 and we calculate the remaining days until the 01/01/2023 = 224 [day_shift] + we add the number of Earth years since that date [years_after_last_perihelion] + the remaining number of days [day_number]. The result is the total number of days since the perihelion in 2022. We can then use the modulus function % to compute the remaining days after the last complete martian year [planet_day_nr]




Mode of calculation: Earth/outer planet:
-------------------------------------------------------------
I used there a bit of trigonometry and a bit of Pythagoras (see the detailed sketches on the repository).

∆Ep = √((∆E sin α)^2 + (∆p - ∆E cos α)^2)

with: 

α : angle between the Earth and the selected planet at input date
∆Ep : distance Earth/selected planet
∆E : distance Sun/Earth
∆p : distance Sun/selected planet 

with α = t(wE - wp)

where:

t = date in days
wE = angle between the actual position of the Earth and its last opposition with the selected planet
wp = angle between the actual position of the selected planet and its last opposition with Earth

hence the first developped formula:

∆Tp = √((∆T sint(wE - wp))^2 + (∆p - ∆T cos t(wE - wp))^2)
  
where
wE = tnE
wp = tnp

that is, the date (t) * mean motion in °/day of the Earth (E) or the selected planet (p)

hence the second developped formula applied in the program:

∆TP = √((∆T sint(tnE - tnp))^2 + (∆p - ∆T cos t(tnE - tnp))^2)

and the third formula using Kepler's 3rd Law to compute the distances:

∆To = a ((1 - e2)/(1 + e cos n (t - to))

where:

∆To = distance Sun/Earth at the date of the opposition with the selected planet
to = date of the last opposition



please submit objections if any.

