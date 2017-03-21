class BOBSensors:
    def get_all_active_sensors():
        pass

class BOBLightSensor:

    def getsensor_value():
        return 233;

    def is_it_night():
        sensorvalue = BOBLightSensor.getsensor_value()
        print(sensorvalue)
        if sensorvalue < 100:
            return True
        else:
            return False
