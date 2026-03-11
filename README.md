# ☕ Shrutika's Cafe Ordering System

A simple **Python command-line application** that simulates a café ordering and checkout system.
The program displays a café menu, allows users to place orders, generates a receipt, and processes payment using **card or cash**.

---

## 📌 Features

* Display formatted café menu with categories:

  * Espresso
  * Hot Drinks
  * Quick Bites
* Allow customers to order multiple items
* Calculate:

  * Item totals
  * Subtotal
  * 8% gratuity
  * Final total
* Generate a detailed receipt
* Payment system:

  * **Card payment** → confirms payment success
  * **Cash payment** → accepts amount and calculates change
* Input validation for menu items and quantities

---

## 🛠 Technologies Used

* **Python**
* Dictionaries for menu storage
* Loops for ordering system
* Conditional statements for payment processing
* Basic formatting for receipt display

```


## ▶️ How to Run the Program

1. Clone the repository or download the code.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the program:

```bash
python cafe.py
```

---

## 🧾 Example Flow

1. The program displays the café menu.
2. The user enters items they want to order.
3. The system asks for the quantity of each item.
4. After ordering, a receipt is generated with totals.
5. The user chooses a **payment method**:

   * Card → Payment successful
   * Cash → Enter amount and receive change.

---

## 💡 Example Output

```
*************** RECEIPT ***************

ITEM                QTY   PRICE      TOTAL
Latte               2     $2.50      $5.00
Bagel               1     $2.00      $2.00

SUBTOTAL: $7.00
GRATUITY (8%): $0.56
FINAL TOTAL: $7.56

Payment Method: cash
Cash received: $10.00
Change returned: $2.44
```

---

## 🚀 Future Improvements

Possible enhancements for this project:

* Save receipts to a file
* Add menu selection numbers
* Track daily sales
* Create a graphical interface (GUI)
* Store orders in a database

---

## 👩‍💻 Author

**Shrutika More**

This project was created as a learning exercise to practice **Python programming, logic building, and basic system design**.
