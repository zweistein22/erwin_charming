#  -*- coding: utf-8 -*-
#***************************************************************************
#* Copyright (C) 2020 by Andreas Langhoff *
#* <andreas.langhoff@frm2.tum.de> *
#* This program is free software; you can redistribute it and/or modify *
#* it under the terms of the GNU General Public License v3 as published *
#* by the Free Software Foundation; *
# **************************************************************************
"""Intelligent Powersupply doing ramps etc."""

from nicos import session
from nicos.core import  Param,  listof, status, Readable, Override
from nicos.devices.tango import StringIO
from nicos.services.daemon.script import RequestError, ScriptRequest
from nicos.core.utils import usermethod
from nicos.core.params import Value
from time import time as currenttime
import copy

class CharmPowerSupply(StringIO,Readable):

    parameters = {
        'transitions': Param('transition choices as per entangle device configuration',
                       type=listof(str)),
    }

    parameter_overrides = {
        'pollinterval': Override(default=5),  # every 5 seconds
    }




    def doInit(self, mode):
        n_items = 0
        x = super().status()
        if x[0] == status.OK:
            n_items = self.availablelines
        delays = []
        cmds = []
        availabletransitions = []
        for i in range(n_items):
            delays.append(0)
            cmd = "TR" + str(i)
            cmds.append(cmd)
            availabletransitions = self.multiCommunicate((delays,cmds))
            self._setROParam('transitions',availabletransitions)
        print(self.transitions)

    def doShutdown(self):
        pass


    def read(self, maxage=0):
        s = super().status(maxage)
        sv = self.status_value(s[1])
        return sv[1]



    def status_value(self,s1):
        val = ''
        sta = ''
        i = s1.rfind('[')
        if i >= 0:
            val = s1[i:]
            sta = s1[:i - 1]
            self._cache.put(self, 'value', val, currenttime(), self.maxage)
        return (sta,val)

    def doRead(self, maxage=0):
        return self.read(maxage)


    @usermethod
    def apply(self,*argv):
        """
        applies a transition from the 'transitions' parameter.
        Function argument is index to item in the list.
        """
        if not len(argv):
            index = -1
        else:
            index = argv[0]
        if  index == -1:
            msg = ''
            for i in range(len(self.transitions)):
                if i:
                    msg += " ,"
                msg += self.transitions[i] + " (" + str(i) + ")"

            print(msg)
            print('please use 0 based index  as parameter. No action taken.')
        else:
            if ((len(self.transitions) > index) and (index >= 0)):
                cmd = 'APPLY:' + self.transitions[index]
                print(cmd)
                self.write(cmd)
                print(self.transitions[index])
            else:
                print('index out of range. No action taken.')
