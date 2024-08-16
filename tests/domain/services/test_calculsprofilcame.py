import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import time

import numpy as np
from domain.entities.assemblage import AssemblageLinguet
from domain.entities.came import Came
from domain.entities.levier import Levier, Patin
from domain.entities.ressort import Ressort
from domain.entities.soupape import Soupape
from domain.services.calculscinematique import CalculsCinematique
from domain.services.calculsprofilcame import CalculProfilCameAnalytique, CalculProfilCameAnalytiqueApprox, CalculProfilCameTangence
from application.usecases.loiscame import CreateLoisRampe, CreateLoisAccel, CreateLoisDecel, CreateDemiLois, CreateLoisCame
import matplotlib.pyplot as plt
import domain.services.unitees as unit

## Assemblage configuration
if __name__=="__main__":    
    came = Came(
        rayon_base = 19e-3,
        largeur = 8e-3,
        module_young = 200e9,
        coefficient_poisson = 0.3
    )

    patin_came = Patin(
        rayon_courbure = 27e-3,
        largeur = 6e-3,
        module_young = 200e9,
        coefficient_poisson = 0.3
    )

    patin_soupape = Patin(
        rayon_courbure = 18e-3,
        largeur = 6e-3,
        module_young = 200e9,
        coefficient_poisson = 0.3
    )

    linguet = Levier(
        masse = 1,
        inertie = 9e-6,
        longueur = 36.8e-3,
        patin_came = patin_came,
        patin_soupape = patin_soupape
    )

    soupape = SoupapeSansPoussoir(
        masse_soupape=43.5e-3,
        masse_coupelle=5.5e-3,
        module_young=200e9,
        coefficient_poisson=0.3,
        diametre_soupape = 6e-3
    )

    ressort = Ressort(
        masse=27e-3,
        raideur=46.5e3,
        precharge=240
    )
    
    distribution = AssemblageLinguet(
        came = came,
        angle_came = 0,
        coords_came = np.array([0, 14.21, 31.712])*1e-3,
        sens_rotation_came = -1,
        levier = linguet,
        coords_levier = np.array([0, 35.66, 5.412])*1e-3,
        angle_leviercame_init = (90-5.311),
        angles_limites_patincame=(20,25),
        angles_limites_patinsoupape=(25,35),
        ressort = ressort,
        soupape = soupape,
        coords_soupape = np.array([0,0,0]),
        inclinaison_soupape = 0,
    )

    
    
    ## Points Squelette Accélération Positive
    ctrlpts_disp = np.array([[39,0],[43.5,34.1],[47,34.1],[52.5,0]])

    ## Lois antérieure pour comparaison
    ac_comp, levee_comp, vitesse_comp, accel_comp = np.loadtxt("data\\exemple_lois_evo2-E_newgeom.txt").T
    yprofil_comp, zprofil_comp = np.loadtxt("data\\profil_came_exemple_lois_evo2-E_newgeom.txt").T
    ac_courbure_comp, rc_comp = np.loadtxt("data\\rayon_courbure_came_exemple_lois_evo2-E_newgeom.txt").T
    

    fig_accel, (ax_prt, ax_asm) = plt.subplots(2,1)
    plt.title("Accélération")
    ax_prt.plot(ctrlpts_disp[:,0], ctrlpts_disp[:,1], "--x", label="Squelette", color="black")
    ax_asm.plot(ac_comp, accel_comp, "-.", label="Logiciel antérieur")

    fig_vitesse = plt.figure(2)
    plt.title("Vitesse")
    plt.plot(ac_comp, vitesse_comp, "-.", label="Logiciel antérieur")

    fig_levee = plt.figure(3)
    plt.title("Levée")
    plt.plot(ac_comp, levee_comp, "-.", label="Logiciel antérieur")
    
    clr = CreateLoisRampe(
        duree_rampe=36,
        duree_vitesse_constante=25,
        levee_rampe=0.273e-3,
        vitesse_rampe=9e-6,
    )

    cla = CreateLoisAccel(
        duree_montee=15/2,
        duree_palier=7/2,
        duree_descente=11/2,
        accelmax=34.1e-6,
        jerk_final=-2*34.1e-6/11,
        poids_2=2,
        poids_35=5,
        degree_spline=3,
        vitesse_rampe=9e-6,
        levee_rampe=0.273e-3
    )

    cld = CreateLoisDecel(
        levee_max=11.15e-3,
        distribution=distribution,
        regime_affolement = 12200*unit.RPM_TO_DEGPSEC
    )
    
    cdl = CreateDemiLois(
        loisrampe_creator=clr,
        loisaccel_creator=cla,
        loisdecel_creator=cld,
        angle_leveemax=99.25,
        duree_raccord=15.0
    )

    cdl.optimize_demilois()

    demilois = cdl.create_demilois()

    clc = CreateLoisCame(
        demilois_ouverture_creator=cdl,
        demilois_fermeture_creator=cdl
    )

    loiscame = clc.create_loiscame()

    ac_disp = np.linspace(0,198.5,1000)
    accel_disp = loiscame.a(ac_disp)
    vitesse_disp = loiscame.v(ac_disp)
    levee_disp = loiscame.l(ac_disp)
    jerk_disp = loiscame.j(ac_disp)

    plt.figure(fig_accel)
    ax_prt.plot(ac_disp, demilois.lois_rampe.a(ac_disp)*1e6, label="rampe")
    ax_prt.plot(ac_disp, demilois.lois_accel.a(ac_disp - 36)*1e6, label="accel")
    ax_prt.plot(ac_disp, demilois.lois_raccord.a(ac_disp - 67.5)*1e6, label="raccord")
    ax_prt.plot(ac_disp, demilois.lois_decel.a(ac_disp - 99.25)*1e6, label="decel")
    ax_prt.legend()
    ax_asm.plot(ac_disp, accel_disp*1e6, label="assemblage")
    ax_asm.legend()

    plt.figure(2)
    # plt.plot(ac_disp, demilois.lois_rampe.a(ac_disp)*1e3, label="rampe")
    # plt.plot(ac_disp, demilois.lois_accel.a(ac_disp - 36)*1e3, label="accel")
    # plt.plot(ac_disp, demilois.lois_raccord.v(ac_disp - 67.5)*1e3, label="raccord")
    # plt.plot(ac_disp, demilois.lois_decel.a(ac_disp - 99.25)*1e3, label="decel")
    plt.plot(ac_disp, vitesse_disp*1e6)

    plt.figure(3)
    plt.plot(ac_disp, levee_disp*1e3)

    fig_jerk = plt.figure(4)
    plt.plot(ac_disp, jerk_disp)

    fig_profil, ax = plt.subplots()
    matrot = np.array([
        [1, 0, 0],
        [0, np.cos(5.311*unit.DEGREE_TO_RADIAN),  -np.sin(5.311*unit.DEGREE_TO_RADIAN)],
        [0, np.sin(5.311*unit.DEGREE_TO_RADIAN),  np.cos(5.311*unit.DEGREE_TO_RADIAN)]
    ])
    profilcomp = np.array([np.zeros(len(yprofil_comp)), yprofil_comp, -zprofil_comp]).T
    profilcomp = np.array([matrot@profilcomp[i] for i in range(len(profilcomp))])
    ax.plot(profilcomp[:,1], profilcomp[:,2], "-.")

    fig_ci = plt.figure(6)
    plt.plot(np.linspace(0, 199, 199), np.sqrt(yprofil_comp[0:199]**2 + zprofil_comp[0:199]**2), "-.")

    calccinematique = CalculsCinematique(
        distribution = distribution,
        loiscame = loiscame,
    )

    calcprofil = CalculProfilCameAnalytique(
        distribution = distribution,
        loiscame = loiscame,
        calculscinematique = calccinematique
    )
    ac_profil = np.arange(0, 198.5, 0.1)
    start_time_analytique  = time.process_time()
    profil = calcprofil.ci_prime_base3(ac_profil*unit.DEGREE_TO_RADIAN)*1e3
    stop_time_analytique  = time.process_time()
    duration_analytique = stop_time_analytique - start_time_analytique
    
    eps_profil = calcprofil.eps_came(ac_profil*unit.DEGREE_TO_RADIAN)
    eps_disp = np.linspace(0, 2*np.pi, 1000)
    rho = calcprofil.profil_polaire
    rho_profil = rho(eps_disp)*1e3
    yprofil = -rho_profil*np.cos(eps_disp)
    zprofil = -rho_profil*np.sin(eps_disp)

    rayon_courbure = (rho(eps_profil)**2 + rho.derivative()(eps_profil)**2)**(3/2)/(rho(eps_profil)**2 + 2*rho.derivative()(eps_profil)**2 - rho(eps_profil)*rho.derivative(nu=2)(eps_profil))
    rayon_courbure_2 = calcprofil.rayon_courbure(ac_profil*unit.DEGREE_TO_RADIAN)
    
    camepos_fin_rampe = calcprofil.ci_prime_base3(clr.dac_r*unit.DEGREE_TO_RADIAN)*1e3
    camepos_fin_accelo = calcprofil.ci_prime_base3((clr.dac_r + cla.dac_apos)*unit.DEGREE_TO_RADIAN)*1e3
    camepos_leveemax = calcprofil.ci_prime_base3(cdl.ac_lmax*unit.DEGREE_TO_RADIAN)*1e3
    camepos_fin_decel = calcprofil.ci_prime_base3((2*cdl.ac_lmax - clr.dac_r - cla.dac_apos)*unit.DEGREE_TO_RADIAN)*1e3
    camepos_fin_accelf = calcprofil.ci_prime_base3((2*cdl.ac_lmax - clr.dac_r)*unit.DEGREE_TO_RADIAN)*1e3

    plt.figure(fig_profil)
    ax.plot(profil[:,1], profil[:,2], label="Profil Analytique")
    ax.plot(yprofil, zprofil, label="Profil Came Interpolé")
    ax.plot([0, camepos_fin_rampe[0,1]], [0, camepos_fin_rampe[0,2]], "-.", label="Fin Rampe Ouverture V1")
    ax.plot([0, camepos_fin_accelo[0,1]], [0, camepos_fin_accelo[0,2]], "-.", label="Fin Accélération Ouverture V1")
    ax.plot([0, camepos_leveemax[0,1]], [0, camepos_leveemax[0,2]], "-.", label="Levée Maximale V1")
    ax.plot([0, camepos_fin_decel[0,1]], [0, camepos_fin_decel[0,2]], "-.", label="Début Accélération Fermeture V1")
    ax.plot([0, camepos_fin_accelf[0,1]], [0, camepos_fin_accelf[0,2]], "-.", label="Début Rampe Fermeture V1")

    plt.figure(fig_ci)
    plt.plot(ac_profil, np.sqrt(profil[:,1]**2 + profil[:,2]**2))

    fig_polaire = plt.figure(7)
    plt.plot(eps_disp, rho_profil)

    fig_courbure = plt.figure(8)
    plt.plot(ac_courbure_comp, rc_comp, "-.")
    plt.plot(ac_profil, rayon_courbure*1e3)
    plt.plot(ac_profil, rayon_courbure_2*1e3)


    # calcprofilv2 = CalculProfilCameAnalytiqueApprox(
    #     distribution = distribution,
    #     loiscame = loiscame
    # )
    # ac_profilv2 = np.arange(0, 198.5, 0.1)
    # start_time_analytiqueapprox  = time.process_time()
    # profilv2 = calcprofilv2.ci(ac_profilv2)*1e3
    # stop_time_analytiqueapprox  = time.process_time()
    # duration_analytiqueapprox = stop_time_analytiqueapprox - start_time_analytiqueapprox

    # plt.figure(fig_profil)
    # ax.plot(profilv2[:,1], profilv2[:,2], label="Profil Analytique Approché")

    # plt.figure(fig_ci)
    # plt.plot(ac_profilv2[:-1], np.sqrt(profilv2[:,1]**2 + profilv2[:,2]**2))


    # calcprofilv3 = CalculProfilCameTangence(
    #     distribution = distribution,
    #     loiscame = loiscame
    # )
    # ac_profilv3 = np.arange(0.5, 198, 0.1)
    # start_time_tangence  = time.process_time()
    # profilv3 = calcprofilv3.profil_came(ac_profilv3)*1e3
    # stop_time_tangence  = time.process_time()
    # duration_tangence = stop_time_tangence - start_time_tangence

    # plt.figure(fig_profil)
    # ax.plot(profilv3[:,1], profilv3[:,2], label="Profil Méthode des tangentes")

    # plt.figure(fig_ci)
    # plt.plot(ac_profilv3[1:-1], np.sqrt(profilv3[:,1]**2 + profilv3[:,2]**2))

    plt.figure(fig_profil)
    ax.set_aspect('equal', adjustable='box')
    # Move the left and bottom spines to zero position
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    # Hide the right and top spines
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # Set the ticks position to bottom and left
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.legend()
    
    
    plt.show()