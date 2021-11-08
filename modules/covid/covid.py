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

def get_actual_data():
    """
    :return: (bool, dataframe) - bool value represent whether the data are new
    """
    DATA_PATH = "data.pckl"
    yesterday_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    # try to load data
    try:
        dataframe = pd.read_pickle(DATA_PATH)
    except:
        return True, download_data(DATA_PATH)

    if dataframe.index[-1] == yesterday_date:
        # data are actual, but already posted
        return False, dataframe
    else:
        dataframe = download_data(DATA_PATH)
        if dataframe.index[-1] == yesterday_date:
            # new data are actual, should be posted
            return True, dataframe
        else:
            # new data are not actual
            return False, dataframe

def plot_data(dataframe, display=False):
    FIGSIZE = (10, 5)
    tick_spacing = 50
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(*FIGSIZE)
    ax.plot(dataframe.index, dataframe["prirustkovy_pocet_nakazenych"], label="Nově nakažení")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid()
    filepath = os.path.join("modules", "covid", "figs", "plot1.png")
    fig.savefig(filepath, dpi=100)
    if display:
        plt.show()
    plt.clf()


def make_covid_report_when_new():
    new, dataframe = get_actual_data()
    plot_data(dataframe, display=False)
    return new


if __name__ == "__main__":
    new, dataframe = get_actual_data()
    plot_data(dataframe, display=True)




