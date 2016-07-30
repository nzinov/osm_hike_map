from sys import argv
import tiler

tiler.TILE_SERVER = "http://abc.tile.opentopomap.org/{z}/{x}/{y}.png"
minlat, minlon, maxlat, maxlon = map(float, argv[1:5])
width, height = map(int, argv[5:7])
fname = argv[7]
map = tiler.Map((minlat, minlon, maxlat, maxlon), size=(width, height))
map.save_png(fname)
