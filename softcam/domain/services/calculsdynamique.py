import numpy as np

RPM_TO_DEGPSEC = 360/60

def beta(lbd, l_ling, z_l, r_ps) :
    return np.arcsin((lbd+z_l-r_ps)/l_ling)
def beta_dot(lbd_dot, beta, l_ling) :
    return lbd_dot/l_ling/np.cos(beta)

def lbd(beta, l_ling, z_l, r_ps):
    return l_ling*np.sin(beta) - z_l + r_ps
def lbd_dot(beta, dot_beta, l_ling):
    return l_ling*dot_beta*np.cos(beta)
def lbd_ddot(beta, dot_beta, beta_ddot, l_ling):
    return l_ling*(beta_ddot*np.cos(beta) - dot_beta**2*np.sin(beta))

def dynamique_mvmt_affolement(vbeta, t, m1, j2, k, dr, l_ling, r_ps, z_l, mu_ps):

    if m1==0 and j2==0:
        raise ZeroDivisionError
    
    vg12 = vbeta[1]*(l_ling*np.sin(vbeta[0]) + r_ps)
    d = np.sign(vg12)*mu_ps*(r_ps + l_ling*np.sin(vbeta[0])) - l_ling*np.cos(vbeta[0])

    beta_ddot = d*(
        -m1*l_ling*vbeta[1]**2*np.sin(vbeta[0]) + k*(l_ling*np.sin(vbeta[0]) - z_l + r_ps + dr)
    )/(
        j2 - m1*l_ling*np.cos(vbeta[0])*d
    )

    return np.array([vbeta[1], beta_ddot])