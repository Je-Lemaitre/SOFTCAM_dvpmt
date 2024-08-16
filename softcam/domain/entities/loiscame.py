import dataclasses
from typing import Callable
import numpy as np
import scipy.interpolate as scitp
from domain.services.calculsloiscame import CalculRampe

@dataclasses.dataclass
class LoisPhaseRampe:
    duree_rampe : float
    a_rampe : Callable[[np.ndarray], np.ndarray]
    v_rampe : Callable[[np.ndarray], np.ndarray]
    l_rampe : Callable[[np.ndarray], np.ndarray]
    j_rampe : Callable[[np.ndarray], np.ndarray]                                                   

    def j(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac < 0) | (ac > self.duree_rampe))))
        jerk = self.j_rampe(acm)
        jerk[acm.mask] = 0
        return jerk.reshape(np.shape(ac))
    
    def a(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac < 0) | (ac > self.duree_rampe))))
        accel = self.a_rampe(acm)
        accel[acm.mask] = np.nan
        return accel.reshape(np.shape(ac))
    
    def v(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac < 0) | (ac > self.duree_rampe))))
        vitesse = self.v_rampe(acm)
        vitesse[acm.mask] = 0
        return vitesse.reshape(np.shape(ac))
    
    def l(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac < 0) | (ac > self.duree_rampe))))
        levee = self.l_rampe(acm)
        levee[acm.mask] = 0
        return levee.reshape(np.shape(ac))

    @classmethod
    def from_dict(cls, d):
        calcul_rampe = CalculRampe.from_dict(d["calcul_rampe"])
        return cls(
            duree_rampe = d["duree_rampe"],
            a_rampe = calcul_rampe.a,
            v_rampe = calcul_rampe.v,
            l_rampe = calcul_rampe.l,
            j_rampe = calcul_rampe.j
        )
    
    def to_dict(self):
        return {
            "duree_rampe" : self.duree_rampe,
            "calcul_rampe" : self.a_rampe.__self__.to_dict()
        }

@dataclasses.dataclass
class LoisPhaseAccel:
    duree_accel : float
    levee_rampe : float
    vitesse_rampe : float
    a_spl : scitp.BSpline
    v_spl : scitp.BSpline = None
    l_spl : scitp.BSpline = None
    j_spl : scitp.BSpline = None

    def __post_init__(self):
        if not (self.a_spl is None):
            self.v_spl = self.a_spl.antiderivative()
            self.l_spl = self.v_spl.antiderivative()
            self.j_spl = self.a_spl.derivative()

    def j(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac <= 0) | (ac > self.duree_accel))))
        jerk = self.j_spl(acm)
        jerk[acm.mask] = 0
        return jerk.reshape(np.shape(ac))

    def a(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac <= 0) | (ac > self.duree_accel))))
        accel = self.a_spl(acm)
        accel[acm.mask] = np.nan
        return accel.reshape(np.shape(ac))
    
    def v(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac <= 0) | (ac > self.duree_accel))))
        vitesse = self.v_spl(acm) + self.vitesse_rampe - self.v_spl(0)
        vitesse[acm.mask] = 0
        return vitesse.reshape(np.shape(ac))
    
    def l(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac <= 0) | (ac > self.duree_accel))))
        levee = self.l_spl(acm) + (self.vitesse_rampe - self.v_spl(0))*acm + self.levee_rampe - self.l_spl(0)
        levee[acm.mask] = 0
        return levee.reshape(np.shape(ac))

    @classmethod
    def from_dict(cls, d : dict):
        if d["a_spl"] is None :
            a_spl_import = None
        else :
            a_spl_import = scitp.BSpline(d["a_spl"])
        return cls(
            duree_accel = d["duree_accel"],
            levee_rampe = d["levee_rampe"],
            vitesse_rampe = d["vitesse_rampe"],
            a_spl = a_spl_import
        )

    def to_dict(self):
        if self.a_spl is None :
            a_spl_export = None
        else :
            a_spl_export = self.a_spl.__dict__
        return {
            "duree_accel" : self.duree_accel,
            "levee_rampe" : self.levee_rampe,
            "vitesse_rampe" : self.vitesse_rampe,
            "a_spl" : a_spl_export
        }
    
@dataclasses.dataclass
class LoisPhaseRaccord:
    duree_raccord : float
    levee_init : float
    vitesse_init : float
    a_spl : scitp.BSpline
    v_spl : scitp.BSpline = None
    l_spl : scitp.BSpline = None
    j_spl : scitp.BSpline = None

    def __post_init__(self):
        if not (self.a_spl is None):
            self.v_spl = self.a_spl.antiderivative()
            self.l_spl = self.v_spl.antiderivative()
            self.j_spl = self.a_spl.derivative()

    def j(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac >= 0) | (ac <= -self.duree_raccord))))
        jerk = self.j_spl(acm)
        jerk[acm.mask] = 0
        return jerk.reshape(np.shape(ac))

    def a(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac >= 0) | (ac <= -self.duree_raccord))))
        accel = self.a_spl(acm)
        accel[acm.mask] = np.nan
        return accel.reshape(np.shape(ac))
        
    def v(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac >= 0) | (ac <= -self.duree_raccord))))
        vitesse = self.v_spl(acm) + self.vitesse_init - self.v_spl(0)
        vitesse[acm.mask] = 0
        return vitesse.reshape(np.shape(ac))
    
    def l(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac >= 0) | (ac <= -self.duree_raccord))))
        levee = self.l_spl(acm) + (self.vitesse_init - self.v_spl(0))*acm + self.levee_init - self.l_spl(0)
        levee[acm.mask] = 0
        return levee.reshape(np.shape(ac))
    
    @classmethod
    def from_dict(cls, d):
        if d["a_spl"] is None :
            a_spl_import = None
        else :
            a_spl_import = scitp.BSpline(d["a_spl"])
        return cls(
            duree_raccord = d["duree_raccord"],
            levee_init = d["levee_init"],
            vitesse_init = d["vitesse_init"],
            a_spl = a_spl_import
        )
    
    def to_dict(self):
        if self.a_spl is None :
            a_spl_export = None
        else :
            a_spl_export = self.a_spl.__dict__
        return {
            "duree_raccord" : self.duree_raccord,
            "levee_init" : self.levee_init,
            "vitesse_init" : self.vitesse_init,
            "a_spl" : a_spl_export
            }
    
@dataclasses.dataclass
class LoisPhaseDecel:
    duree_decel : float
    leveemax : float
    a_spl : scitp.BSpline
    v_spl : scitp.BSpline = None
    l_spl : scitp.BSpline = None
    j_spl : scitp.BSpline = None

    def __post_init__(self):
        if not (self.a_spl is None):
            self.v_spl = self.a_spl.antiderivative()
            self.l_spl = self.v_spl.antiderivative()
            self.j_spl = self.a_spl.derivative()

    def j(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < -self.duree_decel))))
        jerk = self.j_spl(acm)
        jerk[acm.mask] = 0
        return jerk.reshape(np.shape(ac))

    def a(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < -self.duree_decel))))
        accel = self.a_spl(acm)
        accel[acm.mask] = np.nan
        return accel.reshape(np.shape(ac))
    
    def v(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < -self.duree_decel))))
        vitesse = self.v_spl(acm) - self.v_spl(0)
        vitesse[acm.mask] = 0
        return vitesse.reshape(np.shape(ac))
    
    def l(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < -self.duree_decel))))
        levee = self.l_spl(acm) -self.v_spl(0)*acm + self.leveemax - self.l_spl(0)
        levee[acm.mask] = 0
        return levee.reshape(np.shape(ac))

    @classmethod
    def from_dict(cls, d):
        if d["a_spl"] is None :
            a_spl_import = None
        else :
            a_spl_import = scitp.BSpline(d["a_spl"]) 
        return cls(
            duree_decel = d["duree_decel"],
            leveemax = d["leveemax"],
            a_spl = a_spl_import
        )    
    def to_dict(self):
        if self.a_spl is None :
            a_spl_export = None
        else :
            a_spl_export = self.a_spl.__dict__
        return {
            "duree_decel" : self.duree_decel,
            "leveemax" : self.leveemax,
            "a_spl" : a_spl_export
        }

@dataclasses.dataclass
class LoisPhaseDecelV2:
    duree_decel : float
    l_init : float
    v_init : float
    a_spl : scitp.BSpline
    v_spl : scitp.BSpline = None
    l_spl : scitp.BSpline = None
    j_spl : scitp.BSpline = None

    def __post_init__(self):
        if not (self.a_spl is None):
            self.v_spl = self.a_spl.antiderivative()
            self.l_spl = self.v_spl.antiderivative()
            self.j_spl = self.a_spl.derivative()

    def j(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < self.duree_decel))))
        jerk = self.j_spl(acm)
        jerk[acm.mask] = 0
        return jerk.reshape(np.shape(ac))

    def a(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < self.duree_decel))))
        accel = self.a_spl(acm)
        accel[acm.mask] = np.nan
        return accel.reshape(np.shape(ac))
    
    def v(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < self.duree_decel))))
        vitesse = self.v_spl(acm) + self.v_init - self.v_spl(0)
        vitesse[acm.mask] = 0
        return vitesse.reshape(np.shape(ac))
    
    def l(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = ((ac > 0) | (ac < self.duree_decel))))
        levee = self.l_spl(acm) + (self.v_init - self.v_spl(0))*acm + self.l_init - self.l_spl(0)
        levee[acm.mask] = 0
        return levee.reshape(np.shape(ac))

    @classmethod
    def from_dict(cls, d):
        if d["a_spl"] is None :
            a_spl_import = None
        else :
            a_spl_import = scitp.BSpline(d["a_spl"]) 
        return cls(
            duree_decel = d["duree_decel"],
            leveemax = d["leveemax"],
            a_spl = a_spl_import
        )    
    def to_dict(self):
        if self.a_spl is None :
            a_spl_export = None
        else :
            a_spl_export = self.a_spl.__dict__
        return {
            "duree_decel" : self.duree_decel,
            "leveemax" : self.leveemax,
            "a_spl" : a_spl_export
        }
    
@dataclasses.dataclass
class DemiLois:
    squelette_acceleration : np.ndarray
    squelette_vitesse : np.ndarray
    squelette_levee : np.ndarray
    ac_fin_rampe : float
    ac_fin_accel : float
    ac_leveemax : float
    ac_raccord : float = None
    lois_rampe : LoisPhaseRampe = None
    lois_accel : LoisPhaseAccel = None
    lois_raccord : LoisPhaseRaccord = None
    lois_decel : LoisPhaseDecel = None
    accelmax_opt : float = None
    regime_affolement_opt : float = None
    
    def __post_init__(self):
        self.ac_raccord = self.ac_fin_accel + self.lois_raccord.duree_raccord

    def j(self,ac):
        return ( np.nan_to_num(self.lois_rampe.j(ac)) 
                + np.nan_to_num(self.lois_accel.j(ac - self.ac_fin_rampe)) 
                + np.nan_to_num(self.lois_raccord.j(ac - self.ac_raccord)) 
                + np.nan_to_num(self.lois_decel.j(ac - self.ac_leveemax))
        )

    def a(self,ac):
        return ( np.nan_to_num(self.lois_rampe.a(ac), copy=False) 
                + np.nan_to_num(self.lois_accel.a(ac - self.ac_fin_rampe), copy=False) 
                + np.nan_to_num(self.lois_raccord.a(ac - self.ac_raccord), copy=False) 
                + np.nan_to_num(self.lois_decel.a(ac - self.ac_leveemax), copy=False)
        )
    
    def v(self,ac):
        return ( np.nan_to_num(self.lois_rampe.v(ac)) 
                + np.nan_to_num(self.lois_accel.v(ac - self.ac_fin_rampe)) 
                + np.nan_to_num(self.lois_raccord.v(ac - self.ac_raccord)) 
                + np.nan_to_num(self.lois_decel.v(ac - self.ac_leveemax))
        )
    
    def l(self,ac):
        return ( np.nan_to_num(self.lois_rampe.l(ac)) 
                + np.nan_to_num(self.lois_accel.l(ac - self.ac_fin_rampe)) 
                + np.nan_to_num(self.lois_raccord.l(ac - self.ac_raccord)) 
                + np.nan_to_num(self.lois_decel.l(ac - self.ac_leveemax))
        )
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            squelette_acceleration = np.array(d["squelette_acceleration"]),
            squelette_vitesse = np.array(d["squelette_vitesse"]),
            squelette_levee = np.array(d["squelette_levee"]),
            ac_fin_rampe = d["ac_fin_rampe"],
            ac_fin_accel = d["ac_fin_accel"],
            ac_leveemax = d["ac_leveemax"],
            ac_raccord = d["ac_raccord"],
            lois_rampe = LoisPhaseRampe.from_dict(d["lois_rampe"]),
            lois_accel = LoisPhaseAccel.from_dict(d["lois_accel"]),
            lois_raccord = LoisPhaseRaccord.from_dict(d["lois_raccord"]),
            lois_decel = LoisPhaseDecel.from_dict(d["lois_decel"]),
            accelmax_opt = d["accelmax_opt"],
            regime_affolement_opt = d["regime_affolement_opt"]
        )
    
    def to_dict(self):
        return {
            "squelette_acceleration" : self.squelette_acceleration,
            "squelette_vitesse" : self.squelette_vitesse,
            "squelette_levee" : self.squelette_levee,
            "ac_fin_rampe" : self.ac_fin_rampe,
            "ac_fin_accel" : self.ac_fin_accel,
            "ac_leveemax" : self.ac_leveemax,
            "ac_raccord" : self.ac_raccord,
            "lois_rampe" : self.lois_rampe.to_dict(),
            "lois_accel" : self.lois_accel.to_dict(),
            "lois_raccord" : self.lois_raccord.to_dict(),
            "lois_decel" : self.lois_decel.to_dict(),
            "accelmax_opt" : self.accelmax_opt,
            "regime_affolement_opt" : self.regime_affolement_opt
        }

@dataclasses.dataclass
class LoisCame:
    symetrie : bool = True
    demilois_ouverture : DemiLois = None
    demilois_fermeture : DemiLois = None
    dac_leveemax_ouverture : float = None
    dac_leveemax_fermeture : float = None

    def j(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = (ac>self.dac_leveemax_ouverture)))
        jerk = self.demilois_ouverture.j(acm)
        jerk[acm.mask] = -self.demilois_fermeture.j(self.dac_leveemax_fermeture + self.dac_leveemax_ouverture - np.atleast_1d(ac)[acm.mask])
        return jerk.reshape(np.shape(ac))

    def a(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = (ac>self.dac_leveemax_ouverture)))
        accel = self.demilois_ouverture.a(acm)
        accel[acm.mask] = self.demilois_fermeture.a(self.dac_leveemax_fermeture + self.dac_leveemax_ouverture - np.atleast_1d(ac)[acm.mask])
        return accel.reshape(np.shape(ac))
    
    def v(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = (ac>self.dac_leveemax_ouverture)))
        vitesse = self.demilois_ouverture.v(acm)
        vitesse[acm.mask] = -self.demilois_fermeture.v(self.dac_leveemax_fermeture + self.dac_leveemax_ouverture - np.atleast_1d(ac)[acm.mask])
        return vitesse.reshape(np.shape(ac))
    
    def l(self,ac):
        acm = np.atleast_1d(np.ma.array(np.asarray(ac), mask = (ac>self.dac_leveemax_ouverture)))
        levee = self.demilois_ouverture.l(acm)
        levee[acm.mask] = self.demilois_fermeture.l(self.dac_leveemax_fermeture + self.dac_leveemax_ouverture - np.atleast_1d(ac)[acm.mask])
        return levee.reshape(np.shape(ac))
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            symetrie = d["symetrie"],
            demilois_ouverture = DemiLois.from_dict(d["demilois_ouverture"]),
            demilois_fermeture = DemiLois.from_dict(d["demilois_fermeture"]),
            dac_leveemax_ouverture = d["dac_leveemax_ouverture"],
            dac_leveemax_fermeture = d["dac_leveemax_fermeture"]
        )

    def to_dict(self):
        return {
            "symetrie" : self.symetrie,
            "demilois_ouverture" : self.demilois_ouverture.to_dict(),
            "demilois_fermeture" : self.demilois_fermeture.to_dict(),
            "dac_leveemax_ouverture" : self.dac_leveemax_ouverture,
            "dac_leveemax_fermeture" : self.dac_leveemax_fermeture   
        }

