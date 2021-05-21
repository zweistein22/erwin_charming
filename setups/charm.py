import nicos_mlz.erwin_charming.nicospath as nicospath

# pylint: disable=C:invalid-name
description = 'charm detector'
# pylint: disable=C;invalid-name
group = 'lowlevel'


tango_base = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/ERWIN-detector/'

sysconfig = dict(datasinks = ['LivePNGSink'])

devices = dict(timer = device('nicos_mlz.erwin_charming.devices.detector.CharmTimerChannel',
        description = 'Timer for the charm detector',
        tangodevice = tango_base + 'MeasureTime',
        pollinterval = 3,
        maxage = 4,),
    counter = device('nicos_mlz.erwin_charming.devices.detector.CharmCounterChannel',
        description = 'Counter for the charm detector',
        tangodevice = tango_base + 'MeasureCounts',
        type = 'counter',
        pollinterval = 3,
        maxage = 4,),
    monitor0 = device('nicos.devices.tango.CounterChannel',
        description = 'Monitor 0 for the charm detector',
        tangodevice = tango_base + 'Monitor0',
        type = 'counter',
        pollinterval = 3,
        maxage = 4,),
     monitor1 = device('nicos.devices.tango.CounterChannel',
        description = 'Monitor 1 for the charm detector',
        tangodevice = tango_base + 'Monitor1',
        type = 'counter',
        pollinterval = 3,
        maxage = 4,),
      monitor2 = device('nicos.devices.tango.CounterChannel',
        description = 'Monitor 2 for the charm detector',
        tangodevice = tango_base + 'Monitor2',
        type = 'counter',
        pollinterval = 3,
        maxage = 4,),
      monitor3 = device('nicos.devices.tango.CounterChannel',
        description = 'Monitor 3 for the charm detector',
        tangodevice = tango_base + 'Monitor3',
        type = 'counter',
        pollinterval = 3,
        maxage = 4,),
    histogram = device('nicos_mlz.erwin_charming.devices.detector.CharmImageChannel',
        description = 'Histogram image  from the device',
        tangodevice = tango_base + 'Histogram',
        pollinterval = 3,
        maxage = 4,),
    histogramraw = device('nicos_mlz.erwin_charming.devices.compare.Image',
        description = 'raw Histogram image  from the device',
        tangodevice = tango_base + 'HistogramRaw',
        compare2 = 'histogram',
        pollinterval = 3,
        maxage = 4,),
     LivePNGSink = device('nicos_mlz.erwin_charming.devices.datasinks.PNGLiveFileSinkF',
        description = 'Saves live image as .png every now and then',
        filename = nicospath.NicosPath.live_png(),
        rgb = True,
        log10 = False,
        flipy = False,
        interval = 1,),
    roimanager = device('nicos_mlz.erwin_charming.devices.roimanager.RoiManager',
        description = 'roi manager',
        tangodevice = tango_base + 'RoiManager',
        pollinterval = 3,
        maxage = 4,
        backgroundimage = 'histogram'),
    settings = device('nicos_mlz.erwin_charming.devices.settings.Settings',
        description = 'Settings manager',
        tangodevice = tango_base + 'Settings',
        pollinterval = 3,
        maxage = 4,),)

startupcode = '''
SetDetectors(charm)
LivePNGSink.size = 512
'''