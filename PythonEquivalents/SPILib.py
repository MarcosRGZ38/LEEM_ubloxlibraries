import spidev
import time 

bus = 0 
device = 1 


class SPI:
    def __init__(self):
        self.spi = spidev.SpiDev()
        
    def begin(self, bus, device):
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 500000
        self.spi.mode = 0
    
    def clear_display(self):
        self.msg = [0x76]
        self.spi.xfer2(self.msg)
        time.sleep(5)
        
    def send(self, msg):
        self.spi.xfer2(msg)
    
    
        

    

