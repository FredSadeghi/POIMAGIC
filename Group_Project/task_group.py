from folderScanner import list_files
from animate_hotspots import *

my_files_list = list_files('earthquake_contiguous_usa_12batch', '.csv')

windows = generate_windows(my_files_list, 3)

print("----------------------------------------------------------------------")

for i in range(len(windows)):
    #plots.append(plot_hotspot(windows[i], 50000))
    plot = plot_hotspot(windows[i], 50000)
    plot.show()
    plot.close()


