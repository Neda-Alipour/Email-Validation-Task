import os
import csv
from email_rules import is_valid_email

DATA_DIR = "data"

def parse_agent_output():
    results = {}

    with open("agent_output.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                case_part, ids_part = line.split("INVALID_IDS:")
                case_name = case_part.replace(":", "").strip()
                ids = [int(x) for x in ids_part.strip().split(",") if x]
                results[case_name] = sorted(ids)
            except ValueError:
                return None

    return results

def expected_invalid_ids(case_path):
    expected = []

    with open(os.path.join(case_path, "users.csv")) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not is_valid_email(row["email"]):
                expected.append(int(row["id"]))

    return sorted(expected)

def main():
    agent_results = parse_agent_output()
    if agent_results is None:
        print("FAIL")
        return

    for case in sorted(os.listdir(DATA_DIR)):
        case_path = os.path.join(DATA_DIR, case)

        if case not in agent_results:
            print("FAIL")
            return

        expected = expected_invalid_ids(case_path)
        if agent_results[case] != expected:
            print("FAIL")
            return

    print("PASS")

if __name__ == "__main__":
    main()
