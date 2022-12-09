# Hi


# Nessecary Modules

from scipy import constants
from skyfield.api import load


# Loading Planets

planets = load('de421.bsp')
while True:
	object = input("Celestial Object (eg Planets, Dwarf Planet, Planetoid): ")
	
	print("\n")
	try:
		earth, jupiter = planets['earth'], planets[ object + ' BARYCENTER']
		
		
		# Time
		ts = load.timescale()
		t = ts.now()
		
		astrometric = earth.at(t).observe(jupiter)
		radec=astrometric.radec()

		# Output

		print("Distance (in Lightyears):", float(constants.astronomical_unit / constants.light_year ) * float(radec[2].au), "Decimal:", "{:.8f}".format(float(constants.astronomical_unit / constants.light_year ) * float(radec[2].au)), "Distance (In AU):", radec[2].au)
		print("\n")
		print("Rad:", radec[0],",", "Dec: ", radec[1])


		
	except:
		pass

