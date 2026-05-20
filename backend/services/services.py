from fastapi import HTTPException
from dateutil.easter import easter
from datetime import date

# Get the date of Easter for a given year
def get_easter_date(year: int) -> date:
    return easter(year)

