import sys
import os
from PIL import Image, ImageDraw, ImageFont


def format_demo_output(image_name, image_1, image_2):
    names = [image_1,image_2]
    images = [Image.open(x) for x in names]
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
    save_path = '/home/ubuntu/fawkes/app/tmp/' + image_name + '_output.jpg'
    new_im.save(save_path)
    os.system("aws s3 cp %s s3://trix-public --acl=public-read" % save_path)
    return 'https://trix-public.s3-us-west-2.amazonaws.com/' + image_name + '_output.jpg'
