from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dash is working 🚀"),
    html.P("Quantium environment is set up correctly.")
])

if __name__ == "__main__":
    app.run(debug=True)
