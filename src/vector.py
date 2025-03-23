import math

class Vec3(list):

    def __init__(self, e0, e1, e2):
        self.append(float(e0))
        self.append(float(e1))
        self.append(float(e2))
        # XYZ coordinates
        self.x = e0
        self.y = e1
        self.z = e2
        # RGB
        self.r = e0
        self.g = e1
        self.b = e2
        # Length
        self.length = math.sqrt(e0*e0 + e1*e1 + e2*e2)
        self.squared_length = (e0*e0 + e1*e1 + e2*e2)

    def __add__(self, other):
        return Vec3(self[0] + other[0],
                       self[1] + other[1],
                       self[2] + other[2])

    def __sub__(self, other):
        return Vec3(self[0] - other[0],
                       self[1] - other[1],
                       self[2] - other[2])

    def __mul__(self, other):
        return Vec3(self[0] * other,
                       self[1] * other,
                       self[2] * other)

    def mul(self, other):
        return Vec3(self[0] * other[0],
                       self[1] * other[1],
                       self[2] * other[2])

    def __truediv__(self, other):
        return Vec3(self[0] / other,
                       self[1] / other,
                       self[2] / other)

    def make_unit_vector(self):
        """
        Makes the current vector it's unit vector
        :return:
        """
        self[0] = self[0]/self.length
        self[1] = self[1]/self.length
        self[2] = self[2]/self.length


def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


def cross(v1, v2):
    return Vec3(v1[1]*v2[2] - v1[2]*v2[1],
                   v1[2]*v2[0] - v1[0]*v2[2],
                   v1[0]*v2[1] - v1[1]*v2[0])


def unit_vector(vector):
    return Vec3(vector[0] / vector.length, vector[1] / vector.length, vector[2] / vector.length)
