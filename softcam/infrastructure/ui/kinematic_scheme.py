
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import domain.services.unitees as unit


scale_vector = 5

alpha = 10*unit.DEGREE_TO_RADIAN
gamma0 = 93.636*unit.DEGREE_TO_RADIAN
theta = 24*unit.DEGREE_TO_RADIAN
beta = -13*unit.DEGREE_TO_RADIAN
delta = 15.1*unit.DEGREE_TO_RADIAN
l_ling = 38.001
rpc = 10.5
rps = 16.5
rb = 16
dsoup = 6
levee = 7.94

ipc_min = -25*unit.DEGREE_TO_RADIAN
ipc_max = 30*unit.DEGREE_TO_RADIAN
ips_min = -25*unit.DEGREE_TO_RADIAN
ips_max = 35*unit.DEGREE_TO_RADIAN

#Repère lié à la Soupape
o = np.array([0, 0, 0])
x = np.array([1, 0, 0])
y1 = np.array([0, 1, 0])
z1 = np.array([0, 0, 1])
os = -levee*z1

#Repère lié au moteur
y0 = np.cos(alpha)*y1 - np.sin(alpha)*z1
z0 = np.sin(alpha)*y1 + np.cos(alpha)*z1

#Repère lié au linguet
ol = 35.66*y1 + 0.013*z1
y2 = np.cos(beta)*y1 + np.sin(beta)*z1
z2 = -np.sin(beta)*y1 + np.cos(beta)*z1
y2_pclim_left = np.cos(beta - np.pi/2 + ipc_max)*y1 + np.sin(beta - np.pi/2 + ipc_max)*z1
y2_pclim_right = np.cos(beta - np.pi/2 + ipc_min)*y1 + np.sin(beta - np.pi/2 + ipc_min)*z1
y2_pslim_right = np.cos(beta - np.pi/2 + ips_max)*y1 + np.sin(beta - np.pi/2 + ips_max)*z1
y2_pslim_left = np.cos(beta - np.pi/2 + ips_min)*y1 + np.sin(beta - np.pi/2 + ips_min)*z1

oa = ol - l_ling*y2
ois = oa - rps*z1

#Repère lié à la Came
oc = 14.21*y1 + 31.850*z1
y3_init = np.cos(gamma0)*y1 + np.sin(gamma0)*z1
z3_init = -np.sin(gamma0)*y1 + np.cos(gamma0)*z1
y3 = np.cos(theta + gamma0)*y1 + np.sin(theta + gamma0)*z1
z3 = -np.sin(theta + gamma0)*y1 + np.cos(theta + gamma0)*z1
ob0 = oc - (rb + rpc)*y3_init
ob = 12.19*y1 + 2.73*z1
opb = ob + 2.3*z2

#Repère Mobile au Point de Contact Linguet Came
t23 = np.cos(delta)*y1 + np.sin(delta)*z1
n23 = -np.sin(delta)*y1 + np.cos(delta)*z1
oic = ob + rpc*n23

fig, ax = plt.subplots()

def create_pts():
    return 42

def create_csys(pts, x, y, z):
    return 42

def create_joints(pts, radius):
    return 42

def create_soupape():
    return 42

def create_linguet():
    return 42

def create_came():
    return 42

ax.set_aspect('equal', adjustable='box')
plt.plot(o[1], o[2], "+", color="black")
plt.plot(ol[1], ol[2], "+", color="red")
plt.plot(oc[1], oc[2], "+", color="green")
plt.plot(os[1], os[2], "+", color="blue")
plt.plot(oa[1], oa[2], ".", color="red")
plt.plot(ois[1], ois[2], "+", color="blue")
plt.plot(ob[1], ob[2], ".", color="red")
plt.plot(ob0[1], ob0[2], ".", color="magenta")
plt.plot(oic[1], oic[2], "+", color="black")

plt.arrow(o[1], o[2], scale_vector*y1[1], scale_vector*y1[2], color="blue", width=0.01, head_width = 0.3)
plt.arrow(o[1], o[2], scale_vector*z1[1], scale_vector*z1[2], color="blue", width=0.01, head_width = 0.3)
plt.arrow(ol[1], ol[2], scale_vector*y2[1], scale_vector*y2[2], color="red", width=0.01, head_width = 0.3)
plt.arrow(ol[1], ol[2], scale_vector*z2[1], scale_vector*z2[2], color="red", width=0.01, head_width = 0.3)
plt.arrow(oc[1], oc[2], scale_vector*y3[1], scale_vector*y3[2], color="green", width=0.01, head_width = 0.3)
plt.arrow(oc[1], oc[2], scale_vector*z3[1], scale_vector*z3[2], color="green", width=0.01, head_width = 0.3)
plt.arrow(o[1], o[2], scale_vector*y0[1], scale_vector*y0[2], color="black", width=0.01, head_width = 0.3)
plt.arrow(o[1], o[2], scale_vector*z0[1], scale_vector*z0[2], color="black", width=0.01, head_width = 0.3)
plt.arrow(oc[1], oc[2], scale_vector*y3_init[1], scale_vector*y3_init[2], color="black", width=0.01, head_width = 0.3)
plt.arrow(oc[1], oc[2], scale_vector*z3_init[1], scale_vector*z3_init[2], color="black", width=0.01, head_width = 0.3)
plt.arrow(oic[1], oic[2], scale_vector*t23[1], scale_vector*t23[2], color="black", width=0.01, head_width = 0.3)
plt.arrow(oic[1], oic[2], scale_vector*n23[1], scale_vector*n23[2], color="black", width=0.01, head_width = 0.3)

#Display Soupape
haut_soupape = np.array([os - dsoup/2*y1, os + dsoup/2*y1]).T
queue_soupape = np.array([os, os - 10*z1]).T
plt.plot(haut_soupape[1], haut_soupape[2], color = "blue")
plt.plot(queue_soupape[1], queue_soupape[2], color = "blue")

#Display Linguet
longueur_linguet = np.array([ol, oa]).T
hauteur_linguet = np.array([ob, opb]).T
lim_patin_came_droit = np.array([ob, ob - rpc*y2_pclim_right]).T
lim_patin_came_gauche = np.array([ob, ob - rpc*y2_pclim_left]).T
lim_patin_soupape_droit = np.array([oa, oa + rps*y2_pslim_right]).T
lim_patin_soupape_gauche = np.array([oa, oa + rps*y2_pslim_left]).T
plt.plot(longueur_linguet[1], longueur_linguet[2], color = "red")
plt.plot(hauteur_linguet[1], hauteur_linguet[2], color = "red")
plt.plot(lim_patin_came_droit[1], lim_patin_came_droit[2], color = "red")
plt.plot(lim_patin_came_gauche[1], lim_patin_came_gauche[2], color = "red")
plt.plot(lim_patin_soupape_droit[1], lim_patin_soupape_droit[2], color = "red")
plt.plot(lim_patin_soupape_gauche[1], lim_patin_soupape_gauche[2], color = "red")

arc_patin_came = ptc.Arc(
    ob[1:], 
    width = 2*rpc, height = 2*rpc, 
    angle = (beta + np.pi/2 + ipc_min)/unit.DEGREE_TO_RADIAN, 
    theta1 = 0, 
    theta2 = (ipc_max - ipc_min)/unit.DEGREE_TO_RADIAN, 
    color="red",
    linewidth = 1.5
    )
arc_patin_soup = ptc.Arc(
    oa[1:], 
    width = 2*rps, 
    height = 2*rps, 
    angle = (beta - np.pi/2 + ipc_min)/unit.DEGREE_TO_RADIAN, 
    theta1 = 0, 
    theta2 = (ips_max - ips_min)/unit.DEGREE_TO_RADIAN, 
    color="red",
    linewidth = 1.5
    )
arc_came_base = ptc.Arc(
    oc[1:], 
    width = 2*rb, 
    height = 2*rb, 
    angle = (theta + gamma0)/unit.DEGREE_TO_RADIAN, 
    theta1 = 180, 
    theta2 = 0, 
    color="green",
    linewidth = 1.5
    )
arc_came_levee = ptc.Arc(
    oc[1:], 
    width = 2*rb, 
    height = 4*rb, 
    angle = (theta + gamma0)/unit.DEGREE_TO_RADIAN, 
    theta1 = 0, 
    theta2 = 180, 
    color="green",
    linewidth = 1.5
    )

ax.add_patch(arc_patin_came)
ax.add_patch(arc_patin_soup)
ax.add_patch(arc_came_base)
ax.add_patch(arc_came_levee)

plt.show()


if __name__=="__main__":
    a = [0, 14.21, 31.850]
    b = [0, 35.66, 0.013]
    print(a + b)
    print(oc + ol)