from PIL import Image
import os

######################################################

print('hell world');

picpath = os.path.join( os.path.dirname(__file__),  r'pic/cut19_worldend-2400x1602.jpg');
img = Image.open(picpath);
img.show();
