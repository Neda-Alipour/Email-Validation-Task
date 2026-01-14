def read_agent_output(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
    return content

def validate_output(agent_output):
    expected_invalid_ids = {'2', '4', '6'}
    # Extract the IDs from the agent's output
    if "INVALID_IDS:" in agent_output:
        ids_part = agent_output.split("INVALID_IDS:")[1].strip()
        agent_ids = set(map(str.strip, ids_part.split(',')))
        if agent_ids == expected_invalid_ids:
            return True
    return False

def main():
    # Path to the agent's output file
    agent_output_path = './agent_output.txt'
    
    agent_output = read_agent_output(agent_output_path)
    if validate_output(agent_output):
        print("PASS")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()