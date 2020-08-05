import shapefile
from numpy import array, arange, append
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.pyplot import get_cmap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

# get shapefile data
sf = shapefile.Reader('geo_data/cb_2018_us_county_500k.shp')
sr = sf.records()
shapes = sf.shapes()
n_shapes = len(shapes)

# number counties
county_numbers = array([])
for nn in range(n_shapes):
    county_numbers = append(county_numbers, sr[nn][1])

#cm = get_cmap('bone')
#cccol = cm(1.*arange(n_shapes)/n_shapes)

#   -- plot --
fig = plt.figure()
ax = fig.add_subplot(111)
for nn in range(n_shapes):
    print(sr[nn]['NAME'])
    patches = []
    pts = array(shapes[nn].points)
    prt = shapes[nn].parts
    par = list(prt) + [pts.shape[0]]
    for pp in range(len(prt)):
        patches.append(Polygon(pts[par[pp]:par[pp+1]]))
    ax.add_collection(PatchCollection(patches, facecolor='white',
        edgecolor='gray', linewidths=0.25))

ax.set_xlim(-130,-60)
ax.set_ylim(20,50)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()