import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datavis_fun import *


# Percentiles for recency column
def get_rfm_bin(
    df,
    r_vals: str,
    fr_vals: str,
    mon_vals: str,
    thr_df=None,
    thr_r=None,
    thr_f=None,
    thr_m=None,
):
    """
    Returns dataframe with R, F, M, RFM scores
    Variables:
     - df: dataframe for which you want to calculate R, F, M and RFM scores
     - r_vals: name of a column with recency values
     - fr_vals: name of a column with frequency values
     - mon_vals: name of a column with monetary values
    Optional Variables:
    - If you want to get quantile thresholds from other dataframe, you can specify dataframe and column names for recency/frequency/monetary values
      under thr_df, thr_r, thr_f, thr_m variables
    """
    rfm_df = df.copy()
    if thr_df is None and thr_r is None and thr_f is None and thr_m is None:
        print("Getting threshold quantile values from CURRENT dataframe")
        rfm_df["R"] = assign_rfm_rank(df=rfm_df, col=r_vals, type="r")
        rfm_df["F"] = assign_rfm_rank(df=rfm_df, col=fr_vals, type="fm")
        rfm_df["M"] = assign_rfm_rank(df=rfm_df, col=mon_vals, type="fm")
        rfm_df["RFM"] = rfm_df.R + rfm_df.F + rfm_df.M
        rfm_df["RFM"] = rfm_df["RFM"].astype(int)

    elif (
        thr_df is not None
        and not thr_df.empty
        and thr_r is not None
        and thr_f is not None
        and thr_m is not None
    ):
        print("Getting threshold quantile values from OTHER dataframe")
        rfm_df["R"] = assign_rfm_rank(df=thr_df, col=thr_r, type="r")
        rfm_df["F"] = assign_rfm_rank(df=thr_df, col=thr_f, type="fm")
        rfm_df["M"] = assign_rfm_rank(df=thr_df, col=thr_m, type="fm")
        rfm_df["RFM"] = rfm_df.R + rfm_df.F + rfm_df.M
        rfm_df["RFM"] = rfm_df[rfmcolname].astype(int)

    return rfm_df


def assign_rfm_rank(df, col, type) -> list:
    """
    Assigns R/F/M score based on a 33th and 66th percentile of a provided column
    Returns assigned values as a list

    Variables:
    - df: dataframe
    - col: name of a column you want to assign R/F/M score to
    - type: takes only two values - 'fm' or 'r';
      In case of providing 'r' for values below 33th percentile the '3' score will be given, score '1' will be assigned to values over 66th percentile;
      In case of providing 'fm' for values below 33th percentile the '1' score will be given, score '3' will be assigned to values over 66th percentile;

    """
    p33 = np.percentile(df[col], 33)
    p66 = np.percentile(df[col], 66)

    if type == "fm":
        conditions = [df[col] < p33, df[col] > p66, (df[col] >= p33) & (df[col] <= p66)]
        choices = ["1", "3", "2"]
    elif type == "r":
        conditions = [df[col] < p33, df[col] > p66, (df[col] >= p33) & (df[col] <= p66)]
        choices = ["3", "1", "2"]
    else:
        raise ValueError("Invalid type. Must be 'fm' or 'r'.")

    new_col = np.select(conditions, choices)
    return new_col.astype(str)


def plot_RF(
    data,
    freqvals_c: str,
    rvals_c: str,
    fs=(10, 10),
    ax=None,
    myfont="Bahnschrift",
    ticksize: int = 10,
    axlabsize: int = 10,
    ptitlesize: int = 15,
):
    """
    Creates scatterplot for RF values (recency values are on y-axis)
    Variables:
    - data: dataframe
    - freqvals_c: name of a column with frequency values
    - rvals_c: name of a columns with recency values
    - ax: allows you to place the plot as a part of other figure
    """
    if ax == None:
        fig, ax = plt.subplots(figsize=fs)
    else:
        fig = ax.get_figure()
    # Graph itself
    ax.scatter(data[freqvals_c], data[rvals_c], color="#FEB941", alpha=0.5)
    # Some formatting
    fig.set_facecolor(BG_WHITE)
    ax.set_facecolor(BG_WHITE)
    for tick in ax.get_xticklabels():
        tick.set_fontname(myfont)
    for tick in ax.get_yticklabels():
        tick.set_fontname(myfont)
    ax.ticklabel_format(style="plain")

    ax.set_title("RF", fontfamily=myfont, fontsize=ptitlesize)
    ax.grid(axis="x", linestyle=":")
    ax.set_xlabel("Frequency Values", fontsize=axlabsize)
    ax.set_ylabel("Recency Values", fontsize=axlabsize)
    ax.tick_params(axis="both", labelsize=ticksize)
    ax.get_xaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
    )
    fig.tight_layout()


def plot_RM(
    data,
    monvals_c: str,
    rvals_c: str,
    fs=(10, 10),
    ax=None,
    myfont="Bahnschrift",
    ticksize: int = 10,
    axlabsize: int = 10,
    ptitlesize: int = 15,
):
    """
    Creates scatterplot for RM values (recency values are on y-axis)
    Variables:
    - data: dataframe
    - monvals_c: name of a column with monetary values
    - rvals_c: name of a columns with recency values
    - ax: allows you to place the plot as a part of other figure
    """
    if ax == None:
        fig, ax = plt.subplots(figsize=fs)
    else:
        fig = ax.get_figure()
    # Graph itself
    ax.scatter(data[monvals_c], data[rvals_c], color="#FF0080", alpha=0.5)
    # Some formatting
    fig.set_facecolor(BG_WHITE)
    ax.set_facecolor(BG_WHITE)
    for tick in ax.get_xticklabels():
        tick.set_fontname(myfont)
    for tick in ax.get_yticklabels():
        tick.set_fontname(myfont)
    ax.ticklabel_format(style="plain")

    ax.set_title("RM", fontfamily=myfont, fontsize=ptitlesize)
    ax.grid(axis="x", linestyle=":")
    ax.set_xlabel("Monetary Values", fontsize=axlabsize)
    ax.set_ylabel("Recency Values", fontsize=axlabsize)
    ax.tick_params(axis="both", labelsize=ticksize)
    ax.get_xaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
    )
    fig.tight_layout()
