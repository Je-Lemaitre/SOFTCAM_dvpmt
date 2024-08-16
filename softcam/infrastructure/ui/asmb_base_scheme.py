
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
from matplotlib.axes import Axes
import domain.services.unitees as unit
    
def create_fig(ax : Axes):

    scale_vector = 5

    alpha = 10*unit.DEGREE_TO_RADIAN
    gamma0 = 96.636*unit.DEGREE_TO_RADIAN
    theta = 0*unit.DEGREE_TO_RADIAN
    
    delta = gamma0 - np.pi/2
    l_ling = 38.001
    rpc = 10.5
    rps = 16.5
    rb = 16
    dsoup = 6
    levee = 0

    ipc_min = -10*unit.DEGREE_TO_RADIAN
    ipc_max = 50*unit.DEGREE_TO_RADIAN
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
    beta = np.arcsin((ol[2] - rps)/l_ling)
    y2 = np.cos(beta)*y1 + np.sin(beta)*z1
    z2 = -np.sin(beta)*y1 + np.cos(beta)*z1

    #Repère lié à la Came
    oc = 14.21*y1 + 31.850*z1
    y3 = np.cos(theta + gamma0)*y1 + np.sin(theta + gamma0)*z1
    z3 = -np.sin(theta + gamma0)*y1 + np.cos(theta + gamma0)*z1
    ob = oc - (rb + rpc)*y3
    # fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    # Move the left and bottom spines to zero position
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    # Hide the right and top spines
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # Set the ticks position to bottom and left
    ax.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 

    def create_pts():
        return 42

    def create_revolute_joint(pts, ax : Axes, radius=1, color="black"):
        revolute_joint = ptc.Circle(
            pts[1:], 
            radius = radius,
            edgecolor =color,
            fill = False,
            linewidth = 1.5
            )
        ax.add_patch(revolute_joint)
        return revolute_joint

    def create_csys(pts, y, z, ax : Axes, num = 1, radius_joint=0, scale = 1, color="black"):
        y_start = pts + radius_joint*y
        z_start = pts + radius_joint*z
        y_disp = scale*y
        z_disp = scale*z
        y_end = pts + y_disp
        z_end = pts + z_disp
        ax.arrow(y_start[1], y_start[2], y_disp[1], y_disp[2], color=color, width=0.005, head_width = 0.3)
        ax.arrow(z_start[1], z_start[2], z_disp[1], z_disp[2], color=color, width=0.005, head_width = 0.3)
        return y_end, z_end

    def create_soupape(pts_s, y, z, dsoup=6, lsoup=10):
        
        y_end, z_end = create_csys(pts_s, y, z, ax, num=1, radius_joint=0, scale=5, color="blue")
        
        haut_soupape = np.array([pts_s - dsoup/2*y, pts_s + dsoup/2*y]).T
        queue_soupape = np.array([pts_s, pts_s - lsoup*z]).T
        ax.plot(haut_soupape[1], haut_soupape[2], color = "blue")
        ax.plot(queue_soupape[1], queue_soupape[2], color = "blue")

        return y_end, z_end

    def create_linguet(pts_l, pts_b, y, z, rpc, rps, l_ling, ipcmin, ipcmax, ipsmin, ipsmax, ax : Axes, radius_joint=0):
        
        y_end, z_end = create_csys(pts_l, y, z, ax, num=2, radius_joint=1, scale=5, color="red")

        pts_start_long = pts_l - radius_joint*y
        rev_joint_l = create_revolute_joint(pts_l, ax, radius=1, color="red")
        ax.annotate("L", pts_l[1:], xytext=(-1.2, -1.2), textcoords='offset fontsize', fontsize=12)
        pts_end_long = pts_l - l_ling*y
        ax.scatter(pts_end_long[1], pts_end_long[2], marker="+", color="black", label="A")
        ax.annotate(r"$A_{0}$", pts_end_long[1:], xytext=(-0.8, 0.4), textcoords='offset fontsize', fontsize=12)
        len_ling = np.array([pts_start_long, pts_end_long]).T
        ax.plot(len_ling[1], len_ling[2], color = "red")

        y_pclim_max = -np.sin(ipcmax)*y + np.cos(ipcmax)*z
        y_pclim_min = -np.sin(ipcmin)*y + np.cos(ipcmin)*z
        y_pslim_max = np.sin(ipsmax)*y - np.cos(ipsmax)*z
        y_pslim_min = np.sin(ipsmin)*y - np.cos(ipsmin)*z
        lim_pc_right = np.array([pts_b, pts_b + rpc*y_pclim_max]).T
        lim_pc_left = np.array([pts_b, pts_b + rpc*y_pclim_min]).T
        lim_ps_right = np.array([pts_end_long, pts_end_long + rps*y_pslim_max]).T
        lim_ps_left = np.array([pts_end_long, pts_end_long + rps*y_pslim_min]).T
        ax.plot(lim_pc_right[1], lim_pc_right[2], "-.", color = "red", linewidth = 0.8)
        ax.plot(lim_pc_left[1], lim_pc_left[2], "-.", color = "red", linewidth = 0.8)
        ax.plot(lim_ps_right[1], lim_ps_right[2], "-.", color = "red", linewidth = 0.8)
        ax.plot(lim_ps_left[1], lim_ps_left[2], "-.", color = "red", linewidth = 0.8)

        arc_patin_came = ptc.Arc(
            pts_b[1:], 
            width = 2*rpc, height = 2*rpc, 
            angle = (beta + np.pi/2 + ipc_min)/unit.DEGREE_TO_RADIAN, 
            theta1 = 0, 
            theta2 = (ipc_max - ipc_min)/unit.DEGREE_TO_RADIAN, 
            color="red",
            linewidth = 1.5
            )
        arc_patin_soup = ptc.Arc(
            pts_end_long[1:], 
            width = 2*rps, 
            height = 2*rps, 
            angle = (beta - np.pi/2 + ips_min)/unit.DEGREE_TO_RADIAN, 
            theta1 = 0, 
            theta2 = (ips_max - ips_min)/unit.DEGREE_TO_RADIAN, 
            color="red",
            linewidth = 1.5
            )
        
        ax.add_patch(arc_patin_came)
        ax.add_patch(arc_patin_soup)
        return y_end, z_end

    def create_came(pts_c, y, z, rb, gamma0, ax : Axes, theta=0, radius_joint=0):
        
        y_end, z_end = create_csys(pts_c, y, z, ax, num=3, radius_joint=radius_joint, scale=5, color="green")

        rev_joint_c = create_revolute_joint(pts_c, ax, radius=radius_joint, color="green")
        ax.annotate("C", pts_c[1:], xytext=(0.6, 0.6), textcoords='offset fontsize', fontsize=12)
        arc_came_base = ptc.Arc(
            pts_c[1:], 
            width = 2*rb, 
            height = 2*rb, 
            angle = (theta + gamma0)/unit.DEGREE_TO_RADIAN, 
            theta1 = 0, 
            theta2 = 180, 
            color="green",
            linewidth = 1.5
            )
        arc_came_base_prolong = ptc.Arc(
            pts_c[1:], 
            width = 2*rb, 
            height = 2*rb, 
            angle = (theta + gamma0)/unit.DEGREE_TO_RADIAN, 
            theta1 = 180, 
            theta2 = 0, 
            color="green",
            linewidth = 1,
            linestyle = "-."
            )
        arc_came_levee = ptc.Arc(
            pts_c[1:], 
            width = 2*rb, 
            height = 4*rb, 
            angle = (theta + gamma0)/unit.DEGREE_TO_RADIAN, 
            theta1 = 180, 
            theta2 = 0, 
            color="green",
            linewidth = 1.5
            )
        ax.add_patch(arc_came_base)
        ax.add_patch(arc_came_base_prolong)
        ax.add_patch(arc_came_levee)
        return y_end, z_end 

    def create_bati(pts, y, z, radius_joint=0):
        pts_start = pts + radius_joint*y
        pts_end = pts_start + 4*y
        branch1_start = pts_end + 2*z
        branch1_end = branch1_start + y - z
        branch2_start = pts_end + 1*z
        branch2_end = branch2_start + y - z
        branch3_start = pts_end + 0*z
        branch3_end = branch3_start + y - z
        branch4_start = pts_end - 1*z
        branch4_end = branch4_start + y - z
        branch5_start = pts_end - 2*z
        branch5_end = branch5_start + y - z

        mainline = np.array([pts_start, pts_end]).T
        orthline = np.array([branch1_start, branch5_start]).T
        branch1 = np.array([branch1_start, branch1_end]).T
        branch2 = np.array([branch2_start, branch2_end]).T
        branch3 = np.array([branch3_start, branch3_end]).T
        branch4 = np.array([branch4_start, branch4_end]).T
        branch5 = np.array([branch5_start, branch5_end]).T

        ax.plot(mainline[1], mainline[2], color="black")
        ax.plot(orthline[1], orthline[2], color="black")
        ax.plot(branch1[1], branch1[2], color="black")
        ax.plot(branch2[1], branch2[2], color="black")
        ax.plot(branch3[1], branch3[2], color="black")
        ax.plot(branch4[1], branch4[2], color="black")
        ax.plot(branch5[1], branch5[2], color="black")
    
    def annotate_arc(arc : ptc.Arc, label : str = r"$\alpha$", color : str = "black"):
        angle_start = np.deg2rad(arc.theta1)
        angle_stop = np.deg2rad(arc.theta2)
        radius = arc.height/2
        center = arc.center
        angle_middle = (angle_start + angle_stop)/2
        x = center[0] + 0.9*radius*np.cos(angle_middle)
        y = center[1] + 0.9*radius*np.sin(angle_middle)

        ax.text(x, y, label, horizontalalignment='center', verticalalignment='center', fontsize=11, color=color)

    
    ax.plot(o[1], o[2], "+", color="black")
    ax.annotate("O", o[1:], xytext=(-1.2, 0.6), textcoords='offset fontsize', fontsize=12)

    rev_joint_c = create_revolute_joint(oc, ax, radius=1, color="green")
    ax.plot(os[1], os[2], "+", color="blue")
    ax.annotate(r"$S_{0}$", os[1:], xytext=(0.6, -1.2), textcoords='offset fontsize', fontsize=12)

    ax.plot(ob[1], ob[2], "+", color="magenta")
    ax.annotate(r"$B_{0}$", ob[1:], xytext=(0, -1.2), textcoords='offset fontsize', fontsize=12)

    y0_end, z0_end = create_csys(o, y0, z0, ax, num=0, radius_joint=0, scale=5, color="black")

    y1_end, z1_end = create_soupape(
        pts_s = os, 
        y = y1, 
        z = z1, 
        dsoup = 6, 
        lsoup = 14
        )
    y2_end, z2_end = create_linguet(
        pts_l = ol, 
        pts_b = ob, 
        y = y2, 
        z = z2, 
        rpc = rpc, 
        rps = rps, 
        l_ling = l_ling, 
        ipcmin = ipc_min, 
        ipcmax = ipc_max, 
        ipsmin = ips_min,
        ipsmax = ips_max, 
        ax = ax, 
        radius_joint=1
        )
    y3_end, z3_end = create_came(
        pts_c = oc, 
        y = y3, 
        z = z3, 
        rb = rb, 
        gamma0 = gamma0, 
        ax = ax, 
        theta = theta, 
        radius_joint=1
        )

    o_y0_disp = np.array([5*y0, 15*y0]).T
    ax.plot(o_y0_disp[1], o_y0_disp[2], "-.", color = "black", linewidth = 1)
    o_y1_disp = np.array([5*y1, 15*y1]).T
    ax.plot(o_y1_disp[1], o_y1_disp[2], "-.", color = "blue", linewidth = 1)

    ol_y1_disp = np.array([ol - y1, ol - 10*y1]).T
    ax.plot(ol_y1_disp[1], ol_y1_disp[2], "-.", color = "blue", linewidth = 1)

    cb_disp = np.array([oc-y3, ob]).T
    ax.plot(cb_disp[1], cb_disp[2], "-.", color = "green", linewidth = 1)
    cb_y1_disp = np.array([ob, ob + 15*y1]).T
    ax.plot(cb_y1_disp[1], cb_y1_disp[2], "-.", color = "blue", linewidth = 1)

    ax.annotate(r"$\vec{y_{\!_{0}}}$", y0_end[1:], xytext=(0.6, -1.2), textcoords='offset fontsize', fontsize=10, color="black")
    ax.annotate(r"$\vec{z_{\!_{0}}}$", z0_end[1:], xytext=(0.6, 0.6), textcoords='offset fontsize', fontsize=10, color="black")
    ax.annotate(r"$\vec{y_{\!_{1}}}$", y1_end[1:], xytext=(0.8, 0), textcoords='offset fontsize', fontsize=10, color="blue")
    ax.annotate(r"$\vec{z_{\!_{1}}}$", z1_end[1:], xytext=(-1.2, 0.6), textcoords='offset fontsize', fontsize=10, color="blue")
    ax.annotate(r"$\vec{y_{\!_{2}}}$", y2_end[1:], xytext=(0.6, 0.6), textcoords='offset fontsize', fontsize=10, color="red")
    ax.annotate(r"$\vec{z_{\!_{2}}}$", z2_end[1:], xytext=(0.6, 0.6), textcoords='offset fontsize', fontsize=10, color="red")
    ax.annotate(r"$\vec{y_{\!_{3}}}$", y3_end[1:], xytext=(0, 0.6), textcoords='offset fontsize', fontsize=10, color="green")
    ax.annotate(r"$\vec{z_{\!_{3}}}$", z3_end[1:], xytext=(-1.2, 1.2), textcoords='offset fontsize', fontsize=10, color="green")


    pos_alpha= 15*y1
    pos_alpha_sup = pos_alpha - 0.5*z1 + 0.2*y1
    pos_alpha_inf = pos_alpha - 0.5*z1 - 0.2*y1
    alpha_arc = ptc.Arc(
        o[1:], 30, 30, angle=0.0, theta1=-alpha/unit.DEGREE_TO_RADIAN, theta2=0, color="blue"
    )
    annotate_arc(alpha_arc, r"$\alpha$", color="blue")
    alpha_arrow = ptc.Polygon([pos_alpha[1:], pos_alpha_sup[1:], pos_alpha_inf[1:]], color = "blue")

    pos_beta= ol - 10*y2
    pos_beta_sup = pos_beta - 0.5*z2 + 0.2*y2
    pos_beta_inf = pos_beta - 0.5*z2 - 0.2*y2
    beta_arc = ptc.Arc(
        ol[1:], 20, 20, angle=0, theta1=180 + beta/unit.DEGREE_TO_RADIAN, theta2=180, color="red"
    )
    annotate_arc(beta_arc, r"$\beta$", color="red")
    beta_arrow = ptc.Polygon([pos_beta[1:], pos_beta_sup[1:], pos_beta_inf[1:]], color = "red")

    pos_gamma=ob + 15*y3
    pos_gamma_sup = ob + 15*y3 - 0.5*z3 + 0.2*y3
    pos_gamma_inf = ob + 15*y3 - 0.5*z3 - 0.2*y3
    gamma0_arc = ptc.Arc(
        ob[1:], 30, 30, angle=0.0, theta1=0, theta2=gamma0/unit.DEGREE_TO_RADIAN
    )
    annotate_arc(gamma0_arc, r"$\gamma_{\!_{0}}$", color="black")
    gamma0_arrow = ptc.Polygon([pos_gamma[1:], pos_gamma_sup[1:], pos_gamma_inf[1:]], color = "black")


    ax.add_patch(alpha_arc)
    ax.add_patch(alpha_arrow)
    ax.add_patch(beta_arc)
    ax.add_patch(beta_arrow)
    ax.add_patch(gamma0_arc)
    ax.add_patch(gamma0_arrow)

    pivot_glissant = ptc.Rectangle(
        xy = -12*z1[1:]-2.5*y1[1:],
        width = 5,
        height= 8,
        facecolor ="none",
        edgecolor = "black"
    )
    ax.add_patch(pivot_glissant)

    create_bati(-8*z1-2.5*y1, -y1, z1)
    create_bati(ol, -z1, y1, radius_joint=1)
    create_bati(oc, y1, z1, radius_joint=1)


if __name__=="__main__":
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    create_fig(ax)
    plt.show()
    