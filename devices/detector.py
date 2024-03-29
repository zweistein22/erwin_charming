#  -*- coding: utf-8 -*-
#***************************************************************************
#* Copyright (C) 2020 by Andreas Langhoff *
#* <andreas.langhoff@frm2.tum.de> *
#* This program is free software; you can redistribute it and/or modify *
#* it under the terms of the GNU General Public License v3 as published *
#* by the Free Software Foundation; *
# **************************************************************************
import re
import time
from nicos.core.status import BUSY
from nicos.devices.tango import TimerChannel, CounterChannel, ImageChannel


def isdaqrunning(state1:str):
    items = []
    if state1:
        # pylint: disable=anomalous-backslash-in-string
        items = re.split(',| |=|\*|\n',state1)
        # from CHARMing/charm/Mcpd8.enums.hpp
        if 'DAQ_Running' in items:
            return True
    return False

class CharmTimerChannel(TimerChannel):
    def status(self, maxage=0):
        state = super().status(maxage)
        if isdaqrunning(state[1]):
            return (BUSY, state[1])
        return state

    # pylint: disable=C:invalid-name
    def doStart(self):
       # time.sleep(0.5)
        super().doStart()

 #   def doStop(self):
 #       super.doStop()




class CharmCounterChannel(CounterChannel):
    def status(self, maxage=0):
        state = super().status(maxage)
        if isdaqrunning(state[1]):
            return (BUSY, state[1])
        return state

class CharmImageChannel(ImageChannel):
    # pylint: disable=C:invalid-name
    def doPrepare(self):
        super().doPrepare()
        res = []
        res.append(0)
        # pylint: disable=attribute-defined-outside-init
        self.readresult = res

