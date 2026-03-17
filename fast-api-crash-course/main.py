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


@app.get('/items/{item_id}')
def get_item(item_id: int):
  for item in items:
    if item['id'] == item_id:
      return item
  return{'error': "Item not found"}


@app.get('/items/')
def get_items(skip: int = 0, limit: int = 1):
  return{"skip": skip, "limit": limit}

@app.post('/items')
def add_item(item: dict):
  items.append(item)
  return items

