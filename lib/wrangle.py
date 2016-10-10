import pandas as pd
import pdb

def create_revenue_frame(timecards, employees, rates, pl):

    def get_revenue_column(row):
        gs_rate = rates[(rates["gs"] == int(row["Grade"]) ) & (rates["pl"] == pl)].rate.values[0]
        try:
            return gs_rate * row["hours_spent"]
        except:
            return

    revenue_frame = pd.merge(timecards, employees[["Tock ID","Grade"]], how="left", left_on="user", right_on="Tock ID")
    revenue_frame["revenue"] = revenue_frame.apply(lambda x: get_revenue_column(x), axis=1)
    return revenue_frame

def get_revenue_data(revenue_frame):
    hours = revenue_frame.hours_spent.sum()
    revenue = revenue_frame.revenue.sum()
    return {"hours": hours, "revenue": revenue}
