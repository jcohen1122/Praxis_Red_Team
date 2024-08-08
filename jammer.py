# RED TEAM CODE
# Face team going down

from bluepy import btle
ali_addy = "d3:ea:a6:7d:56:27"
nate_addy = "3f:ba:f5:38:70:17"

class myDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(f"Notification received: {data}")

def sendUnlimitedPackets():
    print("Connecting to peripheral device...")
    peripheral = btle.Peripheral(ali_addy)
    peripheral.setDelegate(myDelegate())

    print("Connected. Starting unlimited packet send...")
    i = 1
    try:
        while True:
            print(f"Sent data: {i}")
            i += 1

    except KeyboardInterrupt:
        print("Stopping unlimited packet send... lucky.")

    finally:
        print("Disconnecting...")
        peripheral.disconnect()

if __name__ == "__main__":
    sendUnlimitedPackets()
