import smbus2 as smbus
import time


I2C_BUFFER_LENGHT = 120

# registros rpi5
# Address = 0x46 y 0x47
# 0x00 == modo standby (00)
# 0x01 == modo activo  (01)



# registros dentro del GPS:
# read data stream == 0xFF





class TwoWire:
     rpiAdress = 0x46
     gpsReadRegister = 0xFF
     standbyMode = 0x00
     activeMode = 0x01


     def begin():
          # iniciar bus
          try:
               bus = smbus.SMBus(1)
          except Exception as ex:
               print("bus not connected at pin 1")
               return ex

          bus.write_byte_data(TwoWire.rpiAdress, TwoWire.gpsReadRegister, TwoWire.activeMode)
          #Seleccionar modo activo
          bus.write_byte_data(TwoWire.rpiAdress, TwoWire.gpsReadRegister, 0x0E)
          #Seleccionar registro de configuracion 0x0E (14)
          bus.write_byte_data(TwoWire.rpiAdress, TwoWire.gpsReadRegister, TwoWire.activeMode)

          time.sleep(0.5)


     def read_i2c_data(lenght):
          #iniciar bus en el puerto 1
          try:
               bus = smbus.SMBus(1)
          except Exception as ex:
               print("bus not connected at pin 1")
               return ex

          return bus.read_i2c_block_data(TwoWire.rpiAdress, TwoWire.gpsReadRegister, lenght)

