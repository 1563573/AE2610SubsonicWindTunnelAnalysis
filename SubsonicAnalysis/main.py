from data import SubsonicWindTunnelData
from stats import do_stats
from analysis import calculate
from plotting import plot_aoa_vs_cl, plot_aoa_vs_cd, plot_aoa_vs_cm, plot_drag_polar, plot_17aoa
import error

csvFname = "../Data/a07x_windtunnel_data.csv"
pklFname = "../Data/data.pkl"

pltSavePath = "../Plots"

# data = SubsonicWindTunnelData(csvFname)
# data.save(pklFname)

dataOrig = SubsonicWindTunnelData.load(pklFname)

data = do_stats(dataOrig)
calculate(data)

plot_aoa_vs_cl.plot(data, pltSavePath, "cl.pdf")
plot_aoa_vs_cd.plot(data, pltSavePath, "cd.pdf")
plot_aoa_vs_cm.plot(data, pltSavePath, "cm.pdf")
plot_drag_polar.plot(data, pltSavePath, "dragPolar.pdf")

error.tabulate(data, "../Report/tables", "forceTorqueError_Tabular_")

plot_17aoa.plot(dataOrig, pltSavePath, "aoa17.pdf")