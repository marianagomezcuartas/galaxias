import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


BASE_PATH = "Rotcurves/"


class Rotcurve:
    def __init__(self, number_dat):
        file_path = f"{number_dat}.dat"
        self.name = self.get_name(file_path)
        self.data = self.get_data(file_path)

        # columnas R (Kpc), Vc (km/s)
        self.R = self.data["R"]
        self.Vc = self.data["Vc"]

        self.data["R"] = self.R
        self.data["Vc"] = self.Vc

        # Calcular máximo global
        max_idx = self.data["Vc"].idxmax()
        self.max = (self.data.loc[max_idx, "R"], self.data.loc[max_idx, "Vc"])

        # Calcular picos locales
        Vc_values = self.data["Vc"].values
        peaks_idx, _ = find_peaks(Vc_values, height=50, distance=5)
        self.peaks = [
            (self.data.loc[idx, "R"], self.data.loc[idx, "Vc"]) for idx in peaks_idx
        ]
        self.num_peaks = len(self.peaks)

    @staticmethod
    def get_name(file_path):
        path = BASE_PATH + file_path
        with open(path, "r") as file:
            first_line = file.readline()

            if len(first_line.split()) == 1:
                name = first_line.split()[0]
            else:
                name = "No name"
        return name

    @staticmethod
    def get_data(file_path):
        path = BASE_PATH + file_path
        with open(path, "r") as file:
            first_line = file.readline()
            # si la primera linea es un solo numero, entonces header = 1,
            # si la primera linea son dos numeros, entonces header = None
            has_header = len(first_line.split()) == 1
            header = 0 if has_header else None

        df = pd.read_csv(path, sep="\s+", header=header, names=["R", "Vc"])
        return df


Rotcurves = {i: Rotcurve(i) for i in range(1, 230)}

# Diccionario con las propiedades de los objetos
rotcurve_properties = {
    i: {
        "name": Rotcurves[i].name,
        "max": Rotcurves[i].max,
        "num_peaks": Rotcurves[i].num_peaks,
        "peaks": Rotcurves[i].peaks,
    }
    for i in range(1, 230)
}

# DataFrame con las propiedades
rotcurve_properties_df = pd.DataFrame.from_dict(rotcurve_properties, orient="index")
