import pandas as pd
import matplotlib.pyplot as plt

def show_pie_chart():
    
    data = pd.read_csv("data.csv")
    
    expense_data = data[data["Type"] == "expense"]
    
    category_totals = expense_data.groupby("Category")["Amount"].sum()
    
    plt.pie(category_totals,
            labels=category_totals.index,
            autopct='%1.1f%%'
            )
    
    plt.title("Expense Distribution")
    plt.show()
    
    
    
def show_bar_chart():
    
    data = pd.read_csv("data.csv")
    
    expense_data = data[data["Type"] == "expense"]
    
    category_totals = expense_data.groupby("Category")["Amount"].sum()
    
    plt.figure(figsize=(8, 5))
    
    plt.bar(category_totals.index,
            category_totals.values
            )
    
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expenses by Category")
    plt.show()    
    
    

def show_monthly_trend():
    
    data = pd.read_csv("data.csv")
    
    data["Date"] = pd.to_datetime(data["Date"])
    
    expense_data = data[data["Type"] == "expense"]
    
    monthly_expense = expense_data.groupby(expense_data["Date"].dt.month)["Amount"].sum()
    
    plt.figure(figsize=(8, 5))
    
    plt.plot(monthly_expense.index, 
             monthly_expense.values,
             marker='o'
            )
    
    plt.xlabel("Month")
    plt.ylabel("Expense")
    plt.title("Monthly Expense Trend")
    plt.show()
    
    