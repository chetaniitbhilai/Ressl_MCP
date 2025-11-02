from fastapi import FastAPI
from pydantic import BaseModel
from tools.tool import search_keyword_in_file

app = FastAPI()

class SearchRequest(BaseModel):
    file_path: str
    keyword: str

@app.get("/")
def read_root():
    return {"message": "MCP Server is running"}

@app.post("/search")
def search_file(req: SearchRequest):
    result = search_keyword_in_file(req.file_path, req.keyword)
    return {"results": result}
