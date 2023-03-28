from matplotlib import pyplot as plt
from os import path


def plot(data, directory=None, fname=None):
    fig, ax = plt.subplots()
    ax.errorbar(data.low_off.aoa, data.low_off.cm, yerr=data.low_off.cm_std, fmt="b.-",
                label=f"$v_\infty = {round(data.low_off.velocity.mean().value, 2)} m/s$")
    ax.errorbar(data.high_off.aoa, data.high_off.cm, yerr=data.high_off.cm_std, fmt="m.-",
                label=f"$v_\infty = {round(data.high_off.velocity.mean().value, 2)} m/s$")
    ax.errorbar(data.low_on.aoa, data.low_on.cm, yerr=data.low_on.cm_std, fmt="k.-",
                label=f"$v_\infty = {round(data.low_on.velocity.mean().value, 2)} m/s$, with end plate")
    ax.errorbar(data.high_on.aoa, data.high_on.cm, yerr=data.high_on.cm_std, fmt="c.-",
                label=f"$v_\infty = {round(data.high_on.velocity.mean().value, 2)} m/s$, with end plate")

    ax.legend()
    ax.grid()

    ax.set_ylabel("Pitching Moment Coefficient, $C_m$")
    ax.set_xlabel("Angle of Attack, $\\alpha$ ($\degree$)")

    plt.minorticks_on()

    if directory is not None and fname is not None:
        plt.savefig(path.join(directory, fname))

    plt.show()
