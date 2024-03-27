import asyncio
from bleak import BleakClient

# define ble address and gatt chars
address = "28:CD:C1:07:09:F2" #  replace with your device's MAC address
MODEL_NBR_UUID = "00002a00-0000-1000-8000-00805f9b34fb"   # Model Number characteristic UUID
ADV_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E" # Advertising UUID
RX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E" # Receiving UUID
TX_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E" # Transmitting UUID

# main
async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

        # runs when receiving data from ble server
        def notification_handler(sender: int, data: bytearray):
            print(f"Notification received from {sender}: {data}")

        await client.start_notify(TX_UUID, notification_handler)

        while True:
            # Keep the loop running to receive notifications
            await asyncio.sleep(1)

asyncio.run(main(address))