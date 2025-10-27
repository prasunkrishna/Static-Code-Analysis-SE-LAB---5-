import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
        
    if not item:
        return
        
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass

def get_qty(item):
    try:
        return stock_data[item]
    except KeyError:
        return 0 

def load_data(file="inventory.json"):
    try:
        
        with open(file, "r", encoding="utf-8") as f:
            global stock_data
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Info: {file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Starting with empty inventory.")
        stock_data = {}

def save_data(file="inventory.json"):
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))

def print_data():
    print("--- Items Report ---")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("------------------")

def check_low_items(threshold=5):
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result

def main():
    load_data() 
    
    add_item("apple", 10)
    add_item("banana", 5)
    
    try:
        add_item("apple", 3)
        remove_item("banana", 2)
        remove_item("orange", 1) 
    except TypeError:
        print("Error: Invalid item type or quantity.")

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Orange stock: {get_qty('orange')}")
    print(f"Low items: {check_low_items()}")
    
    print_data()
    save_data()

    
    print("Inventory check complete.")

if __name__ == "__main__":
    main()