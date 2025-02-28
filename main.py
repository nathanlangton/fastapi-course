from fastapi import FastAPI
from typing import Optional
from enum import Enum
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return "Hello World!"

# Even though there is another endpoint that has the same schema, if ordered correctly
# We can get the intended functionality by defining it first, 'all' can then be called separate to the other endpoint
# To pass in query params they can just be defined within the function and do not need to be declared anywhere else
# Params can be provided normal python default values making them params optional to the user, This can also be done
# WIth typing "Optional"
@app.get("/blog/all")
def get_all_blog(page = 1, page_size: Optional[int] = 10):
    return {"message": f"All {page_size} Blogs on page {page}"}

# Using Enums we can set specific values allowed into the endpoint, this can be very handy
class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}

# Path Parameters defined with {}
# Type Validation is handled and returns Error Message
# Uses PyDantic Behind the scenes
@app.get("/blog/{id}")
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)