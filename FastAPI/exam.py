from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int, request: Request):
  client_host = request.client.host
  return {"client_host": client_host, "movie_id": movie_id}
# http://127.0.0.1:8000/movies/123


if __name__ == "__main__":
  uvicorn.run("exam:app")



# · Request Object로 접근할 수 있는 요소:

# - method
# ex) request.method
# - URL

# ex) request.url

# ex) request.url.path

# ex) request.url.port

# - Headers

# ex) request.headers['content-type']

# - Query Parameters

# ex) request.query_params['search']

# - Path Parameters

# ex) request.path_params['username']

# - Client Address

# ex) request.client.host

# - Cookies

# ex) request.cookies.get('mycookie')

# - Body

# ex) bytes: await request.body()

# ex) form data or multipart: await request.form()

# ex) json: await request.json()

# - RequestFiles

# - Application

# - Other State