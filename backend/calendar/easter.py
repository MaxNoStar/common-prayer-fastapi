from dateutil.easter import easter
from datetime import date, timedelta
from typing import Dict


def get_movable_feast_dates(year: int) -> Dict[str, date]:
    """
    Returns the main movable feasts and holy days according to the
    1662 Book of Common Prayer, keyed by name.
    """
    easter_date = easter(year)

    return {
        # Pre-Lent
        "septuagesima": easter_date - timedelta(days=63),
        "sexagesima": easter_date - timedelta(days=56),
        "quinquagesima": easter_date - timedelta(days=49),

        # Lent
        "ash_wednesday": easter_date - timedelta(days=46),
        "first_sunday_in_lent": easter_date - timedelta(days=42),
        "second_sunday_in_lent": easter_date - timedelta(days=35),
        "third_sunday_in_lent": easter_date - timedelta(days=28),
        "fourth_sunday_in_lent": easter_date - timedelta(days=21),
        "fifth_sunday_in_lent": easter_date - timedelta(days=14),   # Passion Sunday
        "palm_sunday": easter_date - timedelta(days=7),

        # Holy Week
        "good_friday": easter_date - timedelta(days=2),

        # Easter Week
        "easter_sunday": easter_date,
        "easter_monday": easter_date + timedelta(days=1),
        "easter_tuesday": easter_date + timedelta(days=2),
        "easter_wednesday": easter_date + timedelta(days=3),
        "easter_thursday": easter_date + timedelta(days=4),
        "easter_friday": easter_date + timedelta(days=5),
        "easter_saturday": easter_date + timedelta(days=6),

        # Ascensiontide & Pentecost
        "rogation_sunday": easter_date + timedelta(days=35),
        "ascension_day": easter_date + timedelta(days=39),
        "whitsunday": easter_date + timedelta(days=49),

        # Trinity
        "trinity_sunday": easter_date + timedelta(days=56),
    }