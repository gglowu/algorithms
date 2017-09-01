from PIL import Image
from point import *

#Class pic is for preprocessing PNG, including mapping pixels to travel cost and generating PNG by path route
#pwidth: width of PNG
#pheight: height of PNG
#colormap: Dictionary of {pixel value:pixel type}. Pixel value here means the RGB value of pixel and it will be transferred to HEX value eventually. 
#		   Pixel type means which designation of road current pixel stands for
#startcolor: the color to mark start / finish pixels
    

class  pic():
	def __init__(self, colormap, startcolor):
		self.pwidth = 0
		self.pheight = 0
		self.colormap = colormap
		self.startcolor = startcolor

#transfer RGB value to HEX value
	def rgbToHex(self, r,g,b):
		hex_int = (r << 16) | (g << 8) | b
		return hex_int

#input: file path of PNG picture
#output: startx, starty are the (x, y) value of start point. 
#		 endx, endy are the (x,y)value of end point
#        pixmatrix is the point matrix of PNG 
	def readPNG(self, picpath):
		im = Image.open(picpath)
		self.pwidth, self.pheight = im.size
		pixs = im.load()
		pixmatrix = []
		counter = 0
		startx = 0
		starty = 0
		endx = 0
		endy = 0

		for i in range(0, self.pwidth):
			colpixels = []
			for j in range(0, self.pheight):
				r,g,b= pixs[i, j]
				hexvalue = self.rgbToHex(r,g,b)
				#print(isinstance(hexvalue, int))
				node=point(i, j)
				node.ptype = self.colormap[hexvalue]
				colpixels.append(node)
				if hexvalue == self.startcolor:
					if counter == 0:
						startx = i
						starty = j
						counter += 1
					else:
						endx = i
						endy = j
			pixmatrix.append(colpixels)
		return (startx, starty, endx, endy, pixmatrix)

#input: picpath is where to output PNG
#		shortestrout is the point list of shortest path
# output: a PNG picture of which, the color of path is white while other pixels are black

	def writePNG(self, picpath, shortestroute):
		total = self.pwidth * self.pheight

		pixmatrix = [(0,0,0)] * total
		for pix in shortestroute:
			index = pix.y * self.pwidth + pix.x
			pixmatrix[index] = (255, 255, 255)

		newimage = Image.new("RGB", (self.pwidth, self.pheight))
		newimage.putdata(pixmatrix)
		newimage.save(picpath)