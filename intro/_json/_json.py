import json
#DOCS: https://docs.python.org/3/library/json.html

# Example Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Serialize dictionary to JSON string
json_str = json.dumps(data, indent=4)
print("Serialized JSON string:")
print(json_str)

# Deserialize JSON string back to Python dictionary
parsed_data = json.loads(json_str)
print("\nDeserialized Python dictionary:")
print(parsed_data)

# Write JSON to a file
with open("data.json", "w") as file_name:
    json.dump(data, file_name, indent=4)

# Read JSON from a file
with open("data.json", "r") as file_name:
    file_data = json.load(file_name)
    print("\nData loaded from file:")
    print(file_data)