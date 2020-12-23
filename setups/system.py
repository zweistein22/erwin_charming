description = 'system setup'

group = 'lowlevel'

sysconfig = dict(
    cache = 'localhost',
    instrument = 'Erwin-demo',
    experiment = 'Exp',
    datasinks = ['filesink', 'conssink', 'dmnsink', 'livesink','rawsink'],
    notifiers = [],
)


modules = ['nicos.commands.standard']

tango_base = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/ERWIN-detector/'

devices = dict(
    demo = device('nicos.devices.instrument.Instrument',
        description = 'Erwin demo instrument',
        instrument = 'ERWIN-DEMO',
        responsible = 'andreas langhoff <andreas.langhoff@frm2.tum.de>',
        website = 'http://www.nicos-controls.org',
        operators = ['NICOS developer team'],
        facility = 'NICOS demo instruments',
    ),
     Sample = device('nicos.devices.tas.TASSample',
        description = 'sample object',
    ),
    Exp = device('nicos.devices.experiment.Experiment',
        description = 'experiment object',
        dataroot = 'data',
        sendmail = False,
        serviceexp = 'service',
        sample = 'Sample',
        reporttemplate = '',
    ),
    filesink = device('nicos.devices.datasinks.AsciiScanfileSink'),
    conssink = device('nicos.devices.datasinks.ConsoleScanSink'),
    dmnsink = device('nicos.devices.datasinks.DaemonSink'),
    Space = device('nicos.devices.generic.FreeSpace',
        description = 'The amount of free space for storing data',
        warnlimits = (5., None),
        path = None,
        minfree = 5,
    ),
    LogSpace = device('nicos.devices.generic.FreeSpace',
        description = 'Space on log drive',
        path = 'log',
        warnlimits = (.5, None),
        minfree = 0.5,
        lowlevel = True,
    ),
    UBahn = device('nicos_mlz.devices.ubahn.UBahn',
        description = 'Next subway departures',
    ),
    CharmHV = device('nicos_mlz.erwin.devices.charm_HV.CharmPowerSupply',
        description = 'iges CC2X HV',
        tangodevice = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/Erwin/HV-IntelligentPowersupply',
        pollinterval = 3,
        maxage = 4,
   ),

   livesink = device('nicos.devices.datasinks.LiveViewSink',
        description = 'Sends image data to LiveViewWidget',
    ),
    rawsink = device('nicos.devices.datasinks.RawImageSink',
        description = 'Saves image data in RAW format',
        filenametemplate = [
            '%(proposal)s_%(pointcounter)s.raw',
            '%(proposal)s_%(scancounter)s_%(pointcounter)s_%(pointnumber)s.raw'
        ],
    ),
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
    histogram = device('nicos.devices.tango.ImageChannel',
        description = 'Histogram image  from the device',
        tangodevice = tango_base + 'Histogram',
        pollinterval = 3,
        maxage = 4,
    ),
    roimanager = device('nicos_mlz.erwin.devices.roimanager.RoiManager',
        description = 'roi manager',
        tangodevice = tango_base + 'RoiManager',
        pollinterval = 3,
        maxage = 4,
   ),
)

startupcode = '''
from nicos.core import SIMULATION
if not Exp.proposal and Exp._mode != SIMULATION:
    try:
        SetMode('master')
    except Exception:
        pass
    else:
        NewExperiment(0, 'NICOS demo experiment',
                      localcontact='H. Maier-Leibnitz <heinz.maier-leibnitz@frm2.tum.de>')
        AddUser('Nico Suser <nico.suser@frm2.tum.de>')
        NewSample('Gd3CdB7')
'''
