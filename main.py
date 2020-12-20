from tuya import Tuya
import pprint 

from sys import argv


TUYA = Tuya()

def get_arg(key): 
    for arg in argv:
        x = arg.split('=', 1)
        if (len(x) == 2):
            if (x[0] == key): 
                return x[1]
    return False
 


if "devices" in argv: 
    for device in TUYA.devices():  
        print "{}: ".format(device['name'])
        print('=' * (len(device['name']) + 1))
        print "- ID: {}".format(device['id'])
        print "- Type: {}".format(device['ha_type'])
        print "- Data:"
        for key in device['data']: 
            print "  - {}: {}".format(key, device['data'][key]) 
        print ''

control = get_arg('control')
if (control):
    for arg in argv:
            x = arg.split('=', 1)
            if (len(x) == 2):
                if (x[0] != 'control'): 
                    print 'action: {}, device: {}, value: {}'.format(control, x[0], x[1])
                    print TUYA.control(control, x[0], x[1])
 