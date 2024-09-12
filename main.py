from plotly import express as px
import pandas as pd

# Sample data representing zones in a smart city
data = {
    'Zone': ['Water Zone', 'Energy Zone', 'Heat Island'],
    'Latitude': [40.7128, 40.730610, 40.715],
    'Longitude': [-74.0060, -73.935242, -74.010],
    'Description': ['Water usage: 1200 liters/day', 
                    'Energy efficiency: 85%', 
                    'Heat island: +3°C above avg']
}

df = pd.DataFrame(data)

# Create interactive map
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", text="Description",
                        hover_name="Zone", zoom=12, height=600)

# Set map style
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Save the figure as an HTML file
fig.write_html("interactive_map.html")
