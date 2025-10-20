
import json
def save_transactions(transactions):
    with open("transactions.json","w") as file:
        json.dump(transactions,file)
def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
def calculate_balance(transactions):
     balance=0
     for transaction in transactions:
              if transaction["type"]=="income":
                balance+=transaction["amount"]
              elif transaction['type']=="expense":
                balance-= transaction["amount"]
     return balance           
def add_transaction(transactions,trans_type,amount,category,note=""):
    if not category.strip():
        return transactions
    
    transaction={
    'type': trans_type,
    'amount': amount,
    "category": category.strip(),
    "note":note.strip() or "No note"

    }
    transactions.append(transaction)
    save_transactions(transactions)
    return transactions




def delete_transaction(transactions, index_to_delete):
    if 0<=index_to_delete<=len(transactions):
        transactions.pop(index_to_delete)
        save_transactions(transactions)
    return transactions


def edit_transaction(transactions,trans_type,index,new_amount,new_category,new_note):
    if 0<=index<=len(transactions):
        transactions[index]['type']=trans_type
        transactions[index]['amount']= new_amount
        transactions[index]['category']=new_category
        transactions[index]['note']=new_note
        save_transactions(transactions)
    return transactions