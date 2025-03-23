import matplotlib.pyplot as plt
import numpy as np


dipole=np.loadtxt("Document1.txt")
dipole_anakl=np.loadtxt("Document2.txt")
dipole_kat=np.loadtxt("Document3.txt")


dipole_r=np.roll(dipole[:,1],-1)
dipole_anakl_r=np.roll(dipole_anakl[:,1],5)


radians=dipole[:,0]*np.pi/180

plt.figure(1)
ax=plt.subplot(111,projection='polar')
#1 αριθμός γραμμών στο πλέγμα
#1 αριθμός στηλών στο πλέγμα
#1 θέση του subplot στο πλέγμα

ax.plot(radians,dipole_r,label="Dipole")
ax.plot(radians,dipole_anakl_r,label="Ανακλαστήρας")
ax.plot(radians,dipole_kat[:,1],label="Κατευθυντήρας")

ax=plt.gca()

plt.title("Radiation Diagram -E field",y=1.1)
ax.legend(loc="lower left",bbox_to_anchor=(-0.4,-0.1))
ax.set_yticks([-25, -20 , -15, -10, -5 ,0])
plt.show()



yagi_3=np.loadtxt("Document4.txt")
yagi_3_r=np.roll(yagi_3[:,1],-11)

yagi_3_strict=np.loadtxt("Document5.txt")
yagi_3_strict_r=np.roll(yagi_3_strict[:,1],-9)



plt.figure(2)

ax2=plt.subplot(111,projection='polar')

ax2.plot(radians,yagi_3_r,label="Random Distance")
ax2.plot(radians,yagi_3_strict_r,label="Accurate Distance")

ax2.legend(loc="lower left",bbox_to_anchor=(-0.4,-0.1))
ax2.set_yticks([-25, -20, -15, -10 ,-5,0])
plt.title("Rdiatiom Diagram - E plane",y=1.1)

plt.show()
