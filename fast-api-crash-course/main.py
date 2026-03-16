from fastapi import FastAPI
app = FastAPI()

items = [
  {'id': 1, 'name':'item 1'},
  {'id': 2, 'name':'item 2'},
]

@app.get("/")
def health_check():
  return{"status": "ok"}
  

@app.get('/items')
def get_items():
  return{"items": items}