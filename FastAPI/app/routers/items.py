from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
prefix="/items",
tags=["items"],
dependencies=[Depends(get_token_header)],
responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
  return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
  if item_id not in fake_items_db:
    raise HTTPException(status_code=404, detail="Item not found")
  return {"name": fake_items_db[item_id]["name"], "item_id": item_id}