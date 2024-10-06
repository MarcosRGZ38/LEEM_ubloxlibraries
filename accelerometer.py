import spidev

spi = spidev.SpiDev(0,1)
spi.open()

def read(n:int):
  data = spi.readbytes(n)
  return data