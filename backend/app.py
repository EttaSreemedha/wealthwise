# backend/app.py
from flask import Flask, request, jsonify
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Ollama model
ollama = Ollama(base_url=os.getenv('BASE_URL'), model='llama3')

# Mock functions for testing
def fetch_stock_data():
    return {"stocks": "AAPL, MSFT, GOOG"}

def fetch_precious_metals_data():
    return {"metals": "Gold: $1800/oz, Silver: $22/oz"}

def fetch_fund_data():
    return {"funds": "Vanguard S&P 500 ETF, Fidelity Contrafund"}

def fetch_bond_data():
    return {"bonds": "US Treasury Bonds, Corporate Bonds from Company X"}

@app.route('/api/financial-advice', methods=['POST'])
def financial_advice():
    data = request.json

    # Mock real-time data
    stock_data = fetch_stock_data()
    metals_data = fetch_precious_metals_data()
    fund_data = fetch_fund_data()
    bond_data = fetch_bond_data()

    # Create a query based on user details and mock real-time data
    query = f"""
    User Details:
    Age: {data['age']}
    Annual Income: {data['income']}
    Average Annual Expenses: {data['expenses']}
    Employment Status: {data['employmentStatus']}
    Financial Goals: {data['financialGoals']}
    Risk Tolerance: {data['riskTolerance']}
    Investment Horizon: {data['investmentHorizon']}
    Current Savings: {data['currentSavings']}
    Debt Amount: {data['debtAmount']}
    Family Status: {data['familyStatus']}
    
    Real-Time Data (Mocked):
    Stocks: {stock_data}
    Precious Metals: {metals_data}
    Funds: {fund_data}
    Bonds: {bond_data}
    
    Provide investment advice based on the above details and mock real-time data.
    """
    
    # Use Ollama model to generate advice
    response = ollama.invoke(query)
    
    return jsonify({"advice": response})

if __name__ == '__main__':
    app.run(debug=True)




