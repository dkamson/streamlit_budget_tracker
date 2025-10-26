# Full-Stack Streamlit Budget Tracker

A personal finance tracker web application built with Python and Streamlit. This app allows users to track their income and expenses through an interactive UI. All data is saved to a local JSON file, making it a complete, full-stack application.

## Key Features
* **Full CRUD Functionality:** Users can **C**reate, **R**ead, **U**pdate, and **D**elete transactions.
* **Persistent Data:** All data is saved to a `transactions.json` file.
* **Interactive UI:** Built with Streamlit, the app features:
    * A 3-column layout for adding, deleting, and editing items.
    * Popup dialog forms for a clean editing experience.
* **Real-Time Updates:** Uses `st.session_state` and `st.rerun()` to ensure the UI updates instantly after any change.

## Core Skills Demonstrated
* **Full-Stack Development:** Engineered a front-end UI (Streamlit) that interacts with a back-end logic layer (`logic.py`) and a database (JSON file).
* **State Management:** Implemented Streamlit's session state (`st.session_state`) to manage the application's state and handle complex UI interactions like popups.
* **Code Refactoring:** Refactored a command-line Python script into a modular, multi-file web application, separating logic from the UI.
* **Data Handling:** Utilized the Pandas library to display data in a clean, indexed, and sortable table.

## How to Run This Project
1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/streamlit-budget-tracker.git](https://github.com/your-username/streamlit-budget-tracker.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd streamlit-budget-tracker
    ```
3.  Install the required libraries:
    ```bash
    pip install streamlit pandas
    ```
4.  Run the app:
    ```bash
    streamlit run app.py
    ```