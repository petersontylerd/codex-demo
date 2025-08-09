import sqlite3
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

DB_PATH = "sample.db"

# Read aggregated data
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT category, total_amount FROM category_summary", conn)
conn.close()

app = Dash(__name__)
fig = px.bar(df, x="category", y="total_amount", title="Total Amount by Category")

app.layout = html.Div([
    html.H1("Category Summary"),
    dcc.Graph(id="amount-chart", figure=fig),
])

if __name__ == "__main__":
    app.run_server(debug=False)
