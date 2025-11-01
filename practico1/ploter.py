import matplotlib.pyplot as plt
from cleaner_rotcurves import Rotcurves

def plot_rotcurve_with_ax(ax, index):
    ax.plot(Rotcurves[index].R, Rotcurves[index].Vc, '.')
    ax.set_title(f'Galaxia {index}: {Rotcurves[index].name}')
    ax.set_xlabel('R (Kpc)')
    ax.set_ylabel('Vc (km/s)')
    ax.grid(True, alpha=0.3)

def plot_rotcurve(index):
    fig, ax = plt.subplots()

    plot_rotcurve_with_ax(ax, index)
    return fig, ax
