description = 'charm detector setup'

group = 'lowlevel'

excludes = []

sysconfig = dict(
    datasinks = ['Histogram']
)

devices = dict(
    det = device('nicos.devices.generic.detector.Detector',
        description = 'Charm or Mesytec 2D Neutron detector',
        timers = ['timer'],
        monitors = [],
        images = ['histogram'],
        liveinterval = 5.0,
    ),
)

startupcode = '''

'''
