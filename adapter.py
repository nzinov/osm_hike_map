from sys import argv
import smopy

smopy.TILE_SERVER = "http://abc.tile.opentopomap.org/{z}/{x}/{y}.png"
minlat, minlon, maxlat, maxlon, width, height, fname, track = argv[1:]
map = smopy.Map(tuple(map(float, (minlat, minlon, maxlat, maxlon))))
map.save_png(fname)
