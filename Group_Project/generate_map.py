import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df1 = pd.read_csv("earthquake_contiguous_usa_12batch/Earthquake_2020_9_2020_10_filtered.csv", delimiter=',', skiprows=0,
                  low_memory=False)
df2 = pd.read_csv("earthquake_contiguous_usa_12batch/Earthquake_2020_11_2020_12_filtered.csv", delimiter=',',
                  skiprows=0, low_memory=False)

elevation = df1.iloc[:, 4] * df1.iloc[:, 3]
elevation = df2.iloc[:, 4] * df2.iloc[:, 3]
df1.insert(5, column="elevation", value=elevation)
df2.insert(5, column="elevation", value=elevation)

geometry = [Point(xy) for xy in zip(df2['longitude'], df2['latitude'])]
gdf = GeoDataFrame(df2, geometry=geometry)

# this is a simple map that goes with geopandas
usa = gpd.read_file('usa_map/cb_2021_us_state_500k.shp')
usa = usa[~usa['NAME'].isin(['Alaska', 'Hawaii', 'Puerto Rico', 'American Samoa', 'Guam',
                             'Commonwealth of the Northern Mariana Islands', 'United States Virgin Islands'])]
usa = usa.to_crs("EPSG:4326")

gdf.plot(ax=usa.boundary.plot(figsize=(15, 6)), marker='o', color='red', markersize=10)
# plt.show()

# fig = go.Figure(go.Densitymapbox(lat=df1.latitude, lon=df1.longitude, z=df1.elevation, radius=10))
# fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
# fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

fig = go.Figure(go.Densitymapbox(lat=df2.latitude, lon=df2.longitude, z=df2.elevation, radius=15))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

fig.show()

# figs = px.density_mapbox(df1, lat='latitude', lon='longitude', z='elevation',
#                          mapbox_style="stamen-terrain")
#
# plt.show()
