import pandas as pd
import plotly.express as px
import json
from dash import Dash, dcc, html, Input, Output

# Load JSON data
with open("daikibo-telemetry-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Creating DataFrame
df = pd.json_normalize(data)
print(df.head())
print(df.columns)

# Add 'Unhealthy' column
df['Unhealthy'] = df['data.status'].apply(lambda x: 10 if x == 'unhealthy' else 0)

# Downtime per factory
downtime_factory = df.groupby('location.factory')['Unhealthy'].sum().reset_index()

# Initialize Dash app
app = Dash(__name__)
app.title = "Daikibo Telemetry Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Daikibo Telemetry Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(id='factory-chart'),
    html.Hr(),
    dcc.Graph(id='device-chart'),
    dcc.Store(id='selected-factory'),
])

# Callback to update factory chart
@app.callback(Output('factory-chart', 'figure'),
              Input('selected-factory', 'data'))
def update_factory_chart(selected_factory):
    fig = px.bar(downtime_factory,
                 x='location.factory', y='Unhealthy', title="Down Time Per Factory",
                 labels={'Unhealthy': 'Total Down Time (minutes)'}, color='Unhealthy')
    fig.update_traces(marker_color='orange')
    fig.update_layout(clickmode='event+select')
    return fig

# Callback to update device chart based on selected factory
@app.callback(Output('device-chart', 'figure'),
              Input('factory-chart', 'clickData'))
def update_device_chart(clickData):
    if clickData:
        selected_factory = clickData['points'][0]['x']
        filtered_df = df[df['location.factory'] == selected_factory]
        device_df = filtered_df.groupby('deviceType')['Unhealthy'].sum().reset_index()
        fig = px.bar(device_df,
                     x='deviceType', y='Unhealthy',
                     title=f"Down Time Per Device Type ({selected_factory})",
                     labels={'Unhealthy': 'Down Time (minutes)'}, color='Unhealthy')
        fig.update_traces(marker_color='blue')
        return fig
    else:
        return px.bar(title="Select a factory above to see device-level downtime")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


    
        
           
                    
