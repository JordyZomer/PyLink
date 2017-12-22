"""
Unit tests for pylinkirc.classes
"""

import unittest
from pylinkirc.classes import *

class ChannelSmartBansCoreTestCase(unittest.TestCase):
    def _test_smart_ban_core(self, sinput, soutput):
        self.assertEqual(Channel._make_smartban(sinput), soutput)

    def test_smartban_forward_v6(self):
        self._test_smart_ban_core('2605:fb80:f000:541::1', '2605:fb80:f000:541::*')
        self._test_smart_ban_core('1:222:333:4444:xyz:ghj:klq:sssw', '1:222:333:4444:*')
        self._test_smart_ban_core('234:567::klq:sssw', '234:567::*')
        self._test_smart_ban_core('0::1', '0::*')
        self._test_smart_ban_core('0::g', '0::*')

    def test_smartban_forward_v4(self):
        self._test_smart_ban_core('1.2.3.4', '1.2.*')
        self._test_smart_ban_core('10.129.ey.sq', '10.129.*')

    def test_smartban_general(self):
        self._test_smart_ban_core('12345678.9ABCDEF0.0000000.IP', '*.9ABCDEF0.0000000.IP')
        self._test_smart_ban_core('2636D9B1:484C2B21:6149628:IP', '*:484C2B21:6149628:IP')
        self._test_smart_ban_core('hidden-v3atuu.fibre.someisp.net', '*.fibre.someisp.net')
        self._test_smart_ban_core('2.3.4.5.someip.net', '*.3.4.5.someip.net')
        self._test_smart_ban_core('ip1-2-3-40.someip.net', '*.someip.net')
        self._test_smart_ban_core('irc-123ada.ip-10-252-14.net', '*.ip-10-252-14.net')
        self._test_smart_ban_core('magicnet-s38.uhq.150.12.IP', '*.uhq.150.12.IP')
        self._test_smart_ban_core('n0body.Users.MyNet.org', '*.Users.MyNet.org')
        self._test_smart_ban_core('staff.blahnet.tk', '*.blahnet.tk')

    def test_smartban_keep_as_is(self):
        self._test_smart_ban_core('overdrivenetworks.com', 'overdrivenetworks.com')
        self._test_smart_ban_core('Clk-123A4567.com', 'Clk-123A4567.com')
        self._test_smart_ban_core('unaffiliated/tacocat', 'unaffiliated/tacocat')
        self._test_smart_ban_core('overdrive-irc/staff/GLolol', 'overdrive-irc/staff/GLolol')
        self._test_smart_ban_core('overdrive-irc/3.years.club/GLolol', 'overdrive-irc/3.years.club/GLolol')

if __name__ == '__main__':
    unittest.main()
