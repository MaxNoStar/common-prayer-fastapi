from fastapi import APIRouter
from backend.calendar.easter import get_movable_feast_dates

router = APIRouter()

@router.get("/movable-feast/{year}")
async def get_movable_feast(year: int):
    movable_feasts = get_movable_feast_dates(year)
    return movable_feasts