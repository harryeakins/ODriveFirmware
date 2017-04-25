from generated.RotorAutoGenerated import RotorAutoGenerated


class Rotor(RotorAutoGenerated):

    def __init__(self, motor):
        self.motor = motor
        self._get = motor.odrive._get
        self._set = motor.odrive._set
        self._monitor = motor.odrive._monitor