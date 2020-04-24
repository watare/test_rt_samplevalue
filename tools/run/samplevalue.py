import subprocess as sub



sub.run(["/app/sv_publisher eth0 0x4000 '/run/log.csv' MU_POSTE_1 1"],shell=True)

f = open("dolbi.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
