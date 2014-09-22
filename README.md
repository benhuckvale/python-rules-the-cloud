Python Rules the Cloud: Programs for the workshop at the PyCon 2014 conference
==============================================================================


Workshop information
--------------------

http://www.phillipkent.net/PyConUK-VDC-API-Exercises-20140919.pdf

http://www.phillipkent.net/PyConUK-VDC-API-Challenges-20140919.pdf


Documentation for Interoute VDC
-------------------------------

http://cloudstore.interoute.com/main/knowledge-centre/library/vdc-v2


Challenge 1 - Extracting information
====================================

I've turned the dictionary of data into an object dynamically, so that you can browse it in the repl.
To get started, use the script-then-interactive way of running python:

python -i browse_in_repl.py

For example:

```
>>> vms.<TAB>
vms.as_dict         vms.count           vms.mro(            vms.virtualmachine
>>> vms.virtualmachine
[<class 'obj_from_dict.virtualmachine'>, <class 'obj_from_dict.virtualmachine'>]
>>> x=vms.virtualmachine[0]
>>> x.<TAB>
x.account                x.affinitygroup          x.as_dict                x.cpunumber              x.cpuspeed               x.cpuused
x.created                x.displayname            x.displayvm              x.domain                 x.domainid               x.guestosid
x.haenable               x.hypervisor             x.id                     x.isdynamicallyscalable  x.memory                 x.mro(
x.name                   x.networkkbsread         x.networkkbswrite        x.nic                    x.passwordenabled        x.rootdeviceid
x.rootdevicetype         x.securitygroup          x.serviceofferingid      x.serviceofferingname    x.state                  x.tags
x.templatedisplaytext    x.templateid             x.templatename           x.zoneid                 x.zonename
>>> x.name
u'Cobra'
```


Challenge 2 - interesting representation
========================================

I thought I'd play around with Panda3D. Created a height map of the uk and plotted the virtual machines retrieved in their geographic locations. It's just for London and Slough. I couldn't find a 'Computer' 3d asset so I used toasters. If the toaster is spinning the VM is running. Multiple VMs in the same location stack up.

On Mac OS X I found I had to:

```
install Panda3d sdk from http://www.panda3d.org/download.php?sdk
install nvidia's cg toolkit from https://developer.nvidia.com/cg-toolkit-download
sudo cp /Library/Python/2.5/site-packages/Panda3D.pth /Library/Python/2.7/site-packages/
export VERSIONER_PYTHON_PREFER_32_BIT=yes
python visualise_3d.py
```

Included screenshot file: screenshot_visualise_3d.png
