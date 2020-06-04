import sys
import pandas as pd
import sqlite3 as sq
import numpy as np


def main(points, vertices, prims, detail):

    #############################
    # Point Manipulation
    #############################

    # move points in Y direction
    points['P.Y'] += 1

    # delete point number 28
    points.drop([28], inplace=True)

    # add five new points
    for i in range(20):
        points = points.append(
            {'P.X': 0.2 * i,
             'P.Y': 0.0,
             'P.Z': 0.0}, ignore_index=True)

    # add point atribute
    points['TestAttrib'] = 'abc'

    #############################
    # Vertex Manipulation
    #############################

    # add vertex atribute
    vertices['NV'] = 'testing...'

    #############################
    # Primitive Manipulation
    #############################

    # add prim attribute
    prims['foo'] = 'myprim'

    # delete prim number 28
    prims.drop([28], inplace=True)

    #############################
    # Detail Manipulation
    #############################

    return (points, vertices, prims, detail)


if __name__ == '__main__':
    # read the argument
    db_path = sys.argv[1]

    # create db connection
    conn = sq.connect(db_path)

    # create curser
    cursor = conn.cursor()

    # retrieve all data to panda dataframe
    points = pd.read_sql_query("SELECT * FROM POINTS", conn)
    vertices = pd.read_sql_query("SELECT * FROM VERTICES", conn)
    prims = pd.read_sql_query("SELECT * FROM PRIMITIVES", conn)
    detail = pd.read_sql_query("SELECT * FROM DETAIL", conn)

    # execute
    points, vertices, prims, detail = main(points, vertices, prims, detail)

    # write to db
    points.to_sql(name="POINTS_NEW", con=conn, index=False)
    vertices.to_sql(name="VERTICES_NEW", con=conn, index=False)
    prims.to_sql(name="PRIMITIVES_NEW", con=conn, index=False)
    detail.to_sql(name="DETAIL_NEW", con=conn, index=False)
