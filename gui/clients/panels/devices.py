from nicos.clients.gui.panels.devices import DevicesPanel

class DevicesPanel1(DevicesPanel):
    def on_client_cache(self, data):
        rv = super().on_client_cache(data)
        (time, key, op, value) = data
        if '/' not in key:
            return
        ldevname, subkey = key.rsplit('/', 1)
        if ldevname not in self._devinfo:
            return

        devitem = self._devitems[ldevname]

        if subkey == 'status':
             t = devitem.text(2)
             i = t.rfind('[')
             if i >=0:
                 t = t[:i-1]
             devitem.setText(2,str(t))
        if ldevname in self._control_dialogs:
                dlg = self._control_dialogs[ldevname]
                ct = dlg.statuslabel.text()
                dlg.statuslabel.setText('Hello' +ct[5:])

        return rv



