from datetime import datetime, timezone

from dto.environmental_variable import EnvironmentalVariable
from smartgadget import pySmartGadget


def get_reading():
    sht31_smart_gadget = 'CE:D6:5F:23:8A:E8'
    print('Connecting to:', sht31_smart_gadget)
    gadget = pySmartGadget.SHT31(sht31_smart_gadget)
    print('Connected')

    environmental_variable = EnvironmentalVariable(datetime.now(timezone.utc), gadget.readTemperature(),
                                                   gadget.readHumidity())

    return environmental_variable


def main():
    print(get_reading())


if __name__ == "__main__":
    main()
