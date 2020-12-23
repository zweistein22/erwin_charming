description = 'charm detector'
group = 'lowlevel'



tango_base = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/ERWIN-detector/'

sysconfig = dict(
    datasinks = ['Histogram']
)

devices = dict(
    timer = device('nicos.devices.tango.TimerChannel',
        description = 'Timer for the charm detector',
        tangodevice = tango_base + 'MeasureTime',
        pollinterval = 3,
        maxage = 4,
    ),
    counter = device('nicos.devices.tango.CounterChannel',
        description = 'Counter for the charm detector',
        tangodevice = tango_base + 'MeasureCounts',
        type = 'counter',
        pollinterval = 3,
        maxage = 4,
    ),
    histogram = device('nicos.devices.tango.BaseImageChannel',
        description = 'Histogram image  from the device',
        tangodevice = tango_base + 'Histogram',
        pollinterval = 3,
        maxage = 4,
    ),
    det = device('nicos.devices.generic.detector.Detector',
        description = 'Charm or Mesytec 2D Neutron detector',
        timers = ['timer'],
        monitors = [],
        images = ['histogram'],
        liveinterval = 5.0,
    ),


)

startupcode = '''
SetDetectors(det)
'''