import dash
import dash_core_components as dcc
import dash_html_components as html

def server_plot(fig):
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(figure=fig)
    ])
    
    app.run_server(debug=True, use_reloader=False)