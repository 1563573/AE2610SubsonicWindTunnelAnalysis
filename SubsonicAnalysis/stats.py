from data import SubsonicWindTunnelData, WindSpeed, EndPlate
from scipy import stats
from astropy import constants as const
from astropy import units as u
from astropy import uncertainty as unc
import numpy as np
from reduction import Data, Results


def do_stats(data):
    res = Results()
    res.high_off = _do_stats_one_config(WindSpeed.HIGH, EndPlate.OFF, data)
    res.high_on = _do_stats_one_config(WindSpeed.HIGH, EndPlate.ON, data)
    res.low_off = _do_stats_one_config(WindSpeed.LOW, EndPlate.OFF, data)
    res.low_on = _do_stats_one_config(WindSpeed.LOW, EndPlate.ON, data)
    return res


def _do_stats_one_config(windSpeed, endPlate, data):
    res = Data()
    for roundAOA in range(21):
        aoaArr = data.get_angle_of_attack(windSpeed, endPlate, roundAOA)
        forceXArr = data.get_force_x(windSpeed, endPlate, roundAOA)
        forceYArr = data.get_force_y(windSpeed, endPlate, roundAOA)
        torqueArr = data.get_torque_z(windSpeed, endPlate, roundAOA)
        voltageArr = data.get_tared_baratron_voltage(windSpeed, endPlate, roundAOA)
        if len(aoaArr) != 0:
            aoaDist = _do_instantaneous_stats(aoaArr)
            forceXDist = _do_instantaneous_stats(forceXArr)
            forceYDist = _do_instantaneous_stats(forceYArr)
            torqueDist = _do_instantaneous_stats(torqueArr)
            voltageDist = _do_instantaneous_stats(voltageArr)

            res.aoa = np.append(res.aoa, aoaDist.pdf_mean())
            res.force_x = np.append(res.force_x, forceXDist.pdf_mean())
            res.force_y = np.append(res.force_y, forceYDist.pdf_mean())
            res.torque = np.append(res.torque, torqueDist.pdf_mean())
            res.voltage = np.append(res.voltage, voltageDist.pdf_mean())

            res.aoa_std = np.append(res.aoa_std, aoaDist.pdf_std())
            res.force_x_std = np.append(res.force_x_std, forceXDist.pdf_std())
            res.force_y_std = np.append(res.force_y_std, forceYDist.pdf_std())
            res.torque_std = np.append(res.torque_std, torqueDist.pdf_std())
            res.voltage_std = np.append(res.voltage_std, voltageDist.pdf_std())

            res.aoa_ns = np.append(res.aoa_ns, aoaDist.n_samples)
            res.force_x_ns = np.append(res.force_x_ns, forceXDist.n_samples)
            res.force_y_ns = np.append(res.force_y_ns, forceYDist.n_samples)
            res.torque_ns = np.append(res.torque_ns, torqueDist.n_samples)
            res.voltage_ns = np.append(res.voltage_ns, voltageDist.n_samples)
    return res


def _do_instantaneous_stats(arr):
    mean = np.mean(arr)
    stdDev = np.std(arr, ddof=1) #/ np.sqrt(len(arr))
    stdDev = (stdDev**2 + (0.01*mean)**2)**.5
    numSamples = 1e5 #len(arr)
    return unc.normal(mean, std=stdDev, n_samples=round(numSamples))