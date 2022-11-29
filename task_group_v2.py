from folderScanner import list_files
from generate_map_v2 import plotly_heatmap
from windows_functions import generate_windows, generate_windows_filtered

#pointCount = 50000 #plot dpi
#frameRate = 6 #frameRate of the animation
#plotType = "nearest"

windowSize = 3 #how many batches to include in each window
w_depth = .3 
w_mag = .7

my_files_list = list_files('earthquake_contiguous_usa_12batch', '.csv') #list of all batches names
windows = generate_windows(my_files_list, windowSize) #all window dataframes

windows_d1, windows_d2 = generate_windows_filtered(windows,w_depth,w_mag)

# plotly_heatmap(windows_d1, w_depth, w_mag)
plotly_heatmap(windows_d2, w_depth, w_mag)
