import plotly.graph_objects as go
from server_plot import server_plot


def plotly_heatmap(windows, w_depth, w_mag):
    
    windowsNum = range(len(windows))
    
    for i in windowsNum:
        elevation = (windows[i].iloc[:, 4]*w_depth) + (windows[i].iloc[:, 3]*w_mag)
        windows[i].insert(5, column="elevation", value=elevation) 
    
    # Create figure
    fig = go.Figure()
    
    # Add traces, one for each slider step
    for step in windowsNum:
        fig.add_trace(
            go.Densitymapbox(lat=windows[step].latitude, lon=windows[step].longitude, z=windows[step].elevation, radius=15)
            )
    
    # Make 10th trace visible
    #fig.data[10].visible = True
    
    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                  {"title": "Slider switched to step: " + str(i)}],  # layout attribute
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)
    
    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Window: "},
        pad={"t": 50},
        steps=steps
    )]
    
    fig.update_layout(sliders=sliders)
    fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
    fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
    
    fig.show()
    
    server_plot(fig)