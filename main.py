from fastmcp import FastMCP


mcp=FastMCP("2nd-Remote-Server")

balance=10000
total_expense=0
expense_dict={}

# Global dictionary aur variables
expense_dict = {}
total_expense = 0.0
balance = 100000.0   # maan lo initial balance

@mcp.tool
def Add_Expense(item_name: str, price: float):
    """Add expense in diary"""
    global total_expense, balance, expense_dict
    
    # expense_dict me item store karna
    expense_dict[item_name] = price
    
    # total_expense update karna
    total_expense += price
    
    # balance update karna
    balance -= price
    
    return {"item": item_name, "price": price, "total_expense": total_expense, "balance": balance}


@mcp.tool
def check_balance() -> float:
    """Check remaining balance"""
    global balance
    return balance




if __name__ == "__main__":
    mcp.run()

# uv run fastmcp run main.py
# uv run fastmcp  inspect main.py
#uv run fastmcp dev inspector main.py
