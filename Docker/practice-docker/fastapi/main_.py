# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# # @app.get("/items/{item_id}")
# # async def read_item(item_id: int):
# #     return {"item_id": item_id}

# from enum import Enum

# from fastapi import FastAPI

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# from fastapi import FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    name = item.name
    price = item.price
    return {"name": name, "price": price}

# from typing import Union

# from fastapi import FastAPI, Query
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import Union

# from fastapi import FastAPI, Query
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         Union[str, None],
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^fixedquery$",
#             deprecated=True,
#         ),
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# from fastapi import FastAPI, Path, Query
# from typing_extensions import Annotated

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import Union

# from fastapi import Body, FastAPI
# from pydantic import BaseModel
# from typing_extensions import Annotated

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)],
#     q: Union[str, None] = None,
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import List, Union

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     images: Union[List[Image], None] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# from fastapi import FastAPI, File, UploadFile
# from typing_extensions import Annotated

# # app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

# from fastapi import FastAPI, File, Form, UploadFile
# from typing_extensions import Annotated

# app = FastAPI()


# @app.post("/files/")
# async def create_file(
#     file: Annotated[bytes, File()],
#     fileb: Annotated[UploadFile, File()],
#     token: Annotated[str, Form()],
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#     }

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse


# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name


# app = FastAPI()


# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )


# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {"foo": "The Foo Wrestlers"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}

# from typing import Any, List, Union

# @app.get("/items/", response_model=List[Item])
# async def read_items() -> Any:
#     return [
#         {"name": "Portal Gun", "price": 42.0},
#         {"name": "Plumbus", "price": 32.0},
#     ]

from typing import Union

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons