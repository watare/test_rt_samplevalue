import docker as docker
import os
import toml

#identification du repertoire de travail
dir = os.getcwd()

#chargement du fichier de config
config =  toml.load('conf.toml')
for ied in config['ied']:
    if not os.path.exists(ied['id']):
        try:
            #os.mkdir('dir/'+ied['id']+'/')
            os.mkdir(ied['id'])
            print('dossier créé')
        except :
            print('erreur creation dossier')
    
    run = dir +'/'+ied['id']

    #creation du fichier de run

    f= open(run+'/samplevalue.py','w')
    f.write("import subprocess as sub\n")
    f.write("sub.run([\"/app/sv_publisher")
    f.write(' '+ied['nic'] +' '+ ied['appid']+' '+'\''+ ied['logpath'] +'\''+' '+ied['iedname']+' '+str(ied['duration'])+'\"],shell=True)')
    f.close()
    client = docker.from_env()
    client.containers.run("watar/sv:latest",
    cap_add=["SYS_ADMIN","NET_ADMIN","NET_RAW","SYS_NICE"],
    detach=True,
    volumes={run:{'bind':'/run','mode':'rw'} })
