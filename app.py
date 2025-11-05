import streamlit as st
import random
from agent import get_response
from db.user import USERS

st.set_page_config(
    page_title="FitBite Assistant",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ FitBite Virtual Waiter")

# --- Assign random user per session ---
if "user" not in st.session_state:
    st.session_state.user = random.choice(USERS)
    st.session_state.user_id = st.session_state.user["id"]
    st.session_state.wallet_balance = st.session_state.user["wallet_balance"]
    st.session_state.history = []

# --- Initialize cart and orders ---
if "cart" not in st.session_state:
    st.session_state.cart = []
    st.session_state.orders = []

# --- Initialize chat history ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Display user info in sidebar ---
user = st.session_state.user
st.sidebar.header("👤 Current User")
st.sidebar.write(f"**Name:** {user['name']}")
st.sidebar.write(f"**Wallet Balance:** ₦{st.session_state.wallet_balance:,}")

# --- Chat Display ---
st.markdown(
    """Hi there, you are looking stunning!
    What will you like from our restaurant today?"""
)

for chat in st.session_state.history:
    if chat["role"] == "user":
        st.chat_message("user").write(chat["content"])
    else:
        st.chat_message("assistant").write(chat["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask about the menu, or start an order..."):
    # Add user message
    st.session_state.history.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Pass user_id to the agent so it knows whose wallet to update
            response = get_response(prompt, user_id=st.session_state.user_id)
            st.write(response)

    st.session_state.history.append({"role": "assistant", "content": response})

# --- Display updated wallet balance ---
st.sidebar.write(
    f"**Updated Wallet Balance:** ₦{st.session_state.wallet_balance:,}")
