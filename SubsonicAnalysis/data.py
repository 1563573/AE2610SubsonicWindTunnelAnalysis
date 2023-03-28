import pandas as pd
from enum import Enum
import numpy as np
from astropy import units as u
import pickle


class EndPlate(Enum):
    OFF = 0,
    ON = 1


class WindSpeed(Enum):
    HIGH = 0,
    LOW = 1


class SubsonicWindTunnelData:
    _df = None
    _sampleNumberKey = None
    _aoaKey = None
    _forceXKey = None
    _forceYKey = None
    _torqueKey = None
    _baratronVoltageKey = None

    _sampleNumberData = {}
    _aoaData = {}
    _forceXData = {}
    _forceYData = {}
    _torqueData = {}
    _baratronVoltageData = {}

    _kdPairs = None

    _csv_fname = None

    def __init__(self, fname=None):
        if fname is None:
            return
        self._csv_fname = fname
        self._prep_data()
        self._init_data_arrays(list(self._kdPairs.values()))
        self._chunk_data()

    def _prep_data(self):
        self._df = pd.read_csv(self._csv_fname)
        keys = self._df.keys()

        self._sampleNumberKey = keys[0]
        self._aoaKey = keys[1]
        self._forceXKey = keys[2]
        self._forceYKey = keys[3]
        self._torqueKey = keys[4]
        self._baratronVoltageKey = keys[5]

        self._init_kd_pairs()

    def _init_kd_pairs(self):
        self._kdPairs = {self._sampleNumberKey: self._sampleNumberData, self._aoaKey: self._aoaData,
                         self._forceXKey: self._forceXData, self._forceYKey: self._forceYData,
                         self._torqueKey: self._torqueData, self._baratronVoltageKey: self._baratronVoltageData}

    def _init_data_arrays(self, *arrays):
        for windSpeed in WindSpeed:
            for endPlate in EndPlate:
                for roundAOA in range(round(self._df[self._aoaKey].min()), round(self._df[self._aoaKey].max()) + 1):
                    for arr in arrays[0]:
                        arr[(windSpeed, endPlate, roundAOA)] = np.empty(0)

    def _datum_appender(self, windSpeed, endPlate, roundAOA, datumIdx):
        for key in self._kdPairs.keys():
            arr = self._kdPairs[key]
            arr[(windSpeed, endPlate, roundAOA)] = np.append(arr[(windSpeed, endPlate, roundAOA)],
                                                             self._df[key][datumIdx])

    def _chunk_data(self):
        roundAOA_prev = -1
        windSpeed = WindSpeed.HIGH
        endPlate = EndPlate.OFF

        length = len(self._df[self._aoaKey])

        for datumIdx in range(length):
            aoa = self._df[self._aoaKey][datumIdx]
            roundAOA = round(aoa)
            if roundAOA != roundAOA_prev:
                if roundAOA < roundAOA_prev:
                    if windSpeed == windSpeed.LOW:
                        windSpeed = windSpeed.HIGH
                        endPlate = endPlate.ON
                    elif windSpeed == windSpeed.HIGH:
                        windSpeed = windSpeed.LOW

            self._datum_appender(windSpeed, endPlate, roundAOA, datumIdx)
            roundAOA_prev = roundAOA

    def _get_data(self, key, windSpeed, endPlate, roundAOA):
        try:
            data = self._kdPairs[key][(windSpeed, endPlate, roundAOA)]
            if len(data) == 0:
                raise KeyError("No data for params")
            return data
        except KeyError:
            return np.empty(0)

    def get_sample_number(self, windSpeed, endPlate, roundAOA):
        return self._get_data(self._sampleNumberKey, windSpeed, endPlate, roundAOA)

    def get_angle_of_attack(self, windSpeed, endPlate, roundAOA):
        return self._get_data(self._aoaKey, windSpeed, endPlate, roundAOA) * u.deg

    def get_force_x(self, windSpeed, endPlate, roundAOA):
        return self._get_data(self._forceXKey, windSpeed, endPlate, roundAOA) * u.N

    def get_force_y(self, windSpeed, endPlate, roundAOA):
        return self._get_data(self._forceYKey, windSpeed, endPlate, roundAOA) * u.N

    def get_torque_z(self, windSpeed, endPlate, roundAOA):
        return self._get_data(self._torqueKey, windSpeed, endPlate, roundAOA) * u.N * u.m
    
    def get_tared_baratron_voltage(self, windSpeed, endPlate, roundAOA):
        return self._get_data(self._baratronVoltageKey, windSpeed, endPlate, roundAOA) * u.V

    def save(self, fname):
        f = open(fname, 'wb')
        pickle.dump(self.__dict__, f)
        f.close()

    @staticmethod
    def load(fname):
        f = open(fname, 'rb')
        tmp_dict = pickle.load(f)
        f.close()

        me = SubsonicWindTunnelData()
        me.__dict__.update(tmp_dict)

        return me
