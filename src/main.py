import os
from vector import Vec3


def hello_world_ppm():
    image_name = "hello_world.ppm"
    path = os.path.join(os.path.dirname(__file__), "images", image_name)
    ppm_file = open(path, 'w')
    image_width = 150
    image_height = 100
    title = f"P3\n{image_width} {image_height}\n255\n"
    ppm_file.write(title)

    for j in range(image_height):
        print("Scanlines remaining:", image_height - j)
        for i in range(image_width):
            # r = i/(image_width-1)
            # g = j/(image_height-1)
            # b = 0.0
            
            color = Vec3(float(i)/float(image_width), float(j)/float(image_height), 0.0)
            ir = int(255.99*color.r)
            ig = int(255.99*color.g)
            ib = int(255.99*color.b)
            value = f"{ir} {ig} {ib}\n"
            ppm_file.write(value)
            
    ppm_file.close()
    print('Done. Saved as', image_name)


if __name__ == '__main__':
    hello_world_ppm()