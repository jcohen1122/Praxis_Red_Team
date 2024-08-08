# RED TEAM CODE
# Face team security...

from bluepy.btle import Scanner, DefaultDelegate, Peripheral, BTLEException, BTLEDisconnectError
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

def main():
    scanner = Scanner().withDelegate(ScanDelegate())

    while True:
        print("Scanning for devices...")
        try:
            devices = scanner.scan(0.5)

            for dev in devices:
                # Only connect to certain mac address
                # Print device info
                print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
                for (adtype, desc, value) in dev.getScanData():
                    print(" %s = %s" % (desc, value))
                print()
                print()

                # Attempt to connect to device
                try:
                    peripheral = Peripheral(dev.addr)
                    print("Connecting to device:", dev.addr)
            
                    # Print services and characteristics
                    if peripheral:
                        services = peripheral.getServices()
                        for service in services:
                            print("Service:", service)
                            characteristics = service.getCharacteristics()
                            for char in characteristics:
                                print("Characteristic: ", char.uuid)
                                print("Characteristic Value", char.read())
                    peripheral.disconnect()
        except BTLEDisconnectError as e:
            print("Error")


if __name__ == "__main__":
    main()
