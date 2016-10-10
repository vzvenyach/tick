import sys
import pdb

from lib import getdata, wrangle

if __name__ == "__main__":
    try:
        start_date = sys.argv[1]
        project_id = sys.argv[2]
        pl = sys.argv[3]
    except:
        sys.exit("Not enough data")

    cards = getdata.get_tock_timecards_data(start_date, project_id)
    employees = getdata.get_employees()
    rates = getdata.get_rates()

    df = wrangle.create_revenue_frame(cards, employees, rates, pl)
    results = wrangle.get_revenue_data(df)

    results["start_date"] = start_date
    results["project_id"] = project_id
    results["project_name"] = df[df["project_id"] == int(project_id)].project_name.values[0]
    print(results)
