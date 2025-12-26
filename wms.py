import sqlite3

# This function sets up the 'Filing Cabinet' (Database)
def setup_database():
    connection = sqlite3.connect("warehouse_data.db")
    cursor = connection.cursor()
    # Create a table to hold our items
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory 
                      (sku TEXT PRIMARY KEY, name TEXT, quantity INTEGER)''')
    connection.commit()
    connection.close()

def add_item():
    sku = input("Scan/Type SKU: ")
    name = input("Enter Item Name: ")
    qty = int(input("Enter Quantity: "))
    
    conn = sqlite3.connect("warehouse_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO inventory VALUES (?, ?, ?)", (sku, name, qty))
    conn.commit()
    conn.close()
    print("--- Item Saved Successfully! ---")

def view_inventory():
    conn = sqlite3.connect("warehouse_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    print("\n--- Current Stock List ---")
    for item in items:
        print(f"ID: {item[0]} | Name: {item[1]} | Quantity: {item[2]}")
    conn.close()

# Main Menu
setup_database()
while True:
    print("\n1. Add/Update Item  2. View Inventory  3. Exit")
    choice = input("Select an option: ")
    if choice == '1': add_item()
    elif choice == '2': view_inventory()
    elif choice == '3': break