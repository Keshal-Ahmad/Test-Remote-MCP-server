from fastmcp import FastMCP


mcp=FastMCP("2nd-Remote-Server")

balance=10000
total_expense=0
expense_dict={}

# Global dictionary aur variables
expense_dict = {}
total_expense = 0.0
balance = 100000.0   # maan lo initial balance
debt=0.0

@mcp.tool
def Add_Expense(item_name: str, price: float):
    """Add expense in diary"""
    global total_expense, balance, expense_dict,debt
    
    # expense_dict me item store karna
    expense_dict[item_name] = price
    
    # total_expense update karna
    total_expense += price
    
    # balance update karna
    balance -= price

    if balance < 0:
        debt+=abs(balance)
        balance=0

      
    return {"item": item_name, "price": price, "total_expense": total_expense, "balance": balance,"debt":debt}


@mcp.tool
def check_balance() -> float:
    """Check remaining balance"""
    global balance

    return balance

@mcp.resource("keshal://MCP-2")
def info():
    data={
        "code":15-10-2004,
        "Name":"Keshal Ahmad",
        "Type":"MCP_server"
    }

    return data


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

# uv run fastmcp run main.py
# uv run fastmcp  inspect main.py
#uv run fastmcp dev inspector main.py
