Planetracker is meant to help amateur astronomers in the observation of the planets. It calculates for each day of the selected year:

- the distance of the planets from the Sun
- the distance between Earth and the other planets
- the angles between the Earth and the other planets based on the Sun
- the dates of elongations, oppositions and quadratures

Mode of calculation: Sun/planet
------------------------------
Kepler's Law:  r = a ((1 - e2)/(1 + e cos θ))

for:
r= radius (distance Sun/planet in UA)
a = semi-major axis (distance at the periapis; 1UA for the Earth)
e = excentricity (in degrees)
θ = true anomaly

with M = mean anomaly instead of true anomaly

M = n (t - t0), where:
n = mean motion °/day (mean angular velocity = 360°/total year's days)
t = selected day
t0 = date of periapsis

hence the formula:

r = a ((1 - e2)/(1 + e cos M))
r = a ((1 - e2)/(1 + e cos n (t - t0)))


Mode of calculation: Earth/planet:
----------------------------------

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



NB: this is my own formula; please submit objections if any.

