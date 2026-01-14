import os
import csv
import random

BASE_DIR = "data"
CASES = 3
RANDOM_SEED = 42

def generate_email(valid=True):
    if valid:
        return f"user{random.randint(1,100)}@example.com"
    else:
        invalid_formats = [
            "userexample.com",
            "user@.com",
            "user@com",
            "user@exam_ple.com",
            "user@exam!ple.com"
        ]
        return random.choice(invalid_formats)

def setup_environment():
    random.seed(RANDOM_SEED)
    os.makedirs(BASE_DIR, exist_ok=True)
    
    for i in range(1, CASES + 1):
        case_dir = os.path.join(BASE_DIR, f"case_{i:02}")
        os.makedirs(case_dir, exist_ok=True)

        users = []
        for user_id in range(1, 8):
            is_valid = random.choice([True, False])
            users.append({
                "id": user_id, 
                "name": f"User{user_id}", 
                "email": generate_email(is_valid)
                })
        
        csv_path = os.path.join(case_dir, "users.csv")
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
            writer.writeheader()
            writer.writerows(users)

print("Environment setup complete.")

if __name__ == "__main__":
    setup_environment()