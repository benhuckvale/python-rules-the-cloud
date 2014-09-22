from auto_complete_setup import *
import vdc_connect
from obj_from_dict import obj_from_dict
a=vdc_connect.create()
request={'region': 'europe'}
zones=obj_from_dict(a.listZones(request))
vms=obj_from_dict(a.listVirtualMachines(request))
