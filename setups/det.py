description = 'charm detector'
group = 'lowlevel'



tango_base = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/ERWIN-detector/'

sysconfig = dict(
    datasinks = ['LivePNGSink']
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
     LivePNGSink = device('nicos.devices.datasinks.PNGLiveFileSink',
        description = 'Saves live image as .png every now and then',
        filename = 'CHARMing/live_lin.png',
        log10 = False,
        interval = 15,
    ),

)

startupcode = '''
SetDetectors(det)
'''