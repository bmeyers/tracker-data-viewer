import marimo

__generated_with = "0.11.3"
app = marimo.App(width="medium")


@app.cell
def _(pd):
    tracker_df = pd.read_csv("9068_tracker_data.csv", index_col=0, parse_dates=[0])
    return (tracker_df,)


@app.cell
def _(pd):
    power_df = pd.read_csv("9068_ac_power_data.csv", index_col=0, parse_dates=[0])
    return (power_df,)


@app.cell
def _(power_df, tracker_df):
    column_names = tracker_df.columns
    power_col_names = power_df.columns
    return column_names, power_col_names


@app.cell
def _(tracker_df):
    unique_dates = (
        tracker_df.index.normalize().unique()
    )  # Normalize to remove time part
    unique_dates_str = [date.strftime("%Y-%m-%d") for date in unique_dates]
    return unique_dates, unique_dates_str


@app.cell
def _(column_names, mo, power_col_names, unique_dates_str):
    col_slct = mo.ui.multiselect(
        column_names,
        label="tracker columns",
        value=["tracker_1.1-101_tracker_angle_trkr_149827"],
    )
    pow_col_slct = mo.ui.multiselect(
        power_col_names,
        label="power columns",
        value=["inverter_module_1.1_ac_power_(kw)_inv_150135"],
    )
    date_slct = mo.ui.date_range(
        start=unique_dates_str[0], stop=unique_dates_str[-1]
    )
    mo.vstack([mo.center(date_slct), mo.hstack([col_slct, pow_col_slct])])
    return col_slct, date_slct, pow_col_slct


@app.cell
def _(col_slct, date_slct, plt, tracker_df):
    if len(col_slct.value) <= 20:
        tracker_df.loc[
            date_slct.value[0] : date_slct.value[1], col_slct.value
        ].plot()
        plt.legend(loc=4)
        plt.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    else:
        tracker_df.loc[
            date_slct.value[0] : date_slct.value[1], col_slct.value
        ].plot(legend=False)
    plt.gcf()
    return


@app.cell
def _(date_slct, plt, pow_col_slct, power_df):
    power_df.loc[date_slct.value[0] : date_slct.value[1], pow_col_slct.value].plot(
        linewidth=1
    )
    plt.legend(loc=4)
    plt.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    plt.gcf()
    return


@app.cell
def _(col_slct, date_slct, tracker_df):
    tracker_df.loc[date_slct.value[0] : date_slct.value[1], col_slct.value]
    return


@app.cell
def _(date_slct, pow_col_slct, power_df):
    power_df.loc[date_slct.value[0] : date_slct.value[1], pow_col_slct.value]
    return


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    return mo, pd, plt


if __name__ == "__main__":
    app.run()
