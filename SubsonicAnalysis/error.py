from os import path
import numpy as np
from pandas import DataFrame


def tabulate(data, directory=None, fname=None):
    dataArr = [data.high_on, data.high_off, data.low_on, data.low_off]
    labels = ["high on", "high off", "low on", "low off"]
    categories = ["\\alpha (\\degree)", "C_l","C_d","C_m"]
    aoa = []
    cl = []
    cd = []
    cm = []
    for d in dataArr:
        aoa.append(d.aoa.value)
        cl.append(d.cl_std)
        cd.append(d.cd_std)
        cm.append(d.cm_std)

    columns = []
    for c in categories:
        columns.append(f"\\({c}\\)")

    for i in range(len(labels)):
        l = labels[i]
        df = DataFrame(np.vstack((aoa[i], cl[i], cd[i], cm[i])).T, columns=columns)
        if directory is not None and fname is not None:
            with open(path.join(directory, f"{fname}{l.replace(' ', '')}.tex"), 'w') as f:
                f.write(df.to_latex(index=False, escape=False))
