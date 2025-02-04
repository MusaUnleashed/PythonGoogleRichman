import requests

# Base URL of the maze API
BASE_URL = "http://maze-api-url.com"  # Replace with the actual API URL

# Start a new maze
def start_maze():
    response = requests.post(f"{BASE_URL}/")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to start maze")

# Get data for a specific cell
def get_cell_data(maze_id, code):
    response = requests.get(f"{BASE_URL}/{maze_id}/{code}/")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get cell data for code: {code}")

# Solve the maze
def solve_maze(maze_id, total):
    response = requests.post(f"{BASE_URL}/solve/{maze_id}/{total}/")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to solve maze")

# Traverse the maze and collect gold
def traverse_maze(maze_id, start_code):
    visited = set()  # Track visited cells to avoid loops
    total_gold = 0   # Total gold collected
    stack = [(start_code, 0, 0)]  # Stack for DFS: (code, x, y)

    while stack:
        code, x, y = stack.pop()
        if code in visited:
            continue
        visited.add(code)

        # Get cell data
        cell_data = get_cell_data(maze_id, code)
        total_gold += cell_data["score"]

        # Add exits to the stack
        for exit in cell_data["exits"]:
            stack.append((exit["code"], exit["x"], exit["y"]))

    return total_gold

# Main function
def main():
    # Start the maze
    maze_info = start_maze()
    maze_id = maze_info["maze_id"]
    start_code = maze_info["start"]

    # Traverse the maze and collect gold
    total_gold = traverse_maze(maze_id, start_code)

    # Solve the maze
    result = solve_maze(maze_id, total_gold)
    if result["success"]:
        print(f"Maze solved successfully! Total gold: {total_gold}")
    else:
        print("Failed to solve the maze.")

if __name__ == "__main__":
    main()