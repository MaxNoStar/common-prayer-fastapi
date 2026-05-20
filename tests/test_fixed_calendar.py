from backend.calendar.fixed import get_fixed_feast_dates
from datetime import date

def test_get_fixed_feast_dates_current_year():
    dates = get_fixed_feast_dates(2026)
    assert len(dates) == 24
    assert dates["epiphany"] == date(2026, 1, 6)

def test_get_fixed_feast_dates_previous_year():
    dates = get_fixed_feast_dates(2025)
    assert len(dates) == 24
    assert dates["epiphany"] == date(2025, 1, 6)

