from lifxtools import VirtualDevice
import pytest


vdevice = VirtualDevice()

# store volume before tests
# _volume_before_tests = mc.gvol()
# _mute_before_tests = mc.gmute()

class Test_VirtualDevice():

    def test_assert(self):
        assert lal.running == False

#     def test_svol_TypeErrors(self):
#         with pytest.raises(TypeError):
#             mc.svol(4.5) # no floats
#         with pytest.raises(TypeError):
#             mc.svol("30") # no strings

print("end of tests")
