from enum import Enum
from fastapi import FastAPI, Depends
import uvicorn

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users


app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
  admin.router,
  prefix="/admin",
  tags=["admin"],
  dependencies=[Depends(get_token_header)],
  responses={418: {"description": "I'm a teapot"}}
)

@app.get("/")
async def root():
  return {"message": "Hello Bigger Applications!"}

# @app.get("/")
# def read_root():
#   return {"Hello": "World"}

@app.get("/user/{name}")
def read_user_name(name: str):
  return {"name": name}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#   return {"item_id": item_id}

class PayType(str, Enum):
  kakao_pay = "카카오페이"
  naver_pay = "네이버페이"
  toss = "토스"

@app.get("/pay-type/{pay_type}")
async def get_model(pay_type: PayType):
  if pay_type == PayType.kakao_pay:
    return {"pay_type": pay_type, "message": "마음 놓고 금융하다."}

  if pay_type.value == "토스":
    return {"pay_type": pay_type, "message": "금융의 모든것 토스입니다."}

  return {"pay_type": pay_type, "message": "카카오페이, 토스가 아닌 결재 수단을 이용했습니다."}

# 쿼리 매개변수
# : 경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언할 때,
#   쿼리 매개변수로 자동 해석된다.

fake_items_db = [{"name": "Ted"}, {"name": "Robin"}, {"name": "Barney"}]


# @app.get("/items/")
# async def read_item(skip: int, limit: int):
#   return fake_items_db[skip : skip + limit]
# # items/?skip=0&limit=1

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 2):
#   return fake_items_db[skip : skip + limit]
# items/

from typing import Optional

# @app.get("/tv-shows/{tv_show_name}")
# async def read_tv_show(tv_show_name: str, character: Optional[str] = None):
#   if character:
#     return {"tv_show_name": tv_show_name, "character": character}
#   return {"tv_show_name": tv_show_name}
# tv-shows/HIMYM
# tv-shows/HIMYM?character=Ted

# 여러 경로의 매개변수와 쿼리 매개변수를 동시에 선언할 수도 있음
# @app.get("/tv-shows/{tv_show_name}/characters")
# async def read_tv_show_and_character(tv_show_name: str, character: str):
#   return {"tv_show_name": tv_show_name,"character:": character}
# tv-shows/HIMYM/characters?character=Ted

# 쿼리 매개변수의 기본값을 선언하지 않으면, 해당 쿼리 매개변수는 필수 쿼리 매개변수가 된다.
# @app.get("/movies/{movie}")
# async def read_user_item(movie: str, character: str):
#   item = {"movie": movie, "needy": character}
#   return item
# movies/comet => 오류
# movies/comet?character=Kimberley => 정상

from fastapi import Query

# 쿼리 매개변수 제약
# @app.get("/tv-shows/{tv_show_name}")
# async def read_tv_show(tv_show_name: str, character: Optional[str] = Query(None, max_length=10)):
#   if character:
#     return {"tv_show_name": tv_show_name, "character": character}
#   return {"tv_show_name": tv_show_name}

# 정규표현식 제약
# @app.get("/tv-shows/{tv_show_name}")
# async def read_tv_show(tv_show_name: str, character: Optional[str] = Query(None, min_length=3, max_length=10, regex="^fixedquery$")):
#   if character:
#     return {"tv_show_name": tv_show_name, "character": character}
#   return {"tv_show_name": tv_show_name}

# 필수값 지정 : 첫 번째 매개변수로 ...을 입력
# @app.get("/tv-shows/{tv_show_name}")
# async def read_tv_show(tv_show_name: str, character: Optional[str] = Query(..., min_length=3)):
#   if character:
#     return {"tv_show_name": tv_show_name, "character": character}
#   return {"tv_show_name": tv_show_name}

# Query로 쿼리 매개변수를 명시적으로 정의하면 list 값을 받도록 선언하거나 여러 값을 받도록 선언 가능
from typing import List

@app.get("/characters/")
async def read_characters(q: Optional[List[str]] = Query(None)):
  query_items = {"q": q}
  return query_items
# characters/?q=ted&q=robin&q=barney

# Path 클래스를 통한 경로 매개변수 검증
from fastapi import Path

# gt : 큰, ge : 크거나 같은, lt : 작은, le : 작거나 같은
@app.get("/movies/{movie_id}")
async def get_movies(movie_id : int = Path(..., title="The ID of the movie to get", ge=100)):
  results = {"movie_id": movie_id}
  return results

# Request Body
from pydantic import BaseModel

class Drama(BaseModel):
  name: str
  description: Optional[str] = None
  score: float
  channel: Optional[str] = None

@app.post("/dramas/")
async def create_drama(drama: Drama):
  return drama

# 경로 매개변수와 Request Body 동시 선언 가능
# @app.put("/dramas/{drama_id}")
# async def create_drama(drama_id: int, drama: Drama):
#   return {"drama_id": drama_id, **drama.dict()}

# 경로 매개변수, 쿼리 매개변수, Request Body 동시 선언 가능
@app.put("/dramas/{drama_id}")
async def create_drama(drama_id: int, drama: Drama, q: Optional[str] = None):
  result = {"drama_id": drama_id, **drama.dict()}
  if q:
    result.update({"q": q})
  return result

# Response Model

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None
  tags: List[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
  return item

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
  return items[item_id]

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
  return items[item_id]

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}",
    response_model=Item,
        response_model_exclude_unset=True,
        response_model_include=["name", "description"],
        response_model_exclude=["tax"]
)
async def read_item(item_id: str):
  return items[item_id]

##############

from pydantic import EmailStr

class UserIn(BaseModel):
  username: str
  password: str
  email: EmailStr
  full_name: Optional[str] = None

class UserOut(BaseModel):
  username: str
  email: EmailStr
  full_name: Optional[str] = None

# Don't do this in production!
# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#   return user

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
  return user


if __name__ == "__main__":
  uvicorn.run("app.main:app")
