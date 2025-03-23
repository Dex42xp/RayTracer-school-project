import os
import math
from vector import *
from ray import Ray

def write_color(color):
    ir = int(255.99*color.r)
    ig = int(255.99*color.g)
    ib = int(255.99*color.b)
    return f"{ir} {ig} {ib}\n"



def hit_sphere(center, radius, r):
    oc = center - r.origin
    a = dot(r.direction, r.direction)
    b = -2.0 * dot(r.direction, oc)
    c = dot(oc, oc) - radius**2
    discriminant = b * b - 4*a*c

    if discriminant < 0:
        return -1.0
    return (-b - math.sqrt(discriminant)) / (a*2.0)
    
def ray_color(r):
    t = hit_sphere(Vec3(0,0,-1), 0.5, r)
    if t > 0:
        N = unit_vector(r.point_at_parameter(t) - Vec3(0,0,-1))
        return Vec3(N.x+1,N.y+1,N.z+1)*0.5
    
    unit_direction = unit_vector(r.direction)
    t = 0.5 * (unit_direction.y + 1.0)
    return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t


def main():
    image_name = "sphere_normal.ppm"
    aspect_ratio = 16/9
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    if image_height < 1:
        image_height = 1
    
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (image_width/image_height)
    camera_center = Vec3(0, 0, 0)
    
    viewport_u = Vec3(viewport_width, 0 , 0)
    viewport_v = Vec3(0, -viewport_height, 0)
    
    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height
    
    viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
    pixel00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5
    
    path = os.path.join(os.path.dirname(__file__), "images", image_name)
    ppm_file = open(path, 'w')
    
    title = f"P3\n{image_width} {image_height}\n255\n"
    ppm_file.write(title)

    for j in range(image_height):
        print("Scanlines remaining:", image_height - j)
        for i in range(image_width):
            pixel_center = pixel00_loc + (pixel_delta_u * i) + (pixel_delta_v * j)
            ray_direction = pixel_center - camera_center
            r = Ray(camera_center, ray_direction)
            
            pixel_color = ray_color(r)
            ppm_file.write(write_color(pixel_color))
            
    ppm_file.close()
    print('Done. Saved as', image_name)


if __name__ == '__main__':
    main()