from matplotlib import pyplot as plt
from os import path
from data import WindSpeed, EndPlate
import numpy as np


def plot(data, directory=None, fname=None):
    fig, ax = plt.subplots()

    ax.plot(data.get_force_x(WindSpeed.HIGH, EndPlate.ON, 16), label=f"$\\alpha = {round(data.get_angle_of_attack(WindSpeed.HIGH, EndPlate.ON, 16)[0].value,2)}\\degree$")
    ax.plot(data.get_force_x(WindSpeed.HIGH, EndPlate.ON, 17), label=f"$\\alpha = {round(data.get_angle_of_attack(WindSpeed.HIGH, EndPlate.ON, 17)[0].value,2)}\\degree$")
    ax.plot(data.get_force_x(WindSpeed.HIGH, EndPlate.ON, 18), label=f"$\\alpha = {round(data.get_angle_of_attack(WindSpeed.HIGH, EndPlate.ON, 18)[0].value,2)}\\degree$")

    # aoa = np.linspace(0, 20)
    # cl = aoa / 180 * np.pi * 2 * np.pi
    #
    # ax.plot(aoa, cl)

    ax.legend()
    ax.grid()

    ax.set_xlabel("Measurement Index")
    ax.set_ylabel("Force in $x$ Direction (N)")

    plt.minorticks_on()

    if directory is not None and fname is not None:
        plt.savefig(path.join(directory, fname))

    plt.show()
