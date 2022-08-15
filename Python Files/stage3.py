import dash
import dash_html_components as html 
import dash_core_components as dcc
from dash.dependencies import Input, Output
import requests 

# Instantiate Dash App
app = dash.Dash()

# Set up layout for app with an Iframe
app.layout = html.Div([
             
             html.Div([                 # Grabs website to show in dashboard
                        html.Iframe(src="https://ww.flightradar24.com",
                                    
                                    height=500, width=1200)
             ]),

             html.Div([
             
             html.Pre(id='counter_text',
             
             children='Active Flights Worldwide'),
             
             dcc.Interval(id='interval-component',
             # Update every 6 seconds
             interval=6000,
             
             n_intervals=0)
             
             ])
        ])

## Connecting above components to function with callback
@app.callback(Output('counter_text', 'children'),
              [Input('interval-component', 'n_intervals')])

# Setting up the update-app format              
def update_layout(n):
    
    # Url to scrape from
    URL = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    
    # requesting scraper to go get data.
    res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

    data = res.json()

    counter = 0

    for element in data['stats']['total']:

        counter += data['stats']['total'][element]

    return f"Active Flights Worldwide: {counter}"

if __name__ == '__main__':
    app.run_server()