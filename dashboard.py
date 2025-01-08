# Black-Scholes Option Pricing Model with Dashboard

# Import necessary libraries
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Define the Black-Scholes formula
def black_scholes(S, K, T, r, sigma, option_type='call'):
    """Calculate the Black-Scholes option price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

# Define Greeks for options
def calculate_greeks(S, K, T, r, sigma):
    """Calculate Greeks for Black-Scholes model."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta_call = norm.cdf(d1)
    delta_put = -norm.cdf(-d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
    theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365
    rho_call = K * T * np.exp(-r * T) * norm.cdf(d2)
    rho_put = -K * T * np.exp(-r * T) * norm.cdf(-d2)

    return {
        'Delta Call': delta_call,
        'Delta Put': delta_put,
        'Gamma': gamma,
        'Vega': vega,
        'Theta Call': theta_call,
        'Theta Put': theta_put,
        'Rho Call': rho_call,
        'Rho Put': rho_put
    }

# Initialize Dash app
app = Dash(__name__)
app.title = "Black-Scholes Option Pricing"

# Layout for the dashboard
app.layout = html.Div([
    html.H1("Black-Scholes Option Pricing Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Spot Price (S):"),
        dcc.Input(id='spot-price', type='number', value=100, step=1),

        html.Label("Strike Price (K):"),
        dcc.Input(id='strike-price', type='number', value=100, step=1),

        html.Label("Time to Maturity (T in years):"),
        dcc.Input(id='time-to-maturity', type='number', value=1, step=0.01),

        html.Label("Risk-Free Rate (r):"),
        dcc.Input(id='risk-free-rate', type='number', value=0.05, step=0.01),

        html.Label("Volatility (sigma):"),
        dcc.Input(id='volatility', type='number', value=0.2, step=0.01),

        html.Label("Option Type:"),
        dcc.Dropdown(
            id='option-type',
            options=[{'label': 'Call', 'value': 'call'}, {'label': 'Put', 'value': 'put'}],
            value='call'
        )
    ], style={'columnCount': 2, 'marginBottom': '20px'}),

    html.Div([
        html.H3("Option Price:"),
        html.Div(id='option-price-output', style={'marginBottom': '20px'})
    ]),

    html.Div([
        html.H3("Greeks:"),
        html.Div(id='greeks-output', style={'whiteSpace': 'pre-wrap'})
    ]),

    html.Div([
        dcc.Graph(id='heatmap-output')
    ])
])

@app.callback(
    [
        Output('option-price-output', 'children'),
        Output('greeks-output', 'children'),
        Output('heatmap-output', 'figure')
    ],
    [
        Input('spot-price', 'value'),
        Input('strike-price', 'value'),
        Input('time-to-maturity', 'value'),
        Input('risk-free-rate', 'value'),
        Input('volatility', 'value'),
        Input('option-type', 'value')
    ]
)
def update_dashboard(S, K, T, r, sigma, option_type):
    if None in [S, K, T, r, sigma]:
        return "Please input all values.", "", {}

    option_price = black_scholes(S, K, T, r, sigma, option_type)
    greeks = calculate_greeks(S, K, T, r, sigma)

    # Heatmap data
    spot_prices = np.linspace(S * 0.5, S * 1.5, 50)
    volatilities = np.linspace(sigma * 0.5, sigma * 1.5, 50)
    heatmap_data = np.array([
        [black_scholes(spot, K, T, r, vol, option_type) for vol in volatilities] for spot in spot_prices
    ])

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data,
        x=volatilities,
        y=spot_prices,
        colorscale='Viridis',
        colorbar=dict(title='Option Price')
    ))
    fig.update_layout(
        title="Option Price Sensitivity",
        xaxis_title="Volatility",
        yaxis_title="Spot Price"
    )

    greeks_text = "\n".join([f"{key}: {value:.4f}" for key, value in greeks.items()])

    return f"{option_price:.2f}", greeks_text, fig

if __name__ == "__main__":
    app.run_server(debug=True)
