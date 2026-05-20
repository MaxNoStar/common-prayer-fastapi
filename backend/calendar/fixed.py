from datetime import date
from typing import Dict

def get_fixed_feast_dates(year: int) -> Dict[str, date]:
    """
    Returns the fixed feasts and holy days according to the
    1662 Book of Common Prayer, keyed by name.
    """

    return {
        # January
        "the_circumcision_of_our_lord": date(year, 1, 1),
        "epiphany": date(year, 1, 6),
        "the_conversion_of_st_paul": date(year, 1, 25),

        # February
        "the_purification_of_the_virgin_mary": date(year, 2, 2),
        "st_matthias_the_apostle": date(year, 2, 24),

        # March
        "the_annunciation_of_the_blessed_virgin_mary": date(year, 3, 25),

        # April
        "st_mark_the_evangelist": date(year, 4, 25),

        # May
        "st_philip_and_st_james_the_apostles": date(year, 5, 1),

        # June
        "st_barnabas_the_apostle": date(year, 6, 11),
        "the_nativity_of_john_the_baptist": date(year, 6, 24),
        "st_peter_the_apostle": date(year, 6, 29),

        # July
        "st_james_the_greater_apostle": date(year, 7, 25),

        # August
        "st_bartholomew_the_apostle": date(year, 8, 24),

        # September
        "st_matthew_the_apostle_and_evangelist": date(year, 9, 21),
        "st_michael_and_all_the_angels": date(year, 9, 29),

        # October
        "st_luke_the_evangelist": date(year, 10, 18),
        "st_simon_and_st_jude_the_apostles": date(year, 10, 28),

        # November
        "all_saints": date(year, 11, 1),
        "st_andrew_the_apostle": date(year, 11, 30),

        # December
        "st_thomas_the_apostle": date(year, 12, 21),
        "the_nativity_of_our_lord": date(year, 12, 25),
        "st_stephen_the_protomartyr": date(year, 12, 26),
        "st_john_the_evangelist": date(year, 12, 27),
        "holy_innocents": date(year, 12, 28),

    }
