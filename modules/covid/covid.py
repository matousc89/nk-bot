from datetime import date, timedelta
import os

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import matplotlib.ticker as ticker

def download_data(data_path):
    URL_C19 = 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakazeni-vyleceni-umrti-testy.csv'
    URL_HOS = 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.csv'
    dataframe_c19 = pd.read_csv(URL_C19, index_col="datum")
    dataframe_hos = pd.read_csv(URL_HOS, index_col="datum")
    dataframe = dataframe_c19.join(dataframe_hos)
    dataframe.to_pickle(data_path)
    return dataframe

def handle_fig(func):
    def wrapper(*args, **kwargs):
        fig = func(*args, **kwargs)
        if "filename" in kwargs:
            filepath = os.path.join(FIG_PATH, kwargs["filename"])
            fig.savefig(filepath, dpi=100)
        if not kwargs["display"]:
            plt.close(fig)
            fig.clf()
    return wrapper

@handle_fig
def plot_data1(dataframe, **kwargs):
    FIGSIZE = (10, 5)
    WINDOWNAME = "Test 1"
    tick_spacing = 50
    fig = plt.figure(WINDOWNAME, figsize=FIGSIZE)
    ax = plt.gca()
    ax.plot(dataframe.index, dataframe["prirustkovy_pocet_nakazenych"], label="Nově nakažení")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for name, date in DATES.items():
        plt.axvline(dataframe.index.get_loc(date), color="r")
    plt.xticks(rotation=90)
    plt.grid()
    plt.tight_layout()
    return fig

@handle_fig
def plot_data2(dataframe, filename=False, display=False):
    FIGSIZE = (12, 4)
    WINDOWNAME = "Test 2"
    subset = dataframe.loc[dataframe.index > DATES["breakpoint1"]]
    tick_spacing = 1
    fig = plt.figure(WINDOWNAME, figsize=FIGSIZE)
    ax = plt.gca()
    ax.plot(subset.index, subset["kumulativni_pocet_umrti"], label="Kumulativní počet úmrtí")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.xticks(rotation=90)
    plt.grid()
    plt.tight_layout()
    return fig


FIG_PATH = os.path.join("figs")

DATES = {
    "breakpoint1": "2021-10-01",
    "the_other_day": "2020-06-25",
}

if __name__ == "__main__":

    dataframe = download_data(data_path="data.pckl")

    plot_data1(dataframe, display=True, filename="plot1.png")
    plot_data2(dataframe, display=True)

    plt.show()




