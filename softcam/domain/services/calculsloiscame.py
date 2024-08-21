import numpy as np
import numpy.linalg as npl
import scipy.interpolate as scitp
import scipy.special as scs

class CalculRampe():
    """CalculRampe modélise les lois de distribution pour les phases de rampe afin de pouvoir calculer la levée, la vitesse, l'accélération et le jerk.

    Cette classe fournit des méthodes permettant le calcul de la levée et de ses dérivées au cours de la phase de rampe.

    Args:
        duree_rampe (float): Durée angulaire totale de la phase de rampe.
        duree_vitesse_constante (float): Durée angulaire de la sous-phase à vitesse constante dans la phase de rampe.
        levee_rampe (float): Levée caractéristique de la rampe.
        vitesse_rampe (float): Vitesse caractéristique de la rampe.

    Attributes:
        dac_r (float): Durée de la phase de rampe.
        dac_vc (float): Durée de la phase à vitesse constante.
        dac_apos (float): Durée de la phase d'accélération.
        lr (float): Levée caractéristique de la rampe.
        vr (float): Vitesse caractéristique de la rampe.
        la (float): Levée au début de la phase à vitesse constante.
        a7 (float), a6 (float), a5 (float), a4 (float): Coefficients du polynôme de degré 7 modélisant la phase d'accélération en début de rampe.

    Methods:
        compute_coeffs_accel(): Calcule les coefficients du polynôme de degré 7 modélisant la levée pendant la phase d'accéération en début de rampre.
        j(ac: float): Calcule le jerk pour la phase de rampe.
        a(ac: float): Calcule l'accélération pour la phase de rampe.
        v(ac: float): Calcule la vitesse pour la phase de rampe.
        l(ac: float): Calcule la levée pour la phase de rampe.
        compute_levee_accel(): Calcule la levée en début de phase à vitesse constante.
        matrix_pb(): Génère la matrice du système d'équations permettant la détermination de la phase d'accélération en début de rampe.
        bcs_pb(): Génère le vecteur des conditions aux limites.
        from_dict(d: dict): Crée une instance de CalculRampe à partir d'un dictionnaire.
        to_dict() -> dict: Convertit l'instance en dictionnaire.

    Raises:
        ValueError: Si certaines durées sont négatives ou nulles ou si la duree de rampe est inférieure à la durée à vitesse constante.
    """
    def __init__(self, duree_rampe: float, duree_vitesse_constante: float, levee_rampe: float, vitesse_rampe: float):
        if duree_rampe<=0 :
            raise ValueError("La rampe a une durée nulle ou négative.")
        if duree_vitesse_constante<=0:
            raise ValueError("La phase à vitesse constante de la rampe à une durée nulle ou négative.")
        if duree_rampe < duree_vitesse_constante :
            raise ValueError("La durée de la phase à vitesse constante doit être inférieure à la durée de la phase de rampe.")
        
        self.__dac_r = duree_rampe
        self.__dac_vc = duree_vitesse_constante
        self.__dac_apos = duree_rampe - duree_vitesse_constante
        self.__lr = levee_rampe
        self.__vr = vitesse_rampe
        
        self.__la = self.compute_levee_accel()
        self.__a7, self.__a6, self.__a5, self.__a4 = self.compute_coeffs_accel()
    
    @property
    def dac_r(self):
        return self.__dac_r
    @property
    def dac_vc(self):
        return self.__dac_vc
    @property
    def dac_apos(self):
        return self.__dac_apos
    @property
    def lr(self):
        return self.__lr
    @property
    def vr(self):
        return self.__vr
    
    @property
    def la(self):
        return self.__la
    
    @property
    def a7(self):
        return self.__a7
    @property
    def a6(self):
        return self.__a6
    @property
    def a5(self):
        return self.__a5        
    @property
    def a4(self):
        return self.__a4
    
    def compute_coeffs_accel(self):
        """Calcule les coefficients du polynôme de degré 7 qui modélise la levée pendant la phase d'accélération des rampes d'ouverture et de fermeture. 
        
        Ce calcul revient à résoudre un système d'équations linéaires d'ordre 4. Cette résolution est ici présentée de façon matricielle.

        Returns:
            numpy.ndarray: Coefficients du polynôme de degré 7 modélisant la levée.
        
        Raises:
            ValueError: Si la matrice du système d'équation n'est pas inversible, il n'est pas possible de trouver des solutions. 
        """
        if npl.det(self.matrix_pb()) < 1e-5 :
            raise ValueError("La matrice du problème est difficilement inversible. Il se peut que les solutions du problème n'existent pas ou soient imprécises")
        return npl.inv(self.matrix_pb())@self.bcs_pb()

    def j(self, ac: float) -> float:
        """Calcul du jerk spécifiquement pour la phase de rampe.

        Args:
            ac (numpy.ndarray): Angle de rotation de la came.
        
        Returns:
            float: Jerk de la soupape (en m/rad^3).
        """
        def j_ar(x):
            xm = np.atleast_1d(np.ma.array(np.array(x), mask = ((x < 0) | (x >= self.dac_r - self.dac_vc))))
            jerk = 210*self.a7*xm**4 + 120*self.a6*xm**3 + 60*self.a5*xm**2 + 24*self.a4*xm
            jerk[xm.mask] = 0
            return jerk.reshape(np.shape(x))
        
        acm = np.atleast_1d(np.ma.array(np.array(ac), mask = ((ac < 0) | (ac > self.dac_r))))
        jerk = j_ar(acm)
        jerk[acm.mask] = np.nan

        return jerk.reshape(np.shape(ac))

    def a(self, ac: float) -> float:
        """Calcul de l'accélération spécifiquement pour la phase de rampe.

        Args:
            ac (numpy.ndarray): Angle de rotation de la came.
        
        Returns:
            float: Accélération de la soupape (en m/rad²).
        """
        def a_ar(x):
            xm = np.atleast_1d(np.ma.array(np.array(x), mask = ((x < 0) | (x >= self.dac_r - self.dac_vc))))
            accel = 42*self.a7*xm**5 + 30*self.a6*xm**4 + 20*self.a5*xm**3 + 12*self.a4*xm**2
            accel[xm.mask] = 0
            return accel.reshape(np.shape(x))
        
        acm = np.atleast_1d(np.ma.array(np.array(ac), mask = ((ac < 0) | (ac > self.dac_r))))
        accel = a_ar(acm)
        accel[acm.mask] = np.nan

        return accel.reshape(np.shape(ac))
            
    def v(self, ac: float) -> float:
        """Calcul de la vitesse spécifiquement pour la phase de rampe.

        La loi de vitesse est divisée en 2 phases, une accélération qui suit la loi donné par le polynôme et une phase à vitesse constante. deux fonctions sont définies pour pouvoir les calculer.
        
        Args:
            ac (numpy.ndarray): Angle de rotation de la came.
        
        Returns:
            float: Vitesse de la soupape (en m/rad).
        """
        def v_ar(x):
            xm = np.atleast_1d(np.ma.array(np.array(x), mask = ((x < 0) | (x >= self.dac_r - self.dac_vc))))
            vitesse = 7*self.a7*xm**6 + 6*self.a6*xm**5 + 5*self.a5*xm**4 + 4*self.a4*xm**3
            vitesse[xm.mask] = 0
            return vitesse.reshape(np.shape(x))
        
        def v_vcr(x):
            xm = np.atleast_1d(np.ma.array(np.array(ac), mask = ((x < self.dac_r - self.dac_vc) | (x > self.dac_r))))
            vitesse = self.vr + 0*xm
            vitesse[xm.mask] = 0
            return vitesse.reshape(np.shape(x))
        
        acm = np.atleast_1d(np.ma.array(np.array(ac), mask = ((ac < 0) | (ac > self.dac_r))))
        vitesse = v_ar(acm) + v_vcr(acm)
        vitesse[acm.mask] = np.nan

        return vitesse.reshape(np.shape(ac))

    def l(self, ac: float) -> float:
        """Calcul de la levée spécifiquement pour la phase de rampe.

        La loi de levée est divisée en 2 phases, une accélération qui suit la loi donné par le polynôme et une phase affine. Deux fonctions distinctes sont donc définies pour pouvoir les calculer.
        
        Args:
            ac (numpy.ndarray): Angle de rotation de la came.
        
        Returns:
            float: Levée de la soupape (en m).
        """
        def l_ar(x):
            xm = np.atleast_1d(np.ma.array(np.array(x), mask = ((x < 0) | (x >= self.dac_r - self.dac_vc))))
            levee = self.a7*xm**7 + self.a6*xm**6 + self.a5*xm**5 + self.a4*xm**4
            levee[xm.mask] = 0
            return levee.reshape(np.shape(x))
        def l_vcr(x):
            xm = np.atleast_1d(np.ma.array(np.array(ac), mask = ((x < self.dac_r - self.dac_vc) | (x > self.dac_r))))
            levee = self.lr + self.vr*(xm - self.dac_r)
            levee[xm.mask] = 0
            return levee.reshape(np.shape(x))
        acm = np.atleast_1d(np.ma.array(np.array(ac), mask = ((ac < 0) | (ac > self.dac_r))))
        levee = l_ar(acm) + l_vcr(acm)
        levee[acm.mask] = np.nan
        return levee.reshape(np.shape(ac))
    
    def compute_levee_accel(self) -> float:
        levee_accel = self.lr - self.dac_vc*self.vr
        if levee_accel < 0 :
            raise ValueError("La levée renseigné pour la rampe conduit à une levée négative. Afin de contrer ce problème vous pouvez au choix : \n \ac Augmenter la levée de rampe \n \ac Diminuer la vitesse de rampe \n \ac Diminuer la durée de la phase à vitesse constante.")
        return levee_accel
    
    def matrix_pb(self) -> np.ndarray:
        """Crée la matrice représentant le système linéaire représentant le problème.

        La matrice réduite est de dimension 4x4.

        Returns:
            numpy.ndarray: La matrice 4x4 représentative du problème.
        """
        return np.array([
            [self.dac_apos**3, self.dac_apos**2, self.dac_apos, 1],
            [7*self.dac_apos**3, 6*self.dac_apos**2, 5*self.dac_apos, 4],
            [42*self.dac_apos**3, 30*self.dac_apos**2, 20*self.dac_apos, 12],
            [210*self.dac_apos**3, 120*self.dac_apos**2, 60*self.dac_apos, 24]
        ])
    
    def bcs_pb(self) -> np.ndarray:
        """Crée le vecteur représentant les conditions aux limites du problème.

        Ce vecteur est un vecteur réduit aux coefficient qui ne sont pas nuls a priori.

        Returns:
            numpy.ndarray: Vecteur des conditions aux limites.
        """
        return np.array([
            self.la/self.dac_apos**4, 
            self.vr/self.dac_apos**3,
            0,
            0
        ])
    
    @classmethod
    def from_dict(cls, d: dict):
        """Crée une instance de la classe CalculRampe à partir d'un dictionnaire contenant les attributs de la classe. 
        
        Cette opération permet d'importer une classe CalculRampe qui aurait été stockée au format .json.

        Args:
            dict: Dictionnaire dont les clés sont les attributs de la classe.
        
        Returns:
            CalculRampe: Une instance de la classe CalculRampe.
        """
        return cls(**d)
    
    def to_dict(self) -> dict:
        """Convertit les attributs de la classe en un dicitionnaire. 
        
        Cette opération est nécessaire pour pouvoir stocker les données au format .json.

        Returns:
            dict: Dictionnaire dont les clés sont les attributs de la classe.
        """
        return {
            "duree_rampe" : self.dac_r,
            "duree_vitesse_constante" : self.dac_vc,
            "levee_rampe" : self.lr,
            "vitesse_rampe" : self.vr
        }
    

class CalculRaccord():
    """Utilitaire de calcul du raccord en accélération positive et limite de décélération à l'affolement.
     
    Cette classe fournit des fonctions permettant de calculer la phase de raccord entre l'accélération positive et la décélération à la limite de l'affolement. Ce raccord est créé par une courbe de Bézier à trois points de contrôle. Le premier point de contrôle est le point de fin d'accélération positive. Le second point de contrôle est le point au début de la phase de décélération à la limite de l'affolement. Le dernier point de contrôle est l'intersection des tangentes aux deux premiers points de contrôle.

    Args:
        duree_raccord (float): Durée du raccord, doit être positive.
        accel_init (float): Accélération en fin de phase d'accélération positive.
        jerk_init (float): Jerk en fin de phase d'accélération positive.
        accel_final (float): Accélération en début de phase de décélération à la limite de l'affolement.
        jerk_final (float): Jerk en début de phase de décélération à la limite de l'affolement.

    Attributes:
        dac_raccord (float): Durée du raccord Duration of the connection, must be positive.
        ai (float): Accélération en fin de phase d'accélération positive.
        ji (float): Jerk en fin de phase d'accélération positive.
        af (float): Accélération en début de phase de décélération à la limite de l'affolement.
        jf (float): Jerk en début de phase de décélération à la limite de l'affolement.
        a_spl (scipy.interpolate.BSpline): Spline interpolant l'accélération.
        v_spl (scipy.interpolate.BSpline): Spline interpolant la vitesse.
        l_spl (scipy.interpolate.BSpline): Spline interpolant la levée.
        j_spl (scipy.interpolate.BSpline): Spline interpolant le jerk.

    Methods:
        update(): Updates the attributes representing the interpolations of acceleration, velocity, lift, and jerk.
        compute_accel_spl() -> scipy.interpolate.BSpline: Interpole l'accélération par un BSpline.
        get_bezier_parameters(X, Y, degree=3): Calcule la relation entre l'abscisse curviligne de la courbe de bézier et les coordonnées du point.
        bezier_curve(points: list, nTimes: int=50) -> tuple[np.ndarray, np.ndarray]: Retourne la courbe de Bézier passant par les points de contrôle.

    Raises:
        ValueError: Si la durée du raccord n'est pas strictement positive.
    """
    def __init__(self, duree_raccord, accel_init, jerk_init, accel_final, jerk_final):
        if duree_raccord<=0:
            raise ValueError("Le raccord a une durée négative ou nulle ce qui n'est pas permis.")

        self.__dac_raccord = duree_raccord
        self.__ai = accel_init
        self.__ji = jerk_init
        self.__af = accel_final
        self.__jf = jerk_final

        self.__a_spl = self.compute_accel_spl()
        self.__v_spl = self.a_spl.antiderivative(nu=1)
        self.__l_spl = self.a_spl.antiderivative(nu=2)
        self.__j_spl = self.a_spl.derivative(nu=1)
    
    @property
    def dac_raccord(self):
        return self.__dac_raccord
    @property
    def ai(self):
        return self.__ai
    @property
    def ji(self):
        return self.__ji
    @property
    def af(self):
        return self.__af
    @property
    def jf(self):
        return self.__jf
    @property
    def a_spl(self):
        return self.__a_spl
    @property
    def v_spl(self):
        return self.__v_spl
    @property
    def l_spl(self):
        return self.__l_spl
    @property
    def j_spl(self):
        return self.__j_spl
    
    @dac_raccord.setter
    def dac_raccord(self, new_dac: float) -> None:
        """Met à jour la durée du raccord.

        Ce "setter" s'assure en même temps que la dure du raccord est strictement positive. Et recalcule la spline représentant le raccord.

        Args:
            new_dac: Nouvelle durée du raccord.

        Raises:
            ValueError: Si la nouvelle durée n'est pas strictement positive, la durée est considérée comme non valide.
        """
        if new_dac <= 0:
            raise ValueError("Le raccord a une durée négative ou nulle ce qui n'est pas permis.")
        self.__dac_raccord = new_dac
        self.a_spl = self.compute_accel_spl()
    @ai.setter
    def ai(self, new_ai: float) -> None:
        """Met à jour l'ordonnée (accélération) du premier point de contrôle.

        Args:
            new_af: Nouvelle valeur d'accélération.
        """
        self.__ai = new_ai
    @ji.setter
    def ji(self, new_ji: float) -> None:
        """Met à jour la dérivée du premier point de contrôle.
        
        Ce "setter" s'assure que cette dérivée n'est pas égale à la dérivée du deuxième point de contrôle. Si c'était le cas, les deux tangentes seraient parallèles et aucune intersection ne pourrait donc être trouvée.

        Args:
            new_jf: Nouvelle valeur de la dérivée.

        Raises:
            ZeroDivisionError: Si new_ji = jf. Cela signifierait que les tangentes sont parallèle et que aucune intersection n'existe.
        """
        if new_ji == self.jf :
            raise ZeroDivisionError("Les tangentes sont parallèles. Aucune solution ne peut être trouvée pour le troisième point.")
        else :
            self.__ji = new_ji
    @af.setter
    def af(self, new_af: float) -> None:
        """Met à jour l'ordonnée (accélération) du deuxième point de contrôle.

        Args:
            new_af: Nouvelle valeur d'accélération.
        """
        self.__af = new_af
    @jf.setter
    def jf(self, new_jf: float) -> None:
        """Met à jour la dérivée du deuxième point de contrôle.
        
        Ce "setter" s'assure que cette dérivée n'est pas égale à la dérivée du premier point de contrôle. Si c'était le cas, les deux tangentes seraient parallèles et aucune intersection ne pourrait donc être trouvée.

        Args:
            new_jf: Nouvelle valeur de la dérivée.

        Raises:
            ZeroDivisionError: Si new_jf = ji. Cela signifierait que les tangentes sont parallèle et que aucune intersection n'existe.
        """
        if new_jf == self.ji :
            raise ZeroDivisionError("Les tangentes sont parallèles. Aucune solution ne peut être trouvée pour le troisième point.")
        else :
            self.__jf = new_jf
   
    def update(self) -> None:
        """Met à jour les attributs représentant les interpolations de l'accélération, de la vitesse, de la levée et du jerk.

        Returns:
            None
        """
        self.__a_spl = self.compute_accel_spl()
        self.__v_spl = self.a_spl.antiderivative(nu=1)
        self.__l_spl = self.a_spl.antiderivative(nu=2)
        self.__j_spl = self.a_spl.derivative(nu=1)

    def compute_accel_spl(self) -> scitp.BSpline:
        """Interpole l'accélération en se basant sur la courbe de Bézier précédemment calculée.

        Returns:
            scipy.interpolate.BSpline: A B-spline représentant l'accélération sur la phase de raccord.
        """
        ac_int, a_int = self.compute_bezier_3rd_pts(0, self.ai, self.ji, -self.dac_raccord, self.af, self.jf)
        knots = np.array([[0, self.ai],[ac_int, a_int],[-self.dac_raccord, self.af]]) 
        ac_evalpts, accel_evalpts = self.bezier_curve(knots)
        ind_sort = np.argsort(ac_evalpts)
        ac_evalpts = np.take(ac_evalpts, ind_sort)
        accel_evalpts = np.take(accel_evalpts, ind_sort)
        knot_vector,coefficients,degree = scitp.splrep(ac_evalpts, accel_evalpts, k=2)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)

    def get_bezier_parameters(self, X: list, Y: list, degree: int=3) -> list:
        """ Least square qbezier fit using penrose pseudoinverse.

        Parameters:

        X: array of x data.
        Y: array of y data. Y[0] is the y point for X[0].
        degree: degree of the Bézier curve. 2 for quadratic, 3 for cubic.

        Based on https://stackoverflow.com/questions/12643079/b%C3%A9zier-curve-fitting-with-scipy
        and probably on the 1998 thesis by Tim Andrew Pastva, "Bézier Curve Fitting".
        """
        if degree < 1:
            raise ValueError('degree must be 1 or greater.')

        if len(X) != len(Y):
            raise ValueError('X and Y must be of the same length.')

        if len(X) < degree + 1:
            raise ValueError(f'There must be at least {degree + 1} points to '
                            f'determine the parameters of a degree {degree} curve. '
                            f'Got only {len(X)} points.')

        def bpoly(n, t, k):
            """ Bernstein polynomial when a = 0 and b = 1. """
            return t ** k * (1 - t) ** (n - k) * scs.comb(n, k)
            #return comb(n, i) * ( t**(n-i) ) * (1 - t)**i

        def bmatrix(T):
            """ Bernstein matrix for Bézier curves. """
            return np.array([[bpoly(degree, t, k) for k in range(degree + 1)] for t in T])

        def least_square_fit(points, M):
            M_ = np.linalg.pinv(M)
            return M_ @ points

        T = np.linspace(0, 1, len(X))
        M = bmatrix(T)
        points = np.array(list(zip(X, Y)))

        final = least_square_fit(points, M).tolist()
        final[0] = [X[0], Y[0]]
        final[len(final)-1] = [X[-1], Y[-1]]
        return final

    def bezier_curve(self, points: list, nTimes: int= 50) -> tuple[np.ndarray, np.ndarray]:
        """
        Given a set of control points, return the
        bezier curve defined by the control points.

        points should be a list of lists, or list of tuples
        such as [ [1,1], 
                    [2,3], 
                    [4,5], ..[Xn, Yn] ]
            nTimes is the number of time steps, defaults to 1000

            See http://processingjs.nihongoresources.com/bezierinfo/
        """

        nPoints = len(points)
        xPoints = np.array([p[0] for p in points])
        yPoints = np.array([p[1] for p in points])

        t = np.linspace(0.0, 1.0, nTimes)

        polynomial_array = np.array([self.bernstein_poly(i, nPoints-1, t) for i in range(nPoints) ])
        xvals = np.dot(xPoints, polynomial_array)
        yvals = np.dot(yPoints, polynomial_array)

        return xvals, yvals

    def compute_bezier_3rd_pts(self, x1: float, y1: float, j1: float, x2: float, y2: float, j2: float) -> tuple[float, float]:
        """Calcule les coordonées du 3ème point de controle de la courbe de Bézier. 
        
        Cette fonction à pour objectif de calculer le troisième point de contrôle de la courbe de Bézier à partir des coordonnées de 2 points et de la valeur des dérivées en ces points. 
        Le troisième point se trouve en fait à l'intersection des tangentes aux deux autres points.

        Args:
            x1 (float): Abscisse du premier point.
            y1 (float): Ordonnée du premier point.
            j1 (float): Dérivée de la courbe au premier point.
            x2 (float): Abscisse du second point.
            y2 (float): Ordonnée du second point.
            j2 (float):  Dérivée de la courbe au second point.

        Returns:
            float: Abscisse du troisième point.
            float: Ordonnée du troisième point.
        """
        if j1 == j2 :
            raise ZeroDivisionError("Les tangentes sont parallèles. Aucune solution ne peut être trouvée pour le troisième point.")

        xnew = (j2*x2 - j1*x1 - (y2 - y1))/(j2-j1) 
        return xnew, j1*(xnew-x1) + y1

    def bernstein_poly(self, i: int, n: int, t: float) -> float:
        """Évalue en t le ième membre du polynôme de Bernstein d'ordre n.

        Args :
            i (int): Indice du membre du polynôme de Bernstein à évaluer.
            n (int): Ordre du polynôme de Bernstein.
            t (float): Valeur en laquelle évaluer le polynôme.
        
        Returns:
            float: Valeur en t du ième membre du polynôme de Bernstein d'ordre n.
        """
        return scs.comb(n, i) * ( t**(n-i) ) * (1 - t)**i


if __name__ == "__main__":
    raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
    
    control_points = raccord.get_bezier_parameters([1, 2, 3], [4, 5, 6], degree=2)