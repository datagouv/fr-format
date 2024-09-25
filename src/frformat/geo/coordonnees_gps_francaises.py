from shapely.geometry import Point, shape
from shapely.geometry.base import BaseGeometry

from frformat import Metadata

name = "Coordonnées GPS françaises"
description = """Check that GPS coordinates are in a bounding box approximating France (including DOM)"""

FRANCE_BOUNDING_BOXES = [
    {
        "nom": "Guadeloupe",
        "depts": "971",
        "x_min": -61.809839,
        "y_min": 15.832041,
        " x_max": -61.001959,
        "y_max": 16.514488,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-61.809839, 15.832041],
                    [-61.001959, 15.832041],
                    [-61.001959, 16.514488],
                    [-61.809839, 16.514488],
                    [-61.809839, 15.832041],
                ]
            ],
        },
    },
    {
        "nom": "Martinique",
        "depts": "972",
        "x_min": -61.229033,
        "y_min": 14.388646,
        " x_max": -60.809655,
        "y_max": 14.878723,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-61.229033, 14.388646],
                    [-60.809655, 14.388646],
                    [-60.809655, 14.878723],
                    [-61.229033, 14.878723],
                    [-61.229033, 14.388646],
                ]
            ],
        },
    },
    {
        "nom": "Guyane",
        "depts": "973",
        "x_min": -54.60239,
        "y_min": 2.111055,
        " x_max": -51.619041,
        "y_max": 5.748138,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-54.60239, 2.111055],
                    [-51.619041, 2.111055],
                    [-51.619041, 5.748138],
                    [-54.60239, 5.748138],
                    [-54.60239, 2.111055],
                ]
            ],
        },
    },
    {
        "nom": "La Réunion",
        "depts": "974",
        "x_min": 55.216526,
        "y_min": -21.389631,
        " x_max": 55.836654,
        "y_max": -20.8718,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [55.216526, -21.389631],
                    [55.836654, -21.389631],
                    [55.836654, -20.8718],
                    [55.216526, -20.8718],
                    [55.216526, -21.389631],
                ]
            ],
        },
    },
    {
        "nom": "Mayotte",
        "depts": "976",
        "x_min": 45.01833,
        "y_min": -13.005254,
        " x_max": 45.299985,
        "y_max": -12.63659,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [45.01833, -13.005254],
                    [45.299985, -13.005254],
                    [45.299985, -12.63659],
                    [45.01833, -12.63659],
                    [45.01833, -13.005254],
                ]
            ],
        },
    },
    {
        "nom": "France",
        "depts": "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,2A,2B,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95",
        "x_min": -5.141277,
        "y_min": 41.333571,
        " x_max": 9.560091,
        "y_max": 51.088989,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-5.141277, 41.333571],
                    [9.560091, 41.333571],
                    [9.560091, 51.088989],
                    [-5.141277, 51.088989],
                    [-5.141277, 41.333571],
                ]
            ],
        },
    },
]


def create_polygons() -> list[BaseGeometry]:
    geoms = [region["geometry"] for region in FRANCE_BOUNDING_BOXES]
    polys = [shape(geom) for geom in geoms]
    return polys


POLYGONS: list[BaseGeometry] = create_polygons()


def is_point_in_france(coordonnees_xy: tuple[float, float]) -> bool:
    """Returns True if the point is in metropolitan France, Guadeloupe, Martinique,
    Guyane, la Réunion or Mayotte. As we are using bounding boxes (with a small margin),
    locations outside of France but quite close by may return True.
    """
    p = Point(*coordonnees_xy)
    return any(p.within(poly) for poly in POLYGONS)


class CoordonneesGPSFrancaises:
    metadata = Metadata(name, description)

    @classmethod
    def is_valid(cls, lon: float, lat: float) -> bool:
        return is_point_in_france((lon, lat))
