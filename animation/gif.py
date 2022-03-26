from PIL import Image


images = []
images.append(Image.open('ball1.png'))
images.append(Image.open('ball2.png'))
images[0].save('anime.gif', save_all=True, append_images=images[1:2], duration=100, loop=0)

