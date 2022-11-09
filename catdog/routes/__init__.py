from typing import List
from fastapi import APIRouter

from catdog.models import Owner

router = APIRouter(prefix="/owners", tags=["owners"])

owners = [Owner(id=1, name="Derk")]


@router.get("/", response_model=List[Owner])
async def list_owners() -> List[Owner]:
    return owners

@router.get("/{owner_id}", response_model=Owner)
async def get_owner(owner_id: int) -> Owner:
    return next(item for item in owners if item.id == owner_id)