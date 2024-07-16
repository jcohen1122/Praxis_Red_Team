from bluez_peripheral.advert import Advertisement
from bluez_peripheral.util import get_message_bus
import asyncio
import dbus

async def main():
    service_ids = ["fff0"]
    appearance = 0
    timeout = 60
    advert = Advertisement("redTeam", service_ids, appearance, timeout)
    bus = await get_message_bus()
    print("Advertising...")

    await advert.register(bus)

    try:
        i = 0
        while True:
            print(i, ": Connected...")
            i += 1
        print("Disconnected.")
    except KeyboardInterrupt:
        print("Stopping Advertisment...")

if __name__ == "__main__":
    asyncio.run(main())
