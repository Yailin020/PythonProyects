import imageio.v3 as iio


filenames = [
    'images/file1.png',
    'images/file2.png',
]
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0, disposal=2)
