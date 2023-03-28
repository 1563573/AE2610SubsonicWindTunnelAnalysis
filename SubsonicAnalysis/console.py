from data import SubsonicWindTunnelData, WindSpeed, EndPlate
import numpy as np
from stats import do_stats
from analysis import calculate
from matplotlib import pyplot as plt

pklFname = "../Data/data.pkl"

dataOrig = SubsonicWindTunnelData.load(pklFname)
data = do_stats(dataOrig)
calculate(data)