import mock
import pytest
from pytest_mock import mocker
from bobsensors import *

def test_light_sensor_nightcheck(mocker):
    # Let's simulate that the sensor is telling us it's night
    mocker.patch.object(BOBLightSensor, 'getsensor_value')
    BOBLightSensor.getsensor_value.return_value = 90
    # Now let's test the
    isItNight = BOBLightSensor.is_it_night()
    assert(isItNight == True)

    # Now let's make it day
    BOBLightSensor.getsensor_value.return_value = 100
    isItNight = BOBLightSensor.is_it_night()
    assert(isItNight == False)
