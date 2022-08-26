import json
from pathlib import Path

a = {1: "あ"}

with open(f"{Path(__file__).resolve().parent}/test", "w") as f:
    json.dump(a, f)
