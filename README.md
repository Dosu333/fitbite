# 🍽️ FitBite — AI-Powered Waiter

**FitBite** is an intelligent restaurant chatbot that combines conversational AI with real-world transactional logic.
Built with **Google Gemini Function Calling**, **Streamlit**, and **Python**, it lets users explore a restaurant’s menu, customize their meals, manage their cart, and make wallet-based payments — all through natural language.

---

## 🚀 Features

✅ **Conversational Ordering Flow**

* Users can chat naturally to browse the full menu, pick meals, and choose sides.
* The assistant ensures every order follows the restaurant’s rules (no missing required sides, no invented items).

✅ **Function Calling with Gemini**

* Uses Google’s `genai` SDK and the Gemini 2.5-flash model to trigger backend functions like `make_payment` securely.
* The model doesn’t just chat — it executes real Python logic based on user intent.

✅ **Wallet System Integration**

* Each user has a wallet balance stored in memory.
* Payments deduct from the wallet, with error handling for insufficient funds or missing users.

✅ **Persistent State via Streamlit**

* Session-based balance tracking ensures each user’s wallet stays consistent across requests.
* Clean Streamlit interface for testing, debugging, and demoing the conversation.

✅ **Robust Error Handling & Retry Logic**

* Automatic backoff retries for transient `503` errors from the API.
* Graceful fallbacks when responses are missing or delayed.

---

## 🧠 System Architecture

```
┌──────────────────────────────┐
│        Streamlit UI          │
│  - Displays chat messages    │
│  - Captures user prompts     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        get_response()        │
│  - Handles LLM prompt flow   │
│  - Detects function calls    │
│  - Calls make_payment()      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         call_function()      │
│  - Executes local functions  │
│  - Returns structured result │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         make_payment()       │
│  - Checks wallet balance     │
│  - Deducts & updates state   │
│  - Returns JSON response     │
└──────────────────────────────┘
```

---

## 🧩 Tech Stack

| Layer                | Technology              | Purpose                                             |
| -------------------- | ----------------------- | --------------------------------------------------- |
| **Frontend**         | Streamlit               | Chat interface for testing and demos                |
| **LLM API**          | Gemini 2.5-Flash        | Natural language understanding and function calling |
| **Backend**          | Python                  | Core logic and function definitions                 |
| **State Management** | Streamlit Session State | Tracks user wallet balance                          |
| **Environment**      | `.env` + `dotenv`       | Secure API key management                           |

---

## ⚙️ Project Structure

```
fitbite/
├── app.py                  # Streamlit interface
├── agent.py                # Core LLM chat and response logic
├── functions/
│   ├── call_function.py    # Function call handler
│   └── wallet.py           # Payment logic and schemas
├── db/
│   ├── user.py             # Mock user database
│   └── menu.py             # Full restaurant menu data
├── .env                    # Stores GEMINI_API_KEY
└── README.md
```

---

## 💵 Example Conversation

**User:**

> What’s on your menu?

**Bot:**

> Sure! Here’s our Full Menu. Would you like me to show you by category — Rice Dishes, Grills, or Drinks?

---

**User:**

> Add Grilled Chicken with Jollof Rice.

**Bot:**

> Got it! Grilled Chicken with Jollof Rice has been added to your cart. Would you like anything else?

---

**User:**

> I’m ready to pay.

**Bot:**

> Here’s your order summary:
> • Grilled Chicken + Jollof Rice — ₦3,500
> • Service Fee: ₦200
> • Delivery Fee: ₦500
> **Total: ₦4,200**
>
> Would you like to confirm and pay ₦4,200?

---

**User:**

> Yes, confirm payment.

**Bot:**

> ✅ Payment of ₦4,200 successful. New balance: ₦7,800.

---

## 🧪 Local Setup

### 1️⃣ Clone and Navigate

```bash
git clone https://github.com/<yourusername>/fitbite.git
cd fitbite
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment

Create a `.env` file with your Gemini API key:

```
GEMINI_API_KEY=your_google_api_key_here
```

### 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧰 Key Concepts Demonstrated

| Concept                          | Why It Matters                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------- |
| **Function Calling with Gemini** | Demonstrates advanced LLM-tool integration — a must-have skill for AI engineers. |
| **LLM-Driven Transactions**      | Bridges conversation AI with real backend logic.                                 |
| **Session Management**           | Ensures state consistency in an interactive app.                                 |
| **Error Handling + Retries**     | Shows reliability and production readiness.                                      |
| **Prompt Engineering**           | Guides model behavior with system instructions and constraints.                  |

---

## 🧑‍💻 Author

**Oladosu Larinde** — Lead Software Engineer

* 🎧 Built scalable backend systems with Django, Celery, Redis, and Nginx.
* 🧠 Passionate about building AI-powered tools that bridge natural conversation and computation.
* 💬 [LinkedIn](https://linkedin.com/in/oladosularinde) · [GitHub](https://github.com/Dosu333)

