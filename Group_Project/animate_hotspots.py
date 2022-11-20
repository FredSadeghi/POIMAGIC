import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def plot_hotspot(df, pointCount):
    #file - file path to be read
    #pointCount - number of points to be used when making grid
    
    data = df
    
    Lat = data.iloc[:,1]
    Long = data.iloc[:,2]
    Elev = data.iloc[:,4] * data.iloc[:,3]
    
    pts = pointCount; 
    
    [x,y]=np.meshgrid(np.linspace(np.min(Long),np.max(Long),np.sqrt(pts).astype(int)),np.linspace(np.min(Lat),np.max(Lat),np.sqrt(pts).astype(int)));
    z = griddata((Long, Lat), Elev, (x, y), "nearest");
    
    x = np.matrix.flatten(x); #Gridded longitude
    y = np.matrix.flatten(y); #Gridded latitude
    z = np.matrix.flatten(z); #Gridded elevation
    
    #plot
    plt.scatter(x,y,1,z)
    plt.colorbar(label='Magnitude * Depth')
    plt.xlabel('Longitude [°]')
    plt.ylabel('Latitude [°]')
    return plt

def generate_windows(fileList, window):
    #list of all files to be read
    #size of sliding window
    #pointCount - number of points to use in heatmap
    windows = []

    for i in range(len(fileList)):
        if i+window > len(fileList):
            break;
        frames = []
        for j in range(window):
            frames.append(pd.read_csv(fileList[i+j]))
        data = pd.concat(frames)
        print("Window ", i +1)
        print(data, "\n")
        windows.append(data)
    return windows


