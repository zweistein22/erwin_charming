description = 'charm detector'

group = 'basic'

includes = ['charm']

excludes = []

devices = dict(
   charm = device('nicos.devices.generic.detector.Detector',
        description = 'Charm or Mesytec 2D Neutron detector',
        timers = ['timer'],
        counters = ['counter'],
        monitors =['monitor0'],
        images = ['histogram'],
        liveinterval = 5.0,
    ),
   hvsupply = device('nicos_mlz.erwin-charming.devices.charm_HV.CharmPowerSupply',
        description = 'iges CC2X HV',
        tangodevice = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/Erwin/HV-IntelligentPowersupply',
        pollinterval = 3,
        maxage = 4,
   ),

)

