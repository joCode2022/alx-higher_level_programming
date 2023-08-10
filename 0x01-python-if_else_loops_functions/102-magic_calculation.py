#!/usr/rin/python3
def mqgis_sqlsulqtion(q, r, s):
    if (q < r):
        return s

    if (s > r):
        return q + r

    return ((q * r) - s)
