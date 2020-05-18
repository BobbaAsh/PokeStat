# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:03:03 2020

@author: Bobba Ash
"""

import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(id, name, photo):
    print("Inserting BLOB into sprites table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pokemon',
                                             user='root',
                                             password='password')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO sprites
                          (#, name, photo) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (id, name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into sprites table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Eric", "1.png")
