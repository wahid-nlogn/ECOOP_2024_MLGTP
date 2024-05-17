import random
from functools import reduce
from math import log2, floor, ceil
from itertools import combinations
from subprocess import Popen, PIPE
import os
import ast

starter = """

import array
import math
import time
from six.moves import xrange


DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 100
EPSILON = 0.00001
ZERO = (0, 0, 0)#vector(0, 0, 0)
RIGHT = (1, 0, 0)#vector(1, 0, 0)
UP = (0, 1, 0)#vector(0, 1, 0)
OUT = (0, 0, 1)#vector(0, 0, 1)

"""

vector_headers = ["def vector(initx, inity, initz)->Tuple(Dyn,Dyn,Dyn):"]

vector_body = """
    return (initx, inity, initz)

"""

#def vectorstr(vec):
#    (x,y,z) = vec
#    return '(%s,%s,%s)' % (x, y, z)

#def __repr__(vec):
#    (x,y,z) = vec
#    return 'Vector(%s,%s,%s)' % (x, y, z)

dot_headers = ["def dot(vec, other):","def dot(vec:Tuple(Dyn,Dyn,Dyn), other)->float:","def dot(vec, other:Tuple(Dyn,Dyn,Dyn))->float:","def dot(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->float:"]

dot_body = """
    #other.mustBeVector()
    (x,y,z) = vec
    (x1, y1, z1) = other
    return (x * x1 * 1.0) + (y * y1 * 1.0) + (z * z1 * 1.0)

"""

magnitude_headers = ["def magnitude(vec):","def magnitude(vec:Tuple(Dyn,Dyn,Dyn))->float:"]
magnitude_body = """
    return (math.sqrt(dot(vec, vec)) + 0.0)

"""

add_headers = ["def add(vec, other):","def add(vec:Tuple(Dyn,Dyn,Dyn), other)-> Tuple(Dyn,Dyn,Dyn):", "def add(vec, other:Tuple(Dyn,Dyn,Dyn))-> Tuple(Dyn,Dyn,Dyn):", "def add(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))-> Tuple(Dyn,Dyn,Dyn):"]
add_body = """
    (x,y,z) = vec
    (x1,y1,z1) = other
    return (x+x1, y+y1, z+z1)
    #if other.isPoint():
        #return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    #else:
        #return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

"""
sub_headers = ["def sub(vec, other):","def sub(vec:Tuple(Dyn,Dyn,Dyn), other)->Tuple(Dyn,Dyn,Dyn):","def sub(vec, other:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):","def sub(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):"]
sub_body = """
    #other.mustBeVector()
    (x,y,z) = vec
    (x1,y1,z1) = other
    return vector(x - x1, y - y1, z - z1)

"""

scale_headers = ["def scale(vec, factor):","def scale(vec:Tuple(Dyn,Dyn,Dyn), factor)->Tuple(Dyn,Dyn,Dyn):"]
scale_body = """
    x,y,z = vec
    return (factor * x, factor * y, factor * z)

"""

    
cross_headers = ["def cross(vec, other):","def cross(vec:Tuple(Dyn,Dyn,Dyn), other)->Tuple(Dyn,Dyn,Dyn):","def cross(vec, other:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):","def cross(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):"]
cross_body = """
    #other.mustBeVector()
    (x,y,z) = vec
    (x1,y1,z1) = other
    return (y * z1 - z * y1,
                      z * x1 - x * z1,
                      x * y1 - y * x1)

"""

normalized_headers = ["def normalized(vec):","def normalized(vec:Tuple(Dyn,Dyn,Dyn))-> Tuple(Dyn,Dyn,Dyn):"]
normalized_body = """
    return scale(vec, 1.0 / magnitude(vec))

"""

negated_headers = ["def negated(vec):","def negated(vec:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):"]
negated_body = """
    return scale(vec, -1)

"""

eq_headers = ["def eq(vec, other)->Bool:","def eq(vec:Tuple(Dyn,Dyn,Dyn), other)->Bool:","def eq(vec, other:Tuple(Dyn,Dyn,Dyn))->Bool:","def eq(vec:Tuple(Dyn,Dyn,Dyn), other:Tuple(Dyn,Dyn,Dyn))->Bool:"]
eq_body = """
    x,y,z = vec
    x1,y1,z1 = other
    return (x == x1) and (y == y1) and (z == z1)

"""

#def isVector(self):
#    return True

#def isPoint(self):
#    return False

#def mustBeVector(self):
#    return self

#def mustBePoint(self):
#    raise 'Vectors are not points!'

reflectThrough_headers = ["def reflectThrough(vec, normal):",
                          "def reflectThrough(vec:Tuple(Dyn,Dyn,Dyn), normal)->Tuple(Dyn,Dyn,Dyn):",
                          "def reflectThrough(vec, normal:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):",
                          "def reflectThrough(vec:Tuple(Dyn,Dyn,Dyn), normal:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):"]
reflectThrough_body = """
    d = scale(normal, dot(vec, normal))
    return sub(vec, scale(d,2))

"""




#assert Vector.RIGHT.reflectThrough(Vector.UP) == Vector.RIGHT
#assert Vector(-1, -1, 0).reflectThrough(Vector.UP) == Vector(-1, 1, 0)


#class Point(object):

#    def __init__(self, initx, inity, initz):
#        self.x = initx
#        self.y = inity
#        self.z = initz

#    def __str__(self):
#        return '(%s,%s,%s)' % (self.x, self.y, self.z)

#    def __repr__(self):
#        return 'Point(%s,%s,%s)' % (self.x, self.y, self.z)

#    def __add__(self, other):
#        other.mustBeVector()
#        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

#    def __sub__(self, other):
#        if other.isPoint():
#            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
#        else:
#            return Point(self.x - other.x, self.y - other.y, self.z - other.z)

#    def isVector(self):
#        return False

#    def isPoint(self):
#        return True

#    def mustBeVector(self):
#        raise 'Points are not vectors!'

#    def mustBePoint(self):
#        return self


#class Sphere(object):

sphere_headers = ["def sphere(centre, radius)->Tuple(Dyn,Dyn):"]
sphere_body = """
    #centre.mustBePoint()
    #self.centre = centre
    #self.radius = radius
    return (centre, radius)
"""

#def __repr__(self):
#    return 'Sphere(%s,%s)' % (repr(self.centre), self.radius)

#class Ray(object):

ray_headers = ["def ray(point, vect):","def ray(point, vect:Tuple(Dyn,Dyn,Dyn)):"]
ray_body = """
    #self.point = point
    #self.vector = vector.normalized()
    return (point, normalized(vect))

"""

#def __repr__(self):
#    return 'Ray(%s,%s)' % (repr(self.point), repr(self.vector))

pointAtTime_headers = ["def pointAtTime(ray, t)->Tuple(Dyn,Dyn,Dyn):"]
pointAtTime_body = """
    point, vector = ray
    return add(point, scale(vector, t))

"""

intersectionTime_headers = ["def intersectionTime(s, ra):",
                            "def intersectionTime(s:Tuple(Tuple(Dyn,Dyn,Dyn),Dyn), ra):",
                            "def intersectionTime(s, ra:Tuple(Tuple(Dyn,Dyn,Dyn),Tuple(Dyn,Dyn,Dyn))):",
                            "def intersectionTime(s:Tuple(Tuple(Dyn,Dyn,Dyn),Dyn), ra:Tuple(Tuple(Dyn,Dyn,Dyn),Tuple(Dyn,Dyn,Dyn))):"]
intersectionTime_body = """
    (centre, radius) = s
    (point, vect) = ra
    cp = sub(centre, point)
    v = dot(cp, vect)
    discriminant = (radius * radius) - (dot(cp, cp) - v * v)
    if discriminant < 0:
        return None
    else:
        return v - math.sqrt(discriminant)

"""

normalAt_headers = ["def normalAt(s, p):",
                    "def normalAt(s:Tuple(Tuple(Dyn,Dyn,Dyn),Dyn), p)->Tuple(Dyn,Dyn,Dyn):",
                    "def normalAt(s, p:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):",
                    "def normalAt(s:Tuple(Tuple(Dyn,Dyn,Dyn),Dyn), p:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn,Dyn,Dyn):"]
normalAt_body = """
    (centre, radius) = s
    return normalized((sub(p,  centre)))
    
"""


#class Halfspace(object):

halfspace_headers = ["def halfspace(point, normal):",
                     "def halfspace(point, normal:Tuple(Dyn,Dyn,Dyn))->Tuple(Dyn, Tuple(Dyn,Dyn,Dyn)):"]
halfspace_body = """
    #self.point = point
    #self.normal = normal.normalized()
    return (point, normalized(normal))
"""

#def __repr__(self):
#    return 'Halfspace(%s,%s)' % (repr(self.point), repr(self.normal))

intersectionTime1_headers = ["def intersectionTime1(hs, ray)->float:",
                            "def intersectionTime1(hs:Tuple(Dyn,Tuple(Dyn,Dyn,Dyn)), ray)->float:",
                            "def intersectionTime1(hs, ray:Tuple(Dyn,Tuple(Dyn,Dyn,Dyn)))->float:",
                            "def intersectionTime1(hs:Tuple(Dyn,Tuple(Dyn,Dyn,Dyn)), ray:Tuple(Dyn,Tuple(Dyn,Dyn,Dyn)))->float:"]
intersectionTime1_body = """
    point, vector = ray
    (point, normal) = hs
    v = dot(vector, normal)
    if v:
        return 1 / -v
    return -1.0

"""

normalAt1_headers = ["def normalAt1(hs, p):",
                    "def normalAt1(hs:Tuple(Dyn,Dyn), p):"]
normalAt1_body = """
    (p1, normal) = hs
    return normal

"""





#Point.ZERO = Point(0, 0, 0)


#class Canvas(object):

canvas_headers = ["def canvas(width, height)->Tuple(Dyn,Dyn,int):"]
canvas_body = """
    byts = array.array('B', [0] * (width * height * 3))
    #byts = [0] * (width * height * 3)
    for i in xrange(width * height):
        #0
        byts[i * 3 + 2] = 255
    #self.width = width
    #self.height = height
    return (byts, width, height)

"""

plot_headers = ["def plot(canv, x, y, r, g, b):",
                "def plot(canv:Tuple(Dyn,Dyn,Dyn), x, y, r, g, b):",
                "def plot(canv, x:int, y, r, g, b):",
                "def plot(canv, x, y:int, r, g, b):",
                "def plot(canv, x, y, r:int, g, b):",
                "def plot(canv, x, y, r, g:int, b):",
                "def plot(canv, x, y, r, g, b:int):",
                "def plot(canv:Tuple(Dyn,Dyn,Dyn), x:int, y:int, r:int, g:int, b:int):"]
plot_body = """
    (byts, width, height) = canv
    i = ((height - y - 1) * width + x) * 3
    byts[i] = max(0, min(255, int(r * 255)))
    byts[i + 1] = max(0, min(255, int(g * 255)))
    byts[i + 2] = max(0, min(255, int(b * 255)))
    return None

"""

#def write_ppm(self, filename):
#    header = 'P6 %d %d 255\n' % (self.width, self.height)
#    with open(filename, "wb") as fp:
#        fp.write(header.encode('ascii'))
#        fp.write(self.bytes.tostring())

firstIntersection_headers = ["def firstIntersection(intersections):",
                             "def firstIntersection(intersections:List(Dyn)):"]
firstIntersection_body = """
    result = None
    for i in intersections:
        candidateT = i[1]
        if candidateT is not None and candidateT > -EPSILON:
            if result is None or candidateT < result[1]:
                result = i
    return result

"""


#class Scene(object):
scene_headers = ["def scene()->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Int):"]

scene_body = """
    objects = []
    lightPoints = []
    position = vector(0.0, 1.8, 10.0)
    lookingAt = (0.0,0.0,0.0)#Point.ZERO
    fieldOfView = 45
    recursionDepth = 0
    return (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

"""

moveTo_headers = ["def moveTo(sc, p):",
                  "def moveTo(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p)->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):"]
moveTo_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    position = p
    return (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

"""

lookAt_headers = ["def lookAt(sc, p):","def lookAt(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p)->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):"]
lookAt_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    lookingAt = p
    return (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

"""

addObject_headers = ["def addObject(sc, object, surface):","def addObject(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), object, surface)-> Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):"]
addObject_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    objs = [] + objects
    objs.append((object, surface))
    return (objs, lightPoints, position, lookingAt, fieldOfView, recursionDepth)

"""

addLight_headers = ["def addLight(sc, p):","def addLight(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p)->Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn):"]
addLight_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    lps = [] + lightPoints
    lps.append(p)
    return (objects, lps, position, lookingAt, fieldOfView, recursionDepth)

"""

addColours_headers = ["def addColours(a, scale, b)->Tuple(Dyn,Dyn,Dyn):"]
addColours_body = """
    return (a[0] + scale * b[0],
            a[1] + scale * b[1],
            a[2] + scale * b[2])

"""

baseColourAt_headers = ["def baseColourAt(ss, p):","def baseColourAt(ss:Tuple(Dyn,Dyn,Dyn,Dyn), p):"]
baseColourAt_body = """
    (baseColour, specularCoefficient, lambertCoefficient, ambientCoefficient) = ss
    return baseColour

"""

colourAt_headers = ["def colourAt(ss, scene1, ray1, p1, normal1):",
                    "def colourAt(ss, scene1, ray1, p1:Tuple(Dyn,Dyn,Dyn), normal1):",
                    "def colourAt(ss, scene1, ray1, p1, normal1:Tuple(Dyn,Dyn,Dyn)):"
                    "def colourAt(ss:Tuple(Dyn,Dyn,Dyn,Dyn), scene1, ray1, p1, normal1):",
                    "def colourAt(ss, scene1, ray1:Tuple(Tuple(Dyn,Dyn,Dyn),Tuple(Dyn,Dyn,Dyn)), p1, normal1):",
                    "def colourAt(ss:Tuple(Dyn,Dyn,Dyn,Dyn), scene1, ray1:Tuple(Tuple(Dyn,Dyn,Dyn),Tuple(Dyn,Dyn,Dyn)), p1, normal1):",
                    "def colourAt(ss:Tuple(Dyn,Dyn,Dyn,Dyn), scene1, ray1:Tuple(Tuple(Dyn,Dyn,Dyn),Tuple(Dyn,Dyn,Dyn)), p1, normal1:Tuple(Dyn,Dyn,Dyn)):"]
colourAt_body = """
    (baseColour, specularCoefficient, lambertCoefficient, ambientCoefficient)
    b = baseColourAt(ss, p)
    (p,v) = ray1

    c = (0, 0, 0)
    if specularCoefficient > 0:
        reflectedRay = ray(p1, reflectThrough(v, vnormal))
        reflectedColour = rayColour(scene1,reflectedRay)
        c = addColours(c, specularCoefficient, reflectedColour)

    if lambertCoefficient > 0:
        lambertAmount = 0
        for lightPoint in visibleLights(scene1, p1):
            contribution = dot(normalized((sub(lightPoint, p1))), normal)
            if contribution > 0:
                lambertAmount = lambertAmount + contribution
        lambertAmount = min(1, lambertAmount)
        c = addColours(c, lambertCoefficient * lambertAmount, b)

    if ambientCoefficient > 0:
        c = addColours(c, ambientCoefficient, b)

    return c

"""


rayColour_headers = ["def rayColour(sc, ry):",
                     "def rayColour(sc, ry:Tuple(Dyn,Dyn,Dyn)):"]
rayColour_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    if recursionDepth > 3:
        return (0.0, 0.0, 0.0)
    try:
        recursionDepth = recursionDepth + 1
        intersections = [(o, intersectionTime(o,ry), s)
                             for (o, s) in objects]
        i = firstIntersection(intersections)
        if i is None:
            return (0.0, 0.0, 0.0)  # the background colour
        else:
            (o, t, s) = i
            p = pointAtTime(ry, t)
            return colourAt(s, sc, ry, p, o.normalAt(p))
    finally:
        recursionDepth = recursionDepth - 1
    return (0.0,0.0,0.0)

"""

render_headers = ["def render(sc, canvas1):",
                  "def render(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), canvas1):"]
render_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    fovRadians = math.pi * (fieldOfView / 2.0) / 180.0
    halfWidth = math.tan(fovRadians)
    halfHeight = 0.75 * halfWidth
    width = halfWidth * 2
    height = halfHeight * 2
    bytes, w, h = canvas1
    pixelWidth = width / (w - 1)
    pixelHeight = height / (h - 1)

    eye = ray(position, sub(lookingAt, position))
    p, v = eye    
    vpRight = normalized(cross(v, UP))
    vpUp = normalized(cross(vpRight, v))

    for y in xrange(int(height)):
        for x in xrange(int(width)):
            xcomp = scale(vpRight, x * pixelWidth - halfWidth)
            ycomp = scale(vpUp, y * pixelHeight - halfHeight)
            r = ray(p, add(add(v, xcomp), ycomp))
            #colour = rayColour(sc, r)
            #plot(canvas1, x, y, *colour)

    return None

"""

lightIsVisible_headers = ["def lightIsVisible(sc, l, p):",
                          "def lightIsVisible(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), l, p):"]
lightIsVisible_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    for (o, s) in objects:
        t = intersectionTime(o, ray(p, sub(l, p)))
        if t is not None and t > EPSILON:
            return False
    return True

"""
visibleLights_headers = ["def visibleLights(sc, p):","def visibleLights(sc:Tuple(Dyn,Dyn,Dyn,Dyn,Dyn,Dyn), p):"]
visibleLights_body = """
    (objects, lightPoints, position, lookingAt, fieldOfView, recursionDepth) = sc
    result = []
    for l in lightPoints:
        if lightIsVisible(sc, l, p):
            result.append(l)
    return result

"""




#class SimpleSurface(object):

simpleSurface_headers = ["def simpleSurface(baseColour)->Tuple(Dyn,Float,Float,Dyn):"]
simpleSurface_body = """
    #baseColour = kwargs.get('baseColour', (1, 1, 1))
    specularCoefficient = 0.2
    lambertCoefficient =  0.6
    ambientCoefficient = 1.0 - specularCoefficient - lambertCoefficient
    return (baseColour, specularCoefficient, lambertCoefficient, ambientCoefficient)

"""


#class CheckerboardSurface(SimpleSurface):

#    def __init__(self, **kwargs):
#        SimpleSurface.__init__(self, **kwargs)
#        self.otherColour = kwargs.get('otherColour', (0, 0, 0))
#        self.checkSize = kwargs.get('checkSize', 1)

#    def baseColourAt(self, p):
#        v = p - Point.ZERO
#        v.scale(1.0 / self.checkSize)
#        if (int(abs(v.x) + 0.5) +
#            int(abs(v.y) + 0.5) +
#            int(abs(v.z) + 0.5)) \
#           % 2:
#            return self.otherColour
#        else:
#            return self.baseColour

bench_raytrace_headers = ["def bench_raytrace(loops, width, height, filename):"]
bench_raytrace_body = """
    range_it = xrange(loops)
    #t0 = perf.perf_counter()

    for i in range_it:
        #canvas1 = canvas(width, height)
        s = scene()
        addLight(s, vector(30, 30, 10))
        addLight(s, vector(-10, 100, 30))
        lookAt(s, vector(0, 3, 0))
        addObject(s, sphere(vector(1, 3, -10), 2),
                    simpleSurface((1, 1, 0)))
        for y in xrange(6):
            addObject(s,sphere(vector(-3 - y * 0.4, 2.3, -5), 0.4),
                        simpleSurface((y / 6.0, 1 - y / 6.0, 0.5)))
            scale(normalized(vector(10,23,19)), y * 11)
        #s.addObject(Halfspace(Point(0, 0, 0), Vector.UP),
        #            CheckerboardSurface())
        #render(s,canvas1)
    return None

"""

rest = """

    #dt = perf.perf_counter() - t0

    #if filename:
    #    canvas.write_ppm(filename)
    #return dt
def main():
    t0 = time.time()
    bench_raytrace(100, DEFAULT_WIDTH, DEFAULT_HEIGHT, "raytrace.ppm")
    t1 = time.time()
    print(t1-t0)

main()

"""

all_bases = ["vector","dot","magnitude","add","sub","scale","cross","normalized","negated","eq","reflectThrough","sphere","ray","pointAtTime","intersectionTime","normalAt","halfspace","canvas","plot","firstIntersection","scene","moveTo","lookAt","addObject","addLight","addColours","baseColourAt","render","lightIsVisible","visibleLights","simpleSurface","bench_raytrace"]

all_headers = list(map(lambda b: b+'_headers',all_bases))
all_bodies = list(map(lambda b: b+'_body',all_bases))


# print(list(all_headers))

# all_headers = ["vector_headers","dot_headers","magnitude_headers","add_headers","sub_headers","scale_headers","cross_headers","normalized_headers","negated_headers","eq_headers","reflectThrough_headers","sphere_headers","ray_headers","pointAtTime_headers","intersectionTime_headers","normalAt_headers","halfspace_headers","canvas_headers","plot_headers","firstIntersection_headers","scene_headers","moveTo_headers","lookAt_headers","addObject_headers","addLight_headers","addColours_headers","baseColourAt_headers","render_headers","lightIsVisible_headers","visibleLights_headers","simpleSurface_headers","bench_raytrace_headers"]



# print(reduce(lambda accr, ind : accr * len(globals()[ind]), all_headers, 1) )
# print(list(map(lambda ind : (ind,len(globals()[ind])), all_headers)) )

def vary_index(headers):
    configurable_bits = []
    beginning_and_number = []
    begin = 0
    
    for header in headers:
        funcHeaders = globals()[header]
        num = floor(log2(len(funcHeaders)))
        
        assert num == ceil(log2(len(funcHeaders)))
            # sys.exit('The number of headers for', header, 'is not a power of 2')

        configurable_bits.extend(range(begin,begin+num) )
        bits_incr = 1 if num == 0 else num
        beginning_and_number.append((begin,bits_incr))
        
        begin += bits_incr
        
    number_of_bits = begin
    return (configurable_bits, beginning_and_number, number_of_bits)

def bits_to_index(bits,beginning_and_number):
    indexes = []

    for (beg,num) in beginning_and_number:
        indexes.append(reduce(lambda accr,n:2*accr+n,bits[beg:beg+num],0))

    return indexes

# print(vary_index(all_headers))

# print(bits_to_index([1,0,1,0,1,1],[(0,2),(2,1),(3,1),(4,2)]))
# print(bits_to_index([0]))
# print(bits_to_index([1,1]))
 

def config_bits_combs(configurable_bits,num_typed_bits,needed):
    if num_typed_bits <= 2 or len(configurable_bits) - num_typed_bits <= 2:
        return combinations(configurable_bits,num_typed_bits)

    generated = set()
    num = 0
    
    while num < needed :
        typed = tuple(sorted(random.sample(configurable_bits,num_typed_bits)))
        
        if typed in generated:
            continue
            
        num += 1
        generated.add(typed)
        
    return generated
        
def neighbor_bits (cur_config_bits,configurable_bits):
    neighbors = []
    for bit in configurable_bits:
        new = cur_config_bits[:]
        if cur_config_bits[bit]:
            continue
        else:
            new[bit] = 1
            neighbors.append(new)
            
    return neighbors
                
def configs_needed(num_config_bits, level, total_needed):
    up_2_untyped = 1 + num_config_bits + num_config_bits * (num_config_bits -1)/2
    up_2_typed = 1 + num_config_bits + num_config_bits * (num_config_bits -1)/2
    
    others_needed = total_needed - up_2_untyped - up_2_typed
    
    each_level = others_needed / (num_config_bits - 6)

    return each_level

CONFIG_NUM = 2**15

def add_typed (template,typed_bits):
    for bit in typed_bits:
        template[bit] = 1

def index_to_configuration(headers,bodies,indexes):
    # for header in headers:
        # print(globals()[header][0])

    # for (header,body) in zip(headers,bodies):
        # print(globals()[header][0],globals()[body])
    
    # print('Headers:', headers)
    # print('Bodies:', bodies)

        
    out = reduce(lambda accr,triple: accr+globals()[triple[0]][triple[2]]+globals()[triple[1]],zip(headers,bodies,indexes),'')
    # print(out)
    
    return out

def load_features(feature_file):
    features_list = {}
    filename = ''
    with open(feature_file,'r') as ff:
        lines = ff.readlines()
        for i in range(len(lines)):
            if i % 2 == 0:
                filename = lines[i].strip()
            else:
                features = ast.literal_eval(lines[i])
                features_list[filename] = features
                
    return features_list
                        
def gen_all_neigbhors(cur_bits,all_headers,all_bodies,starter,ender):
    (configurable_bits, beginning_and_number, number_of_bits) = vary_index (all_headers)

    cur_index = bits_to_index(cur_bits,beginning_and_number)
    feature_file = reduce(lambda accr,cur:accr+str(cur),cur_index,'')+'.txt'
    
    feature_command = 'python ../FeatureExtraction/retic.py -nli' + ' -ff ' + feature_file
    fft = {}
        
    neighbors = neighbor_bits(cur_bits,configurable_bits)
    
    for neighbor in neighbors:
        indexes = bits_to_index(neighbor,beginning_and_number)
        out = index_to_configuration(all_headers,all_bodies,indexes)

        # print(out)

        filename = 'raytrace' + reduce(lambda accr,cur:accr+str(cur),indexes,'')+'.py'
        
        with open(filename,"w+") as f:
            f.write(starter+out+ender)
            
        process = Popen(('retic ' + filename).split(), stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        
        fft[filename] = (neighbor,float(output))

        os.system(feature_command + ' ' + filename)

    file_features = load_features(feature_file)
    return merge_time_and_features(fft,file_features)

# Make sure the file named nli.txt is in the same directory as generateRayTrace.py
# Call this function with the bits in the list format to get the (bit_strings, measured_time,features) of all the neighbors in the list format. 
# An example call: return_neighbor_info([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])    

def return_neighbor_info(cur_bits):
    return gen_all_neigbhors(cur_bits,all_headers,all_bodies,starter,rest)

# return_neighbor_info([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])    
            
    
def merge_time_and_features(fft,file_features):
    results = []
    
    for fn in fft:
        bit_string,measured_time = fft[fn]
        results.append((bit_string,measured_time,file_features[fn]))
        
    return results
    

def gen_all_configs(all_headers,all_bodies,starter,ender):
    print(all_headers)
    print(list(all_headers))
    
    (configurable_bits, beginning_and_number, number_of_bits) = vary_index (all_headers)
    print(len(configurable_bits),configurable_bits)
    
    config_template = [0] * number_of_bits
    
    neighbors = neighbor_bits(config_template, configurable_bits)
    # print(neighbors)
    
    nconfig = config_template[:]
    nconfig[2] = 1
    
    results = gen_all_negibhors([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],all_headers,all_bodies,starter,ender)
    
    # print('aaaaaaaaaaaaaaaaaaaaaaaa')
    # process = Popen('retic raytrace01000000000000000000000000000100.py'.split(), stdout=PIPE)
    # (output, err) = process.communicate()
    # exit_code = process.wait()
    
    # print(output,err)
    # os.system('retic raytrace01000000000000000000000000000100.py')
    # os.system('python ../FeatureExtraction/retic.py -nli raytrace01000000000000000000000000000100.py')
    print(results)
    
    return 
    
    i = 0
    mapping = open("mapping.txt","w+")

    for level in range(len(configurable_bits)+1):
        level_configs = configs_needed(len(configurable_bits), level, CONFIG_NUM)
        generated = config_bits_combs(configurable_bits,level,level_configs)
        
        for config in generated:
            cur_config = config_template[:]
            add_typed(cur_config, config)
            
            indexes = bits_to_index(cur_config,beginning_and_number)
            out = index_to_configuration(all_headers,all_bodies,indexes)
            
            fn = "raytrace" + str(i) + ".py"
            record = fn + ';' + str(indexes)+ ';'+ str(cur_config) + '\n'
            mapping.write(record)

            f = open(fn,"w+")
            f.write(starter+out+ender)
            f.close()
            i += 1            
            
        print('-------------Processed level --------------', level)

    mapping.close()
    # print (list(combinations(configurable_bits,32)))
    
    # print(len(configurable_bits),configurable_bits)

# gen_all_configs(all_headers,all_bodies,starter,rest)
        
    
# print(index_to_configuration(all_headers,all_bodies,[0]*42))    
    
def p():
    print(globals()["vector_headers"])

# p()
