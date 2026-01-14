import os
import csv

DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "users.csv")

def setup_environment():
    os.makedirs(DATA_DIR, exist_ok=True)

    users = [
        {"id": 1, "name": "Alice", "email": "alice@gmail.com"},
        {"id": 2, "name": "Bob", "email": "bob-at-gmail.com"},
        {"id": 3, "name": "Carol", "email": "carol@yahoo.com"},
        {"id": 4, "name": "Dan", "email": "dan@"},
        {"id": 5, "name": "Eve", "email": "eve@outlook.com"},
        {"id": 6, "name": "Frank", "email": "frankgmail.com"},
    ]

    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
        writer.writeheader()
        writer.writerows(users)

    print("Environment setup complete.")

if __name__ == "__main__":
    setup_environment()