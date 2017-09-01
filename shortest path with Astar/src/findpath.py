import sys
from network import *
from pic import *

def main(argv=None):
	if argv is None:
		argv = sys.argv

	if len(sys.argv) == 1:
		image_list = ['map_00010.png', 'map_00009.png','map_00008.png','map_00007.png','map_00006.png','map_00005.png','map_00004.png','map_00003.png','map_00002.png','map_00001.png', 'map_00000.png']
	else:
		image_list = sys.argv[1:]

	colormap = {0x000000:0, 0xffffff:1, 0xb03a2e:2, 0x6c3483:3, 0x2874a6:4, 0x117565:5, 0x239b56:6, 0xd4ac0d:7, 0xd35400:8}
	timecost = [100,60,30,20,12,6,4,3,60]

	pic_object = pic(colormap, 0xd35400)
	start_point = point(0, 0)
	end_point = point(0,0)

	for imgae_to_process in image_list:
		start_point.x, start_point.y, end_point.x, end_point.y, pixmap = pic_object.readPNG(imgae_to_process)
		routemap = network(timecost, pixmap)
		route = routemap.getPath(start_point, end_point)
		pic_object.writePNG(imgae_to_process[0:-4]+"_route.png", route)

if __name__ == '__main__':
	sys.exit(main())