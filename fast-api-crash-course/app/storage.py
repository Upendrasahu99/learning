# in porduction may be we use sql or sql model or some ORM but here for demo we are using json store

from pathlib import Path
import json

DATA_DIR = Path("data") # it will create file if required
DATA_FILE = DATA_DIR / "issues.json" # we can create separate json file for each resource instead of issue

def load_data():
  if DATA_FILE.exists():
    with open(DATA_FILE, "r") as f:
      content = f.read()
      if content.strip(): # return whide space
        return json.loads()
  return []  
    

def save_data(data):
  DATA_DIR.mkdir(parents=True, exist_ok=True) #create if not exist
  with open(DATA_FILE, "w") as f:
    json.dumps(data, f, indent=2)
