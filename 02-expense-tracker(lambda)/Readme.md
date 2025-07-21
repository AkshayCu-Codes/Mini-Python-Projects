# 💸 Expense Tracker (Lambda Edition)

A simple Python-based Expense Tracker that uses **Lambda functions** for elegant, functional-style logic. Run this in your terminal or host it on **Replit** to track expenses by category, total, and more!

---

## 📦 Features

- Add expenses with amount and category  
- List all expenses  
- Calculate total expenses using `lambda` + `map`  
- Filter expenses by category using `lambda` + `filter`  
- Simple CLI interface (terminal-based)

---

## 📍 How to Run Locally

### ✅ Prerequisites

- Python 3.10 or higher  
- VS Code or any code editor

### 🧑‍💻 Steps

```bash
# 1. Clone the repo or download the code
git clone https://github.com/your-username/expense-tracker-lambda.git
cd expense-tracker-lambda

# 2. Run the script
python app.py
```

You’ll see a menu like this:
```
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
```

---

## ☁️ Host Online with Replit (Free)

You can run this CLI-based tracker online with no setup.

### 🌐 Live App:
[▶ Try on Replit](https://replit.com/@akshaycu11/Expense-TrackerLambda?v=1)

### 🔁 Steps to Host It Yourself on Replit:

1. Visit [https://replit.com](https://replit.com)
2. Click `+ Create` → Select **Python** as the language
3. Name your project: `expense-tracker-lambda`
4. Paste your code into `main.py`
5. Click the **Run** button at the top
6. Your app will launch in the console (left pane)

> ✅ Tip: Share your public Replit URL so others can test it easily!

---

## 🧠 Code Highlights

```python
# Calculate total using lambda + map
def total_expenses(expenses):
    return sum(map(lambda e: e['amount'], expenses))

# Filter expenses by category using lambda + filter
def filter_expenses_by_category(expenses, category):
    return filter(lambda e: e['category'] == category, expenses)
```

---

## 🧠 Tech Stack

- Python 3.10+
- Functional programming concepts
- 100% beginner-friendly

---

## 📈 Project Status

✅ Completed (basic version)  
🚀 Possible Future Enhancements:
- Save expenses to a file
- Export to CSV
- Web UI with Streamlit

---

## 🙌 Author

**Akshay C U**  
[GitHub](https://github.com/AkshayCu-Codes) | [LinkedIn](https://www.linkedin.com/in/akshay-c-0a7106134/)