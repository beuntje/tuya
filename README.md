# tuya

Dependencies: 
-------------
python libs: requests, os, configparser, json, time


Commands:  
---------

Check devices: 
```shell
python main.py devices
```

Apply actions: use "control=xxx" and one or multiple "deviceID=value" 

```shell
python main.py control=turnOnOff az87061484cca89b96e0=0 
python main.py control=turnOnOff az87061484cca89b96e0=1 bf38879fed110101c2otj4=1
python main.py control=brightnessSet az87061484cca89b96e0=53
``` 
 