import pandas as pd
from fiveNumSum import fiveNumSum

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
        #print("Window ", i +1)
        #print(data, "\n")
        windows.append(data)
    return windows

def generate_windows_filtered(windows, w1, w2):
    w_depth = w1 
    w_mag = w2
    total = []
    
    #used to determine d1 and d2
    for i in range(len(windows)):
        for j in range(len(windows[i])):
            total.append(
                (windows[i].iloc[j].iloc[3]*w_depth) + (windows[i].iloc[j].iloc[4]*w_mag))

    summary = fiveNumSum(total)
    d1 = summary[3]
    d2 = summary[2]
    
    #generate the actual windows based on the d1 and d2 thresholds
    windows_d1 = list()
    windows_d2 = list()

    for i in range(len(windows)):
        windows_d1.append(pd.DataFrame())
        for j in range(len(windows[i])):
            if (windows[i].iloc[j].iloc[3]*w_depth) + (windows[i].iloc[j].iloc[4]*w_mag) > d1:
                new_df = pd.DataFrame(windows[i].iloc[j])
                new_df = new_df.T
                frames = [windows_d1[i],new_df]
                windows_d1[i] = pd.concat(frames)#indexes to add to windows_d1
        windows_d1[i] = windows_d1[i].reset_index(drop=True)
        
    for i in range(len(windows)):
        windows_d2.append(pd.DataFrame())
        for j in range(len(windows[i])):
            if (windows[i].iloc[j].iloc[3]*w_depth) + (windows[i].iloc[j].iloc[4]*w_mag) > d2:
                new_df = pd.DataFrame(windows[i].iloc[j])
                new_df = new_df.T
                frames = [windows_d2[i],new_df]
                windows_d2[i] = pd.concat(frames)#indexes to add to windows_d1
        windows_d2[i] = windows_d2[i].reset_index(drop=True)
                
    return windows_d1, windows_d2


#------------------------------------------------------------------------------
#this plotting method is outdated
# def plot_hotspot(df, pointCount, plotType):
#     #file - file path to be read
#     #pointCount - number of points to be used when making grid
    
#     data = df
    
#     Lat = data.iloc[:,1]
#     Long = data.iloc[:,2]
#     Elev = data.iloc[:,4] * data.iloc[:,3]
    
#     pts = pointCount; 
    
#     [x,y]=np.meshgrid(np.linspace(np.min(Long),np.max(Long),np.sqrt(pts).astype(int)),np.linspace(np.min(Lat),np.max(Lat),np.sqrt(pts).astype(int)));
#     z = griddata((Long, Lat), Elev, (x, y), plotType);
    
#     x = np.matrix.flatten(x); #Gridded longitude
#     y = np.matrix.flatten(y); #Gridded latitude
#     z = np.matrix.flatten(z); #Gridded elevation
    
#     #plot
#     plt.scatter(x,y,1,z)
#     plt.xlabel('Longitude [°]')
#     plt.ylabel('Latitude [°]')
#     return plt

