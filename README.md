# Black-Scholes Option Pricing Dashboard

An interactive dashboard for real-time calculations and visualizations of options pricing using the Black-Scholes model. This project is designed for financial professionals, students, and enthusiasts to explore option pricing and Greeks dynamically.

## Features
- Calculate option prices (Call and Put) using the Black-Scholes formula.
- Compute Greeks (Delta, Gamma, Vega, Theta, Rho) to understand price sensitivities.
- Interactive heatmap for analyzing the impact of spot price and volatility on option prices.
- Fully interactive and user-friendly web-based interface built with Dash.

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JordanConallLuthaisWright/black-scholes-dashboard.git
   cd black-scholes-dashboard

## Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: `venv\\Scripts\\activate`

## Install Required Dependencies 
pip install -r requirements.txt

## Run the Dashboard
python app.py

## Access the Dashboard (Open web browser and navigate to:)
http://127.0.0.1:8050/

## Usage Example 

1. Input Parameters:
      - Spot Price (𝑆): Current price of the underlying asset.
      - Strike Price (𝐾): Exercise price of the option.
      - Time to Maturity (𝑇): Remaining time until the option expires (in years).
      - Risk-Free Rate (𝑟): Annualized risk-free interest rate.
      - Volatility (𝜎): Standard deviation of the asset's returns.
      - Option Type: Choose between "Call" or "Put".
        
2. Outputs:
      - Option Price: Displays the calculated price of the selected option.
      - Greeks: Provides sensitivities like Delta, Gamma, Vega, Theta, and Rho.
      - Heatmap: Visual representation of option price sensitivity to spot price and volatility changes.

3. Example:
   - Spot Price: 100
   - Strike Price: 110
   - Time to Maturity: 1 (year)
   - Risk-Free Rate: 0.05 (5%)
   - Volatility: 0.2 (20%)
   - Option Type: Call
  Output:
   - Option Price: e.g., 8.91
   - Greeks: Delta, Gamma, Vega, Theta, Rho.
   - Heatmap showcasing price sensitivity.

## Project Sturcture 
1. dashboard.py: Main Python file to run the application.
2. requirements.txt: List of dependencies for the project.
3. README.md: Documentation file (this file).
     
## Requirements 
Python 3.8 or higher
Libraries: numpy, scipy, plotly, dash

## License 
This project is licensed under the MIT License.

## Authour 
If you have any questions or suggestions, feel free to contact me:
- Name: Jordan Conall Luthais Wright
- Email: jordan.c.l.wright@gmail.com



