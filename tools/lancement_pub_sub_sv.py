import docker as docker
import os

dir = os.getcwd()
run = dir + "/run"
client = docker.from_env()
client.containers.run("watar/sv:latest",
cap_add=["SYS_ADMIN","NET_ADMIN","NET_RAW","SYS_NICE"],
detach=True,
volumes={run:{'bind':'/run','mode':'rw'} })
