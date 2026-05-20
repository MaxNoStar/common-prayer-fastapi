from datetime import date
from dateutil.easter import easter
from backend.calendar.easter import get_movable_feast_dates

# Test verifies that current year for Easter Sunday is correct
def test_get_movable_feast_dates_current_year():
    data = get_movable_feast_dates(2026)
    assert data["easter_sunday"] == date(2026, 4, 5)

# Test verifies that current year for Ash Wednesday is correct
def test_get_movable_feast_dates_current_year_ash_wednesday():
    data = get_movable_feast_dates(2026)
    assert data["ash_wednesday"] == date(2026, 2, 18)

# Test verifies that certain keys are present in the data
def test_get_movable_feast_dates_keys():
    data = get_movable_feast_dates(2026)
    assert "septuagesima" in data