description = 'listmode replay'

group = 'basic'

includes = ['listmode']

excludes = []

devices = dict(listmode = device('nicos.devices.generic.detector.Detector',
        description = 'Charm or Mesytec 2D Neutron listmode replay',
        timers = ['timer'],
        counters = ['counter'],
        monitors =['monitor0'],
        images = ['histogram'],
        liveinterval = 1.0,
        pollinterval = 1,
        maxage = 1,),)

