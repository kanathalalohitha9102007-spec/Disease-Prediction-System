import streamlit as st

st.set_page_config(page_title="Tea Hut", layout="wide")
st.title("🍵 Welcome to Tea Hut")

if 'expenses' not in st.session_state:
    st.session_state.expenses = []

col1, col2 = st.columns(2)

with col1:
    st.subheader("🥤 Select your cup")
    with st.form("select_cup_form"):
        title = st.text_input("Cup Title")
        amount = st.number_input("Amount", min_value=0.0, step=1.0, format="%.2f")
        category = st.selectbox("Category", ["Black Tea", "Green Tea", "Herbal Tea", "Masala Tea", "Other"])
        add = st.form_submit_button("Add Cup")
        if add:
            if title and amount > 0:
                st.session_state.expenses.append({"title": title, "amount": amount, "category": category})
                st.success("Cup added!")
            else:
                st.error("Please enter a valid title and amount.")

with col2:
    st.subheader("🫖 Tea Sales")

    total_sales = sum(item['amount'] for item in st.session_state.expenses)
    st.write(f"Total Tea Sales: ₹{total_sales:.2f}")

    show_details = st.checkbox("Show Cup Details")
    category_filter = st.selectbox("Filter by category", ["ALL", "Black Tea", "Green Tea", "Herbal Tea", "Masala Tea", "Other"])

    if show_details:
        filtered_items = st.session_state.expenses
        if category_filter != "ALL":
            filtered_items = [item for item in st.session_state.expenses if item['category'] == category_filter]

        if filtered_items:
            st.write("### Cups")
            for item in filtered_items:
                st.write(f"{item['title']} - ₹{item['amount']:.2f} ({item['category']})")

            filtered_total = sum(item['amount'] for item in filtered_items)
            st.write(f"Total {category_filter} Cups: ₹{filtered_total:.2f}")
        else:
            st.info("No cups found for selected filter.")
