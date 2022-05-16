#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import binascii
from pefile import PE

pe = PE("C:\\Windows\\System32\\drivers\\tcpip.sys")
debug = pe.DIRECTORY_ENTRY_DEBUG[0].entry
guid = "{0:08X}{1:04X}{2:04X}{3}{4}".format(debug.Signature_Data1,
                                      debug.Signature_Data2,
                                      debug.Signature_Data3,
                                      binascii.hexlify(debug.Signature_Data4).decode("utf-8"),
                                      debug.Age).upper()
print(guid)
