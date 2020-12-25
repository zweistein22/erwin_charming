description = 'charm detector setup'
group = 'lowlevel'



tango_base = 'tango://ictrlfs.ictrl.frm2.tum.de:10000/test/ERWIN-detector/'



startupcode = '''
SetDetectors(charm)
'''