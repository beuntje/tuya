# tuya

Dependencies: 
-------------
python libs: requests, os, configparser, json, time


Commands:  
---------

check devices: 
```shell
python main.py devices
```

Turn device on/off: 

```shell
python main.py control=turnOnOff 2587061484cca89b96e0=0 
python main.py control=turnOnOff 2587061484cca89b96e0=1 bf30879fe8110101c2otj4=1
```

Set lamp brighness:

```shell
python main.py control=brightnessSet 2587061484cca89b96e0=0 
python main.py control=brightnessSet 2587061484cca89b96e0=53
python main.py control=brightnessSet 2587061484cca89b96e0=100
``` 
 