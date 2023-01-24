from os import environ
import fabric
import os
import shutil
import re
import glob
import subprocess

def getConnection():
    return fabric.Connection(
        host= "ios12902e.dc.ricohonline.org",
        user= "oraoper"
    )

def javaOperation():
    try:
        conn = getConnection()
        conn.run("pwd")
            
    except Exception as err:
        print(err)

javaOperation()
