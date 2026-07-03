# 🧠 Decision Lab - Your AI Executive Boardroom for Smarter Decisions 

> **An AI-powered multi-agent boardroom that helps users make complex life and career decisions by consulting specialized AI experts before delivering a final board verdict.**

------------------------------------------------------------------------

## 🌟 Overview

Decision Lab simulates an executive boardroom using multiple AI agents.
Instead of relying on a single AI response, the system assigns
specialized experts to evaluate a decision from different perspectives
before a Chairperson synthesizes a final recommendation.

Whether you're deciding to:

-   🏠 Buy a House
-   🎓 Pursue an MBA
-   💼 Switch Careers
-   🚀 Start a Business

Decision Lab provides balanced, explainable, and structured decision
support.

------------------------------------------------------------------------

## ✨ Features

-   🧠 Intelligent Planner Agent
-   ❓ Dynamic Clarification Questions
-   💰 Financial Analyst
-   ⚠️ Risk Analyst
-   😈 Devil's Advocate
-   🏛 Chairperson (Final Verdict)
-   🎨 Interactive Streamlit Interface
-   🔄 Session State Management
-   🤖 Powered by Google Gemini

------------------------------------------------------------------------

## 🏗 Architecture

``` text
                    User Decision
                          │
                          ▼
                 🧠 Planner Agent
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
 Generates Questions              Selects Experts
        │
        ▼
     User Answers
        │
        ▼
 ┌──────────┬───────────┬────────────┐
 ▼          ▼           ▼
Financial   Risk     Devil's Advocate
 Analyst    Analyst
        │
        └──────────┬───────────────┘
                   ▼
          🏛 Chairperson
                   │
                   ▼
          Final Board Verdict
```

------------------------------------------------------------------------

## 📂 Project Structure

``` text
DecisionLab
│
├── agents/
├── assets/
├── core/
├── streamlit_app.py
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

------------------------------------------------------------------------

## ⚙️ Installation

Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/DecisionLab.git
```

Go to the project

``` bash
cd DecisionLab
```

Install dependencies

``` bash
pip install -r requirements.txt
```

Create a `.env` file

``` env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

``` bash
streamlit run streamlit_app.py
```

------------------------------------------------------------------------

## 💡 How It Works

1.  The user enters a decision.
2.  The Planner Agent categorizes the decision and identifies missing
    information.
3.  The user answers the clarification questions.
4.  Specialized AI experts independently analyze the decision.
5.  The Chairperson synthesizes all opinions into a single board
    verdict.

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   Streamlit
-   Google Gemini API
-   Prompt Engineering
-   Multi-Agent AI Architecture

------------------------------------------------------------------------

## 📸 Screenshots

*Screenshots added in the assetss/ folder for reference.*

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Additional expert agents
-   Decision history
-   PDF report export
-   More decision domains
-   Live deployment

------------------------------------------------------------------------

## 👨‍💻 Author

**Riddhi More**

Created as part of the **Kaggle Vibe Coding Agents Capstone Project**.
