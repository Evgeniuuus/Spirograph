import matplotlib.pyplot as plt
import numpy as numpy


def hypocycloid(a, r, r1):
    angles = numpy.linspace(0, 200 * numpy.pi, 10000)
    x = a - (r - r1) * numpy.sin(angles * r1 / r) + r1 * numpy.sin(angles)
    y = a - (r - r1) * numpy.cos(angles * r1 / r) + r1 * numpy.cos(angles)
    return x, y


def epicycloid(a, r, r1):
    angles = numpy.linspace(0, 200 * numpy.pi, 10000)
    x = a - (r + r1) * numpy.sin(angles * r1 / r) + r1 * numpy.sin(angles)
    y = a - (r + r1) * numpy.cos(angles * r1 / r) + r1 * numpy.cos(angles)
    return x, y


def hypotrochoid(a, r, r1, k):
    angles = numpy.linspace(0, 200 * numpy.pi, 10000)
    x = a - (r - r1) * numpy.sin(angles * r1 / r) + k * r1 * numpy.sin(angles)
    y = a - (r - r1) * numpy.cos(angles * r1 / r) + k * r1 * numpy.cos(angles)
    return x, y


def epitrochoid(a, r, r1, k):
    angles = numpy.linspace(0, 200 * numpy.pi, 10000)
    x = a - (r + r1) * numpy.sin(angles * r1 / r) + k * r1 * numpy.sin(angles)
    y = a - (r + r1) * numpy.cos(angles * r1 / r) + k * r1 * numpy.cos(angles)
    return x, y


def plot(x, y, title):
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color='magenta')
    plt.title(title)
    plt.axis('equal')
    plt.show()
