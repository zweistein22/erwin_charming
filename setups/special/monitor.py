import nicos_mlz.erwin_charming.nicospath as nicospath


description = 'setup for the status monitor'
group = 'special'

_expcolumn = Column(Block('Experiment',
        [BlockRow(Field(name = 'Proposal', key = 'Exp/proposal', width = 7),
                Field(name = 'Title',
                    key = 'Exp/title',
                    width = 20,
                    istext = True,
                    maxlen = 20),
                Field(name = 'Current status',
                    key = 'Exp/action',
                    width = 40,
                    istext = True,
                    maxlen = 40),
                Field(name = 'Last file', key = 'Exp/lastscan'),),
            '---',
            BlockRow(Field(name='Histogram', picture=nicospath.NicosPath.live_png(), refresh=2,
                      width=60, height=30),)],),)

devices = dict(Monitor = device('nicos.services.monitor.qt.Monitor',
        title = 'NICOS status monitor',
        loglevel = 'info',
        # Use only 'localhost' if the cache is really running on
        # the same machine, otherwise use the hostname (official
        # computer name) or an IP address.
        cache = 'localhost',
        font = 'Luxi Sans',
        valuefont = 'Consolas',
        padding = 0,
        layout = [Row(_expcolumn),],),)
