#construction de l'image docker
import subprocess as sub
import docker as docker
import os

dir=os.getcwd()
client = docker.from_env()
image = client.images.build(path=dir,tag="watar/sv:latest")

