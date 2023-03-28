import numpy as np
from astropy import units as u

class Results:
    def __init__(self):
        self.high_on = None
        self.high_off = None
        self.low_on = None
        self.low_off = None


class Data:
    def __init__(self):
        self.aoa = np.empty(0) * u.deg
        self.force_x = np.empty(0) * u.N
        self.force_y = np.empty(0) * u.N
        self.torque = np.empty(0) * u.N * u.m
        self.voltage = np.empty(0) * u.V
        self.velocity = np.empty(0) * u.m / u.s
        self.cl = np.empty(0)
        self.cd = np.empty(0)
        self.cm = np.empty(0)

        self.aoa_std = np.empty(0) * u.deg
        self.force_x_std = np.empty(0) * u.N
        self.force_y_std = np.empty(0) * u.N
        self.torque_std = np.empty(0) * u.N * u.m
        self.voltage_std = np.empty(0) * u.V
        self.velocity_std = np.empty(0) * u.m / u.s
        self.cl_std = np.empty(0)
        self.cd_std = np.empty(0)
        self.cm_std = np.empty(0)

        self.aoa_ns = np.empty(0)
        self.force_x_ns = np.empty(0)
        self.force_y_ns = np.empty(0)
        self.torque_ns = np.empty(0)
        self.voltage_ns = np.empty(0)
        self.velocity_ns = np.empty(0)
        self.cl_ns = np.empty(0)
        self.cd_ns = np.empty(0)
        self.cm_ns = np.empty(0)

        self.average_velocity = 0 * u.m / u.s
        self.average_velocity_std = 0 * u.m / u.s
        self.average_velocity_ns = 0
