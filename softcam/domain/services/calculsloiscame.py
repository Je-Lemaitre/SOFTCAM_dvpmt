import numpy as np
import numpy.linalg as npl
import scipy.interpolate as scitp
import scipy.special as scs

from domain.entities.assemblage import Assemblage, AssemblageLinguet

class CalculRampe():
    """CalculRampe modélise les lois de distribution pour les phases de rampe afin de pouvoir calculer la levée, la vitesse, l'accélération et le jerk.

    Cette classe fournit des méthodes permettant le calcul de la levée et de ses dérivées au cours de la phase de rampe.

    Args:
        duree_rampe (float): Durée angulaire totale de la phase de rampe.
        duree_vitesse_constante (float): Durée angulaire de la sous-phase à vitesse constante dans la phase de rampe.
        levee_rampe (float): Levée caractéristique de la rampe.
        vitesse_rampe (float): Vitesse caractéristique de la rampe.

    Attributes:

    Methods:
    
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
        """Calcul les coefficients du polynôme de degré 7 qui modélise la levée pendant les rampes d'ouverture et de fermeture. Cela revient résoudre un système d'équations linéraires d'ordre 4.

        Raises:
            ValueError: Si la matrice du système d'équation n'est pas inversible, il n'est pas possible de trouver des solutions. 

        Returns:
            numpy.ndarray: Coefficients du polynôme de degré 7 modélisant la levée.
        """
        if npl.det(self.matrix_pb()) < 1e-5 :
            raise ValueError("La matrice du problème est difficilement inversible. Il se peut que les solutions du problème n'existent pas ou soient imprécises")
        return npl.inv(self.matrix_pb())@self.bcs_pb()

    def j(self, ac: float) -> float:
        """Calcul du Jerk spécifiquement pour la phase de rampe d'ouverture.

        Args:
            ac (numpy.ndarray): Angles pour lesquels sont calculées les Jerks
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
        """Calcul l'accélération spécifiquement pour la phase de rampe d'ouverture.

        Args:
            ac (numpy.ndarray): Angles pour lesquels sont calculées les accélérations
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
        return np.array([
            [self.dac_apos**3, self.dac_apos**2, self.dac_apos, 1],
            [7*self.dac_apos**3, 6*self.dac_apos**2, 5*self.dac_apos, 4],
            [42*self.dac_apos**3, 30*self.dac_apos**2, 20*self.dac_apos, 12],
            [210*self.dac_apos**3, 120*self.dac_apos**2, 60*self.dac_apos, 24]
        ])
    
    def bcs_pb(self) -> np.ndarray:
        return np.array([
            self.la/self.dac_apos**4, 
            self.vr/self.dac_apos**3,
            0,
            0
        ])
    
    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)
    
    def to_dict(self) -> dict:
        return {
            "duree_rampe" : self.dac_r,
            "duree_vitesse_constante" : self.dac_vc,
            "levee_rampe" : self.lr,
            "vitesse_rampe" : self.vr
        }
    
class CalculRaccord():
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
    def dac_raccord(self, new_dac):
        if new_dac <= 0:
            raise ValueError("Le raccord a une durée négative ou nulle ce qui n'est pas permis.")
        self.__dac_raccord = new_dac
        self.a_spl = self.compute_accel_spl()
    @ai.setter
    def ai(self, new_ai):
        self.__ai = new_ai
    @ji.setter
    def ji(self, new_ji):
        if new_ji == self.jf :
            raise ZeroDivisionError("Les tangentes sont parallèles. Aucune solution ne peut être trouvée pour le troisième point.")
        else :
            self.__ji = new_ji
    @af.setter
    def af(self, new_af):
        self.__af = new_af
    @jf.setter
    def jf(self, new_jf):
        if new_jf == self.ji :
            raise ZeroDivisionError("Les tangentes sont parallèles. Aucune solution ne peut être trouvée pour le troisième point.")
        else :
            self.__jf = new_jf
   
    def update(self):
        self.__a_spl = self.compute_accel_spl()
        self.__v_spl = self.a_spl.antiderivative(nu=1)
        self.__l_spl = self.a_spl.antiderivative(nu=2)
        self.__j_spl = self.a_spl.derivative(nu=1)

    def compute_accel_spl(self):
        ac_int, a_int = self.compute_bezier_3rd_pts(0, self.ai, self.ji, -self.dac_raccord, self.af, self.jf)

        knots = np.array([[0, self.ai],[ac_int, a_int],[-self.dac_raccord, self.af]]) 
        ac_evalpts, accel_evalpts = self.bezier_curve(knots)
        ind_sort = np.argsort(ac_evalpts)
        ac_evalpts = np.take(ac_evalpts, ind_sort)
        accel_evalpts = np.take(accel_evalpts, ind_sort)
        knot_vector,coefficients,degree = scitp.splrep(ac_evalpts, accel_evalpts, k=2)
        
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)

    def get_bezier_parameters(self, X, Y, degree=3):
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
        final[len(final)-1] = [X[len(X)-1], Y[len(Y)-1]]
        return final

    def bezier_curve(self, points, nTimes=50):
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

    def compute_bezier_3rd_pts(self, x1, y1, j1, x2, y2, j2):
        """This fonction aims to compute the coordinates of the 3rd point in order to link them with a Bézier Curve. 

        Args:
            x1 (float): x-coordinate of the 1st point
            y1 (float): y-coordinate of the 1st point
            j1 (float): dy/dx at the 1st point
            x2 (float): x-coordinate of the 2nd point
            y2 (float): y-coordinate of the 2nd point
            j2 (float): dy/dx at the 2nd point

        Returns:
            float: x-coordinate of the 3rd point
            float: y-coordinate of the 3rd point
        """
        if j1 == j2 :
            raise ZeroDivisionError("Les tangentes sont parallèles. Aucune solution ne peut être trouvée pour le troisième point.")

        xnew = (j2*x2 - j1*x1 - (y2 - y1))/(j2-j1) 
        return xnew, j1*(xnew-x1) + y1

    def bernstein_poly(self, i, n, t):
        """
        The Bernstein polynomial of n, i as a function of t
        """
        return scs.comb(n, i) * ( t**(n-i) ) * (1 - t)**i


if __name__ == "__main__":
    raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
    
    control_points = raccord.get_bezier_parameters([1, 2, 3], [4, 5, 6], degree=2)