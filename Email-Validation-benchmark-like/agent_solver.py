import csv
import os
from email_rules import is_valid_email

DATA_DIR = "data"

lines = []

for case in sorted(os.listdir(DATA_DIR)):
    invalid_ids = []

    with open(os.path.join(DATA_DIR, case, "users.csv")) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not is_valid_email(row["email"]):
                invalid_ids.append(row["id"])

    invalid_ids.sort(key=int)
    lines.append(f"{case}: INVALID_IDS: {','.join(invalid_ids)}")

with open("agent_output.txt", "w") as f:
    f.write("\n".join(lines))
