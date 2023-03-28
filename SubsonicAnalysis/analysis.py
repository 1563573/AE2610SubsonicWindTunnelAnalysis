from parameters import *
from reduction import *
from astropy import uncertainty as unc
from uncertainties import ufloat
import numpy as np


def calculate(data):
    _calculate_local(data.high_on)
    _calculate_local(data.high_off)
    _calculate_local(data.low_on)
    _calculate_local(data.low_off)


def _calculate_local(data):
    velocity_list = []

    for i in range(len(data.aoa)):
        force_x = unc.normal(data.force_x[i], std=data.force_x_std[i], n_samples=round(data.force_x_ns[i]))
        force_y = unc.normal(data.force_y[i], std=data.force_y_std[i], n_samples=round(data.force_y_ns[i]))
        torque = unc.normal(data.torque[i], std=data.torque_std[i], n_samples=round(data.torque_ns[i]))
        voltage = unc.normal(data.voltage[i], std=data.voltage_std[i], n_samples=round(data.voltage_ns[i]))

        dynamic_pressure = voltage * baratron_sensitivity

        velocity = np.sqrt(2 / air_density * dynamic_pressure).to(u.m / u.s)
        velocity_list.append(velocity)

        lift_force = force_x
        drag_force = force_y

        cl = -lift_force / dynamic_pressure / planform_area_wing
        cd = -drag_force / dynamic_pressure / planform_area_wing
        cm = torque / dynamic_pressure / planform_area_wing / chord_wing

        data.velocity = np.append(data.velocity, velocity.pdf_mean())
        data.velocity_std = np.append(data.velocity_std, velocity.pdf_std())
        data.velocity_ns = np.append(data.velocity_ns, velocity.n_samples)

        data.cl = np.append(data.cl, cl.pdf_mean())
        data.cl_std = np.append(data.cl_std, cl.pdf_std())
        data.cl_ns = np.append(data.cl_ns, cl.n_samples)

        data.cd = np.append(data.cd, cd.pdf_mean())
        data.cd_std = np.append(data.cd_std, cd.pdf_std())
        data.cd_ns = np.append(data.cd_ns, cd.n_samples)

        data.cm = np.append(data.cm, cm.pdf_mean())
        data.cm_std = np.append(data.cm_std, cm.pdf_std())
        data.cm_ns = np.append(data.cm_ns, cm.n_samples)

    sum_vel = 0
    sum_vel_std = 0
    for vel in velocity_list:
        sum_vel += vel.pdf_mean()
        sum_vel_std += vel.pdf_std()**2
    sum_vel_std = sum_vel_std**.5

    sum_vel /= len(velocity_list)
    sum_vel_std /= len(velocity_list)
