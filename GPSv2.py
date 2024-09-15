
import PythonEquivalents.SparkFun_ublox_GNSS_library as ubloxGPS
from time import sleep
from datetime import date

day = date.today()

with open("Medidas {day}") as file:
    print(f"medidas del dia {day}")


port = 'devttyACM0'
myGNSS = ubloxGPS.SFE_UBLOX_GNSS()

sleep(1)


i2c = ubloxGPS.Wire.TwoWire()
i2c.begin()


if myGNSS.begin() == False:
    print("GPS not detected at default adress")


myGNSS.setI2COutput(ubloxGPS.COM_TYPE_UBX)

while True:
    if myGNSS.getPVT():

        latitude = myGNSS.getLatitude()
        print("lat" + latitude/10**7+ "degrees")
        file.write("lat" + latitude/10**7 + "degrees")

        longitude = myGNSS.getLonguitude()
        print("long:"+ longitude/10**7 + "degrees")
        file.write("long:"+ longitude/10**7 + "degrees")

        altitude = myGNSS.getAltitude()
        print("altitude" + altitude/10**8 + "degrees")
        file.write("altitude" + altitude/10**8 + "degrees")

