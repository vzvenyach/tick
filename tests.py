from lib import getdata, wrangle
import vcr

@vcr.use_cassette('fixtures/vcr_cassettes/timecards.yaml')
def test_get_tock_timecards_data():
    assert len(getdata.get_tock_timecards_data("2016-10-02", 415)) == 4

def test_get_rates():
    rates = getdata.get_rates()
    assert len(rates) == 9

def test_get_employees():
    employees = getdata.get_employees()
    assert len(employees) == 321

@vcr.use_cassette('fixtures/vcr_cassettes/timecards.yaml')
def test_create_revenue_frame():
    timecards = getdata.get_tock_timecards_data("2016-10-02", 415)
    employees = getdata.get_employees()
    rates = getdata.get_rates()
    results = wrangle.create_revenue_frame(timecards, employees, rates, "Acq")
    assert 'revenue' in results.columns.values

@vcr.use_cassette('fixtures/vcr_cassettes/timecards.yaml')
def test_get_revenue():
    timecards = getdata.get_tock_timecards_data("2016-10-02", 415)
    employees = getdata.get_employees()
    rates = getdata.get_rates()
    revenue_frame = wrangle.create_revenue_frame(timecards, employees, rates, "Acq")
    assert wrangle.get_revenue_data(revenue_frame) == {"hours": 28.75, "revenue": 7853.75}
