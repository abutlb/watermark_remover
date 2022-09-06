import os
from PIL import Image , ImageFilter

if not os.path.exists("out"):
    os.mkdir("out")


def get_sample(data):
    sample = []
    samples = os.listdir(data)
    print(samples)
    for sample_file in samples:
        sample_Image = Image.open(f"{data}{sample_file}").getdata()
        for i in sample_Image:
            if i not in sample:
             sample.append(i)
    print("sample aquired!!")
    return sample


sample_image = get_sample("sample\\")
orignal = Image.open("orignal.jpeg")
#width,hight = orignal.size
#orignal = orignal.resize((width*2,hight*2))

d = orignal.getdata()
new_image = []
n = 0
bg_color = 255
for pixle in d:
    if pixle in sample_image:
        new_image.append((bg_color,bg_color,bg_color))
    else:
        new_image.append(pixle)
    
    #n = n + 1

n = 0

orignal.putdata(new_image)

while True:
    if not os.path.exists(f"out\\new{n}.jpg"):
        orignal.save(f"out\\new{n}.jpg")
        break
    else:
        n = n +1