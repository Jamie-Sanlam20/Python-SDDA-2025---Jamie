# Mini Inventory Management and Filtering Challenge

This exercise guides you through several tasks in Python, starting with an initial inventory, then performing inventory operations and filtering based on conditions. Emojis are added to keep things fun!

---

## Initial Inventory

Begin with an initial inventory list:

```python
inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.20}
]
```

---

## Task 1: Add a New Product

**Instructions:**

- Prompt the user for the product name, quantity, and price.
- Create a new product dictionary and add it to the inventory.
- _Fun Tip:_ For an "Orange", consider using "Orange 🍊"!

**Example Scenario:**

- **User Input:**
  ```
  What is the product name? Orange 🍊
  What is the quantity? 10
  What is the price? 0.60
  ```
- **Expected Output:**

  ```
  {'name': 'Orange 🍊', 'quantity': 10, 'price': 0.6}

  ```

  ````
  Updated Inventory: [{'name': 'Apple 🍎', 'quantity': 30, 'price': 0.5}, {'name': 'Banana 🍌', 'quantity': 20, 'price': 0.2}, {'name': 'Orange 🍊', 'quantity': 10, 'price': 0.6}]
  ```
  ````

---

## Task 2: Update an Existing Product

**Instructions:**

- Prompt for the product name, additional quantity, and new price.
- Loop through the inventory; if the product exists, update its quantity and price.

**Example Scenario:**

- **Initial Inventory:**
  ```python
  [{'name': 'Apple 🍎', 'quantity': 30, 'price': 0.5}, {'name': 'Banana 🍌', 'quantity': 20, 'price': 0.2}]
  ```
- **User Input:**
  ```
  Enter product name to update: Apple 🍎
  Enter additional quantity: 40
  Enter new price: 0.4
  ```
- **Expected Output:**
  ```
  Updated Apple 🍎 successfully! 🎉
  Updated Inventory: [{'name': 'Apple 🍎', 'quantity': 70, 'price': 0.4}, {'name': 'Banana 🍌', 'quantity': 20, 'price': 0.2}]
  ```

---

## Task 3: Add or Update Using a `for-else` Construct

**Instructions:**

- Ask the user for product details.
- Use a `for-else` loop: if the product exists, update it; if not, add it to the inventory.

**Example Scenario:**

- **Initial Inventory:**
  ```python
  [{'name': 'Apple 🍎', 'quantity': 70, 'price': 0.4}, {'name': 'Banana 🍌', 'quantity': 20, 'price': 0.2}]
  ```
- **User Input:**
  ```
  Enter product name: Grape 🍇
  Enter quantity: 15
  Enter price: 1.2
  ```
- **Expected Output:**
  ```
  Added new product Grape 🍇! 🎉
  Updated Inventory: [{'name': 'Apple 🍎', 'quantity': 70, 'price': 0.4}, {'name': 'Banana 🍌', 'quantity': 20, 'price': 0.2}, {'name': 'Grape 🍇', 'quantity': 15, 'price': 1.2}]
  ```
