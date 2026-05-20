from fastapi import APIRouter
from backend.calendar.easter import get_movable_feast_dates
from backend.calendar.fixed import get_fixed_feast_dates

router = APIRouter()


# Return all movable feast dates for a given year
@router.get("/movable-feasts/{year}")
async def get_movable_feast(year: int):
    movable_feasts = get_movable_feast_dates(year)
    return movable_feasts

# Return all fixed feast dates for a given year
@router.get("/fixed-feasts/{year}")
async def get_fixed_feasts(year: int):
    fixed_feasts = get_fixed_feast_dates(year)
    return fixed_feasts
