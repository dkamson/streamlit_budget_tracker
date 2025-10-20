import streamlit as st
import pandas as pd
from logic import load_transactions,calculate_balance,add_transaction,delete_transaction,edit_transaction




@st.dialog("Edit a Transaction")
def show_edit_dialog(index):
    transaction=st.session_state.transactions[index]

    type_options=["Income", "Expense"]
    current_type_index=type_options.index(transaction['type'].title())
    with st.form("edit_form_in_dialog"):
        st.write(f"Editing Transaction {trans_to_edit_string} ")
        new_type= st.selectbox("Transaction type",options=type_options,index=current_type_index)
        amount=st.number_input("Amount",value=transaction['amount'], min_value=0.01,format="%.2f")
        category=st.text_input("Category",value=transaction['category'], placeholder="eg., Job, Groceries")
        note=st.text_area("Note(Optional)",value=transaction['note'])

        col_save,col_cancel=st.columns(2)
        with col_save:
            if st.form_submit_button("Save Changes"):
                edit_transaction(st.session_state.transactions,new_type,index, amount, category,note)
                st.success("Changes Saved")
                st.rerun()

        with col_cancel:
            if st.form_submit_button("Cancel"):
                st.rerun()

st.title("My Budget Tracker")
if "transactions" not in st.session_state:
    st.session_state.transactions=load_transactions()

balance=calculate_balance(st.session_state.transactions)
st.metric(label="Current Balance", value=f"${balance:.2f}")

st.header("All transactions")
if st.session_state.transactions:
    df=pd.DataFrame(st.session_state.transactions)
    df.index+=1
    st.dataframe(df, use_container_width=True)
else:
    st.write("No transactions to display yet")


col1,col2,col3=st.columns(3)

with col1:
    st.header("Add a new Transaction")
    with st.form("new_transaction_form", clear_on_submit=True):
        trans_type= st.selectbox("Type:", ["Income", "Expense"])
        amount=st.number_input("Amount:", min_value=0.01,format="%.2f")
        category=st.text_input("Category:",placeholder="e.g.,Job,Groceries")
        note=st.text_area("Note(Optional)")


        submitted=st.form_submit_button("Add transaction")
        if submitted:
            if not category:
                st.error("Category cannot be empty")

            else:
                add_transaction(st.session_state.transactions,trans_type.lower(),amount,category,note)
                st.success("Transaction Added!")
                st.rerun()

with col2:
    st.header("Delete a Transaction")
    if st.session_state.transactions:
        transactions_options=[f"{i+1}: {t["type"].title()} - ${t["amount"]:.2f} ({t["category"]}) "
        for i,t in enumerate(st.session_state.transactions)]

        trans_to_delete_string=st.selectbox("Select a transaction to delete:", options=transactions_options)

        if st.button('Delete Transaction'):
            trans_index_to_delete=transactions_options.index(trans_to_delete_string)
            delete_transaction(st.session_state.transactions, trans_index_to_delete)
            st.warning("Transaction deleted")
            st.rerun()
    else:
        st.write("No transactions to delete")

with col3:
    st.header("Edit a Transaction")
    if st.session_state.transactions:
        transactions_options=[
        f"{i+1}: {t["type"].title()} - {t["amount"]:.2f} {t["category"]}"
         for i, t in enumerate(st.session_state.transactions)]
        trans_to_edit_string=st.selectbox("Select a transaction to edit",
        options=transactions_options,
        key="edit_selection"                                  
        )

    

        if st.button("Edit Selected Transaction"):
            index_to_edit=transactions_options.index(trans_to_edit_string)
            show_edit_dialog(index_to_edit)
    else:
        st.write('No transactions to edit')
        