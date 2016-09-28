#initiates a default value array for lights
from collections import defaultdict
lights = defaultdict(int)

#function to modify light status
def change(begin, end, action):
    beginx, beginy = map(int, begin.split(","))
    endx, endy = map(int, end.split(","))

    for x in range(beginx, endx+1):
            for y in range(beginy, endy+1):
                    lights[(x,y)] = max(lights[(x,y)]+action,0)

#main code reads from input and parses each line
with open("input6.txt") as f:
    for line in f.readlines():
        print(line)
        ins=line.split(" ")
        
        if line[:6]=="toggle":
            change(ins[1],ins[3],2)
        if line[:8]=="turn off":
            change(ins[2],ins[4],-1)
        if line[:7]=="turn on":
            change(ins[2],ins[4],1)

#extra code for excel output
with open('output6.txt', 'w+') as w:
    for x in range(0, 999):
            for y in range(0, 999):
                    w.write("{0:0>3}".format(lights[(x,y)])+'\n')

#import image library
from PIL import Image
img = Image.new('RGB', (999,999), "black") # create a new black image
pixels = img.load() # create the pixel map

for x in range(img.size[0]):    # for every pixel:
    for y in range(img.size[1]):
        light_int = int(lights[(x,y)] / 50 * 255)
        pixels[x,y] = (light_int, 0, 0) # set the colour accordingly

img.show()

print('end')
