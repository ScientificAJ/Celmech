# Hi


# Nessecary Modules

from scipy import constants
from skyfield.api import load
from skyfield import almanac

# Loading Planets

planets = load('de421.bsp')

# Adding while loop

while True:
    
    # Try and except
    try:
        # Input 
        object = input(
            "Celestial Object (eg Planets, Dwarf Planet, Planetoid): ")

        print("\n")
        if "moon" in object.lower():
            ts = load.timescale()
            t = ts.now()
            moon_phase_type = ""
            moon_phase = almanac.moon_phase(planets, t)
            

            if float(str(moon_phase.degrees).replace(
                    "degree", "").replace("'", "").strip()) > 180.00:
                moon_phase_type = "Waning phase"

            elif float(str(moon_phase.degrees).replace("degree", "").replace("'", "").strip()) < 180.00:
                moon_phase_type = "Waxing phase"

            print(
                "Moon Phase: {:.1f} degrees".format(
                    moon_phase.degrees), ",",  "Phase type: ", moon_phase_type)
        else:
            earth, jupiter = planets['earth'], planets[object + ' BARYCENTER']

            # Time

            ts = load.timescale()
            t = ts.now()

            astrometric = earth.at(t).observe(jupiter)
            radec = astrometric.radec()

            # Output

            print(
                "Distance (in Lightyears):",
                float(
                    constants.astronomical_unit /
                    constants.light_year) *
                float(
                    radec[2].au),
                "Decimal:",
                "{:.8f}".format(
                    float(
                        constants.astronomical_unit /
                        constants.light_year) *
                    float(
                        radec[2].au)),
                "Distance (In AU):",
                radec[2].au)
            print("\n")

            print("Rad:", radec[0], ",", "Dec: ", radec[1])

    except ValueError:
        pass
