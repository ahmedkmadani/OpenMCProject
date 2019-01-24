from PIL import Image

im_1 = Image.open("AP1000.ppm")
im_2 = Image.open("ARC700.ppm")
im_3 = Image.open("VVER.ppm")

im_1.save("AP1000.jpg")
im_2.save("ARC700.jpg")
im_3.save("VVER.jpg")