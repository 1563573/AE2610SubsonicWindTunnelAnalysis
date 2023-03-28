from astropy.units import imperial as i
from astropy import units as u
from astropy.units import cds as c
from astropy import constants as const

i.enable()
c.enable()


span_wing = 27 * i.inch
span_end_plate = 0.08 * i.inch
chord_wing = 12.2 * i.inch
chord_end_plate = 22 * i.inch
max_thickness_wing = 3 * i.inch
max_thickness_end_plate = 9 * i.inch

planform_area_wing = span_wing * chord_wing

baratron_sensitivity = 1.016 * c.mmHg / u.V

room_temp = (70 * i.deg_F).to(u.K, equivalencies=u.temperature())
room_pressure = 97.88 * u.kPa
air_density = 1.15 * u.kg / u.m**3

gas_constant_air = (const.R / (28.9647 * u.g / u.mol)).to(u.J/u.kg / u.K)
# https://www.engineeringtoolbox.com/molecular-mass-air-d_679.html