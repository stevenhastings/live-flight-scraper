import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

crash_free = 0

def refresh_layout():
    
    global crash_free
    
    crash_free += 1
    
    return html.H1(f"Crash free for {crash_free} refreshes")

app.layout = refresh_layout

if __name__ == '__main__':
    app.run_server()