import sys
from PIL import Image, ImageDraw, ImageFont

images = [Image.open(x) for x in sys.argv[1:]]
ubuntu = ImageFont.truetype("Ubuntu-Bold.ttf", 50)
ctr = 0
for im in images:
    im = im.convert("RGB")
    sz = im.size
    if ctr == 0:
        text = "original image"
        color = "#0f5257"
        fontspan = .37
    else:
        color = "#0d2129"
        text = "image w/ protective filter"
        fontspan = .67
    fontsize = 1
    font  = ImageFont.truetype("Ubuntu-Bold.ttf", fontsize)
    while font.getsize(text)[0] < fontspan*im.size[0]:
        fontsize += 1
        font = ImageFont.truetype("Ubuntu-Bold.ttf", fontsize)

    im_new = Image.new('RGB', (sz[0] , sz[1] + int(sz[1]/5)), color)
    im_new.paste(im)
    draw = ImageDraw.Draw(im_new)
    draw.text((sz[0]/10, sz[1]+ int(sz[1]/12)), text, font=font)
    images[ctr] = im_new
    ctr += 1
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

new_im.save('test.jpg')
