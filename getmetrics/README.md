# SmartGadget SHT31

Python interface to Sensirion SmartGadget SHT31 based on bluepy.

This project provides an API to access the functionality of the SmartGadget via BLE.
What's working so far:
  - Connecting
  - Disconnecting
  - Reading
    - Device data: Device name, System ID, Model number, Serial number, Firmware revision, Hardware revision, Software revision, Manufacturer name
    - Battery status
    - Temperature & Humidity (actual values and logged data on device)
    - Oldest & newest timestamp
    - Logging interval
  - Writing
    - Device name
    - Synchronization timestamp
    - Logger interval
- Control notifications
    - Temperature & Humidity

# Usage

Take a look at the main.py example file. For scanning of BLE devices take a look [here](https://ianharvey.github.io/bluepy-doc/scanner.html#sample-code "Documentation of bluepy scanner class").


# Code examples
```python
import smartgadget
from datetime import datetime
import time


def main():
    ble_address = 'F0:D8:7D:63:71:83'
    print('Connecting to:', ble_address)
    gadget = smartgadget.SHT31(ble_address)
    print('Connected')

    print('Device name:', gadget.readDeviceName())

    print('System ID: ', gadget.readSystemId())
    print('Model number string:', gadget.readModelNumberString())
    print('Serial number string:', gadget.readSerialNumberString())
    print('Firmware revision string:', gadget.readFirmwareRevisionString())
    print('Hardware revision string:', gadget.readHardwareRevisionString())
    print('Software revision string:', gadget.readSoftwareRevisionString())
    print('Manufacturer name string:', gadget.readManufacturerNameString())

    print('Battery level [%]:', gadget.readBattery())
    print('Temperature [°C]:', '{:.2f}'.format(gadget.readTemperature()))
    print('Humidity [%]:', '{:.2f}'.format(gadget.readHumidity()))
    gadget.setLoggerIntervalMs(1000 * 60)  # setting a new logger interval will clear all the logged data on the device
    print('LoggerInterval [ms]: ', gadget.readLoggerIntervalMs())
    gadget.setSyncTimeMs()

    # Sleep a bit to enable the gadget to set the SyncTime; otherwise 0 is read when readNewestTimestampMs is used
    time.sleep(0.1)
    print('OldestTimestampMs [µs]:', gadget.readOldestTimestampMs(),
          datetime.utcfromtimestamp(gadget.readOldestTimestampMs() / 1000).strftime('%Y-%m-%d %H:%M:%S'))
    print('NewestTimeStampMs [µs]:', gadget.readNewestTimestampMs(),
          datetime.utcfromtimestamp(gadget.readNewestTimestampMs() / 1000).strftime('%Y-%m-%d %H:%M:%S'))

    gadget.readLoggedDataInterval()

    # enable notifications for humidity values; the object will log incoming data into the loggedData variable
    gadget.setTemperatureNotification(True)

    # enable notifications for humidity values; the object will log incoming data into the loggedData variable
    gadget.setHumidityNotification(True)

    try:
        while True:
            if False is gadget.waitForNotifications(5) or False is gadget.isLogReadoutInProgress():
                print('Done reading data')
                break
            print('Read dataset')
    finally:
        print(gadget.loggedDataReadout)  # contains the data logged by the smartgadget
        print(gadget.loggedData)  # contains the data sent via notifications
        gadget.disconnect()
        print('Disconnected')


if __name__ == "__main__":
    main()

```

# Additional information

[Sensirion Homepage - SHT31 Smart Gadget Development Kit](https://www.sensirion.com/de/umweltsensoren/feuchtesensoren/development-kit/)

[Github of Sensirion](https://github.com/Sensirion "Github of Sensirion")

