import numpy as np

RPM_TO_DEGPSEC = 360/60

def beta(lbd: float, l_ling: float, z_l: float, r_ps: float) -> float :
    """Calcule l'angle beta d'inclinaison du levier en fonction d'un ensemble de paramètres de l'assemblage.

    Cette relation est obtenue par fermeture géométrique et projection suivant l'axe de la soupape.

    Args:
        lbd (float): Levée.
        l_ling (float): Longueur du levier. De son centre de rotation, L, au centre du patin côté soupape, A.
        z_l (float): Coordonnée, suivant z1, du centre de rotation du levier dans le repère (O, x, y1, z1).
        r_ps (float): Rayon de courbure du patin côté soupape.

    Returns:
        float: L'angle beta d'inclinaison du levier.
    """
    return np.arcsin((lbd+z_l-r_ps)/l_ling)

def beta_dot(lbd_dot: float, beta: float, l_ling: float) -> float :
    """Calcule la dérivée de l'angle d'inclinaison du levier par rapport au temps.

    Cette fonction calcule la dérivée de l'angle d'inclinaison de l'angle beta par rapport au temps en fonction de la vitesse de la soupape, de l'inclinaision et de la longueur du levier. Ici, _dot signifie "derivative of time".

    Args:
        lbd (float): Levée.
        l_ling (float): Longueur du levier. De son centre de rotation, L, au centre du patin côté soupape, A.
        z_l (float): Coordonnée, suivant z1, du centre de rotation du levier dans le repère (O, x, y1, z1).
        r_ps (float): Rayon de courbure du patin côté soupape.

    Returns:
        float: L'angle beta d'inclinaison du levier.
    """
    return lbd_dot/l_ling/np.cos(beta)

def lbd(beta: float, l_ling: float, z_l: float, r_ps: float) -> float:
    """Calcule la levée en fonction de l'angle d'inclinaison du levier.

    Cette fonction calcule la levée de la soupape en fonction de l'angle d'inclinaison du levier et d'autres paramètres géométriques de l'assemblage. La relation est la relation "réciproque" à celle implémentée dans la fonction beta.

    Args:
        beta (float): Angle d'inclinaison du levier.
        l_ling (float): Longueur du levier de son centre de rotation au centre du patin côté came.
        z_l (float): Coordonnée, suivant z1, du centre de rotation du levier dans le repère (O, x, y1, z1).
        r_ps (float): Rayon de courbure du patin côté soupape.

    Returns:
        float: Levée.
    """
    return l_ling*np.sin(beta) - z_l + r_ps

def lbd_dot(beta: float, beta_dot: float, l_ling: float) -> float:
    """Calcule la vitesse de la soupape (en m/s).

    Cette fonction calcule la vitesse de la soupape en fonction de l'inclinaison du levier et de sa vitesse de rotation.

    Args:
        beta (float): Inclinaison du levier.
        beta_dot (float): Vitesse de rotation du levier.
        l_ling (float): Longueur du levier.

    Returns:
        float: Vitesse de la soupape.
    """
    return l_ling*beta_dot*np.cos(beta)

def lbd_ddot(beta: float, beta_dot: float, beta_ddot: float, l_ling: float) -> float:
    """Calcule l'accélération de la soupape (en m/s²).

    Cette fonction calcule l'accélération de la soupape en fonction de l'inclinaison du levier, de sa vitesse de rotation et de son accélération angulaire.

    Args:
        beta (float): Inclinaison du levier.
        beta_dot (float): Vitesse de rotation du levier.
        beta_dot (float): Accélération angulaire du levier.
        l_ling (float): Longueur du levier.

    Returns:
        float: Vitesse de la soupape.
    """
    return l_ling*(beta_ddot*np.cos(beta) - beta_dot**2*np.sin(beta))

def dynamique_mvmt_affolement(vbeta: np.ndarray, t: float, m1: float, j2: float, k: float, dr: float, l_ling: float, r_ps: float, z_l: float, mu_ps: float) -> np.ndarray:
    """Implémente la dynamique de l'équation différentiel régissant le mouvement du système à l'affolement.

    La dynamique d'une équation différentielle est une fonction f telle que l'équation différentielle peut se mettre sous la forme, dy/dt = f(y,t). De façon générale, y est un vecteur. Dans notre cas, ce vecteur est de dimension 2. La première coordonnée est l'angle beta et la seconde coordonnée est sa dérivée par rapport au temps. La fonction retourne ce vecteur y dérivée par rapport au temps. La première coordonnée est alors la dérivée de l'angle beta par rapport au temps et la seconde coordonnée est la dérivée seconde de beta. 

    Args:
        vbeta (np.ndarray): Vecteur contenant l'angle beta et sa dérivée par rapport au temps.
        t (float): Variable de temps. Dans notre cas cette variable n'intervient pas dans l'expression de la dynamique. Elle doit néanmoins être définie pour pouvoir utiliser les fonctions de résolution numérique des équations différentielles. 
        m1 (float): Masse de l'ensemble cinématique de la soupape.
        j2 (float): Moment d'inertie du linguet autour de son axe de rotation.
        k (float): Raideur du ressort.
        dr (float): Precharge / Raideur = Différence entre longueur à vide du ressort et longueur du ressort à levée et jeu nul.
        l_ling (float): Longueur du levier.
        r_ps (float): Rayon du patin côté soupape.
        z_l (float): Coordonnée, suivant z1, du centre de rotation du levier dans le repère (O, x, y1, z1).
        mu_ps (float): Coefficient de frottement dynamique entre la soupape et son patin.

    Returns:
        np.ndarray: Vecteur contenant la vitesse de rotation et l'accélération angulaire du linguet.
    
    Raises:
        ZeroDivisionError: Si m1 et j2 sont tous les deux nuls, l'étude n'a que peut d'intérêt. De plus il y a une division par 0.
    """
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