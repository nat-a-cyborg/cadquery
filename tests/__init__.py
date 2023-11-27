from cadquery import *
from OCP.gp import gp_Vec
import unittest
import sys
import os


def readFileAsString(fileName):
    with open(fileName, "r") as f:
        s = f.read()
    return s


def writeStringToFile(strToWrite, fileName):
    with open(fileName, "w") as f:
        f.write(strToWrite)


def makeUnitSquareWire():
    V = Vector
    return Wire.makePolygon(
        [V(0, 0, 0), V(1, 0, 0), V(1, 1, 0), V(0, 1, 0), V(0, 0, 0)]
    )


def makeUnitCube(centered=True):
    return makeCube(1.0, centered)


def makeCube(size, xycentered=True):
    if xycentered:
        return Workplane().rect(size, size).extrude(size).val()
    else:
        return Solid.makeBox(size, size, size)


def toTuple(v):
    """convert a vector or a vertex to a 3-tuple: x,y,z"""
    if type(v) == gp_Vec:
        return (v.X(), v.Y(), v.Z())
    elif type(v) == Vector:
        return v.toTuple()
    else:
        raise RuntimeError(f"dont know how to convert type {str(type(v))} to tuple")


class BaseTest(unittest.TestCase):
    def assertTupleAlmostEquals(self, expected, actual, places, msg=None):
        for i, j in zip(actual, expected):
            self.assertAlmostEqual(i, j, places, msg=msg)


__all__ = [
    "TestCadObjects",
    "TestCadQuery",
    "TestCQGI",
    "TestCQSelectors",
    "TestCQSelectors",
    "TestExporters",
    "TestImporters",
    "TestJupyter",
    "TestWorkplanes",
]
