import os
#os.environ["VERSIONER_PYTHON_PREFER_32_BIT"] = "yes"
os.system("export VERSIONER_PYTHON_PREFER_32_BIT=yes")
from direct.showbase.ShowBase import ShowBase   # import the bits of panda
from panda3d.core import GeoMipTerrain          # that we need
from panda3d.core import Vec3

import vdc_connect
from obj_from_dict import obj_from_dict

 
RESOURCE_DIR = "resources"

pos_for_city = {
 "London 2 (ESX)" : (370, 57, 15),
 "Slough (ESX)" : (359, 55, 15),
}

class DataSource:
    def __init__(self):
        self.api=vdc_connect.create()

    def get_vms(self):
        return obj_from_dict(self.api.listVirtualMachines({})).virtualmachine


class Toaster:
    def __init__(self, location, height, spinning=False):
        self.model = loader.loadModel(os.path.join(RESOURCE_DIR, "toaster/toaster.egg"))
        pos=tuple(map(sum, zip(pos_for_city[location], (0, 0, height*15))))
        self.model.setPos(*pos)
        self.model.setScale(10)
        self.model.reparentTo(render)
        if spinning:
            self.rotation_interval = self.model.hprInterval(20, Vec3(220, 0, 0))
            self.rotation_interval.loop()
 

class MyApp(ShowBase):
    def __init__(self, data_source):
        ShowBase.__init__(self)
        if not os.path.isfile('world.bam'):
            terrain = GeoMipTerrain("worldTerrain")
            terrain.setHeightfield(os.path.join(RESOURCE_DIR, "uk_height_map_25.png"))
            terrain.setColorMap(os.path.join(RESOURCE_DIR, "uk_flopped_rotated_25.png"))
            terrain.setBruteforce(True)
            root = terrain.getRoot()
            root.reparentTo(render)
            root.setSz(10)
            terrain.generate()
            root.writeBamFile('world.bam')
        else:
            world = loader.loadModel("world.bam")
            world.reparentTo(render)

        self.toasters = {}
        self.toasters_by_zone = {}
        for vm in data_source.get_vms():
            height = len(self.toasters_by_zone.get(vm.zonename, []))
            self.toasters[vm.name] = Toaster(vm.zonename, height, vm.state == "Running")
            self.toasters_by_zone.setdefault(vm.zonename, []).append(self.toasters[vm.name])
            

        # In Panda3D you have to cancel the default mouse control to set the camera explicitly
        # Falsify the following 3 lines to allow it back again:
        if True:
            self.disableMouse()
            self.camera.setPos(350, -100, 100)
            self.camera.setHpr(0, -25, 0)
 
data_source = DataSource()
app = MyApp(data_source)                                   # our 'object'
app.run()                                       # away we go!
