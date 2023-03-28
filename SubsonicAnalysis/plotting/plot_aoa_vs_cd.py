from matplotlib import pyplot as plt
from os import path


def plot(data, directory=None, fname=None):
    fig, ax = plt.subplots()
    ax.errorbar(data.low_off.aoa, data.low_off.cd, yerr=data.low_off.cd_std, fmt="b.-",
                label=f"$v_\infty = {round(data.low_off.velocity.mean().value, 2)} m/s$")
    ax.errorbar(data.high_off.aoa, data.high_off.cd, yerr=data.high_off.cd_std, fmt="m.-",
                label=f"$v_\infty = {round(data.high_off.velocity.mean().value, 2)} m/s$")
    ax.errorbar(data.low_on.aoa, data.low_on.cd, yerr=data.low_on.cd_std, fmt="k.-",
                label=f"$v_\infty = {round(data.low_on.velocity.mean().value, 2)} m/s$, with end plate")
    ax.errorbar(data.high_on.aoa, data.high_on.cd, yerr=data.high_on.cd_std, fmt="c.-",
                label=f"$v_\infty = {round(data.high_on.velocity.mean().value, 2)} m/s$, with end plate")

    ax.legend()
    ax.grid()

    ax.set_ylabel("Coefficient of Drag, $C_d$")
    ax.set_xlabel("Angle of Attack, $\\alpha$ ($\degree$)")

    plt.minorticks_on()

    if directory is not None and fname is not None:
        plt.savefig(path.join(directory, fname))

    plt.show()
