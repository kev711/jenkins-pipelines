from os import environ
from fabric import Connection  
import os
import shutil
import re
import glob
import subprocess

def getConnection():
    return Connection(
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
