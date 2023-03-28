from matplotlib import pyplot as plt
from os import path


def plot(data, directory=None, fname=None):
    fig, ax = plt.subplots()
    ax.errorbar(data.low_off.cd, data.low_off.cl, yerr=data.low_off.cl_std, xerr=data.low_off.cd_std, fmt="b.-",
                label=f"$v_\infty = {round(data.low_off.velocity.mean().value, 2)} m/s$")
    ax.errorbar(data.high_off.cd, data.high_off.cl, yerr=data.high_off.cl_std, xerr=data.high_off.cd_std, fmt="m.-",
                label=f"$v_\infty = {round(data.high_off.velocity.mean().value, 2)} m/s$")
    ax.errorbar(data.low_on.cd, data.low_on.cl, yerr=data.low_on.cl_std, xerr=data.low_on.cd_std, fmt="k.-",
                label=f"$v_\infty = {round(data.low_on.velocity.mean().value, 2)} m/s$, with end plate")
    ax.errorbar(data.high_on.cd, data.high_on.cl, yerr=data.high_on.cl_std, xerr=data.high_on.cd_std, fmt="c.-",
                label=f"$v_\infty = {round(data.high_on.velocity.mean().value, 2)} m/s$, with end plate")

    ax.legend()
    ax.grid()

    ax.set_ylabel("Coefficient of Lift, $C_l$")
    ax.set_xlabel("Coefficient of Drag, $C_d$")

    plt.minorticks_on()

    if directory is not None and fname is not None:
        plt.savefig(path.join(directory, fname))

    plt.show()
