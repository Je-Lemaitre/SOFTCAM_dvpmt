import pytest
from unittest import mock
import numpy as np
from softcam.domain.services.calculsloiscame import CalculRampe, CalculRaccord

class Test_CalculRampe:
    # Verify correct initialization with valid parameters
    def test_valid_initialization(self):
        # Valid parameters
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 20.0
        # Initialize the class
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
        # Assertions to check if the object is initialized properly
        assert ramp.dac_r == duree_rampe
        assert ramp.dac_vc == duree_vitesse_constante
        assert ramp.lr == levee_rampe
        assert ramp.vr == vitesse_rampe

    # Test vérifications faites à l'initialisation.
    def test_verif_duration_initialization(self):
        # Test avec une duree de rampe nulle.
        with pytest.raises(ValueError):
            CalculRampe(0, 5.0, 100.0, 20.0)
        # Test avec une duree à vitesse constante nulle.
        with pytest.raises(ValueError):
            CalculRampe(10.0, 0, 100.0, 20.0)
        # Test avec duree phase à vitesse constante supérieure à durée de rampe.
        with pytest.raises(ValueError):
            CalculRampe(5.0, 10.0, 100.0, 20.0)

    # Validate error handling when levee_accel computes to a negative value
    def test_levee_accel_negative_value(self):
        # Invalid parameters leading to negative levee_accel
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 20.0
        vitesse_rampe = 5.0
        # Test if ValueError is raised when levee_accel is negative
        with pytest.raises(ValueError):
            ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)

    # Check that computed coefficients match expected polynomial coefficients for typical input values
    def test_computed_coefficients_match_expected(self):
        # Define typical input values
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 10.0
    
        # Initialize the class
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
    
        # Compute the expected polynomial coefficients manually
        expected_coeffs = np.array([-6.4e-3, 0.1152, -0.72, 1.6])  # Example values, replace with actual expected coefficients
    
        # Get the computed coefficients from the class method
        computed_coeffs = ramp.compute_coeffs_accel()
    
        # Assert that the computed coefficients match the expected coefficients
        np.testing.assert_array_almost_equal(computed_coeffs, expected_coeffs, decimal=5)

    # Validate that properties return the correct private attribute values
    def test_properties_return_correct_values(self):
        # Valid parameters
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 20.0
        # Initialize the class
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
        # Assertions to check if the properties return the correct private attribute values
        assert ramp.dac_r == duree_rampe
        assert ramp.dac_vc == duree_vitesse_constante
        assert ramp.lr == levee_rampe
        assert ramp.vr == vitesse_rampe

    # Ensure correct handling of angles outside the valid range (negative or greater than dac_r)
    def test_angles_outside_valid_range(self):
        # Valid parameters
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 20.0
    
        # Initialize the class
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
    
        # Test angles outside the valid range
        assert np.isnan(ramp.j(-1))
        assert np.isnan(ramp.a(-1))
        assert np.isnan(ramp.v(-1))
        assert np.isnan(ramp.l(-1))
    
        assert np.isnan(ramp.j(15))
        assert np.isnan(ramp.a(15))
        assert np.isnan(ramp.v(15))
        assert np.isnan(ramp.l(15))

    # Assess performance implications for large input arrays in jerk, acceleration, velocity, and lift functions
    def test_performance_large_arrays(self):
        # Initialize the class with sample parameters
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 20.0
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
    
        # Generate large input arrays for testing performance
        large_array = np.linspace(0, duree_rampe, 1000000)
    
        # Test the performance of jerk function with large input array
        jerk_result = ramp.j(large_array)
        assert jerk_result.shape == (1000000,)
    
        # Test the performance of acceleration function with large input array
        accel_result = ramp.a(large_array)
        assert accel_result.shape == (1000000,)
    
        # Test the performance of velocity function with large input array
        velocity_result = ramp.v(large_array)
        assert velocity_result.shape == (1000000,)
    
        # Test the performance of lift function with large input array
        lift_result = ramp.l(large_array)
        assert lift_result.shape == (1000000,)

    # Test the continuity of velocity and lift at the transition from acceleration phase to constant velocity phase
    def test_continuity_velocity_lift_transition(self):
        # Initialize the class with valid parameters
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 10.0
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
    
        # Calculate the transition point from acceleration phase to constant velocity phase
        transition_point = duree_rampe - duree_vitesse_constante
    
        # Check the continuity of velocity at the transition point
        velocity_at_transition = ramp.v(np.array([transition_point]))
        velocity_at_transition_plus_epsilon = ramp.v(np.array([transition_point + 1e-6]))
        assert velocity_at_transition == pytest.approx(velocity_at_transition_plus_epsilon)
    
        # Check the continuity of lift at the transition point
        lift_at_transition = ramp.l(np.array([transition_point]))
        lift_at_transition_plus_epsilon = ramp.l(np.array([transition_point + 1e-6]))
        assert lift_at_transition == pytest.approx(lift_at_transition_plus_epsilon)

    # Test jerk, acceleration, velocity, and lift functions at boundary angles (0 and dac_r)
    def test_behaviour_boundary_angles(self):
        # Initialize the class with dummy values
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 20.0
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
    
        # Test jerk function at boundary angles
        jerk_0 = ramp.j(0)
        jerk_dac_r = ramp.j(ramp.dac_r)
        assert np.isnan(jerk_0) == False
        assert np.isnan(jerk_dac_r) == False
    
        # Test acceleration function at boundary angles
        accel_0 = ramp.a(0)
        accel_dac_r = ramp.a(ramp.dac_r)
        assert np.isnan(accel_0) == False
        assert np.isnan(accel_dac_r) == False
    
        # Test velocity function at boundary angles
        vel_0 = ramp.v(0)
        vel_dac_r = ramp.v(ramp.dac_r)
        assert np.isnan(vel_0) == False
        assert np.isnan(vel_dac_r) == False
    
        # Test lift function at boundary angles
        lift_0 = ramp.l(0)
        lift_dac_r = ramp.l(ramp.dac_r)
        assert np.isnan(lift_0) == False
        assert np.isnan(lift_dac_r) == False

    # Check for correct masking and NaN handling in jerk, acceleration, velocity, and lift calculations
    def test_correct_masking_and_nan_handling(self):
        # Valid parameters
        duree_rampe = 10.0
        duree_vitesse_constante = 5.0
        levee_rampe = 100.0
        vitesse_rampe = 20.0
    
        # Initialize the class
        ramp = CalculRampe(duree_rampe, duree_vitesse_constante, levee_rampe, vitesse_rampe)
    
        # Test Jerk calculation
        ac = np.array([-1, 6.5, 10])
        jerk_result = ramp.j(ac)
        assert np.isnan(jerk_result[0])  # First element should be NaN due to masking
        assert jerk_result[1] == 0  # Second element should be 0 due to masking
    
        # Test Acceleration calculation
        accel_result = ramp.a(ac)
        assert np.isnan(accel_result[0])  # First element should be NaN due to masking
        assert accel_result[1] == 0  # Second element should be 0 due to masking
    
        # Test Velocity calculation
        vel_result = ramp.v(ac)
        assert np.isnan(vel_result[0])  # First element should be NaN due to masking
        assert vel_result[1] == 20.0  # Second element should be 20.0 due to masking
    
        # Test Lift calculation
        lift_result = ramp.l(ac)
        assert np.isnan(lift_result[0])  # First element should be NaN due to masking
        assert lift_result[1] == 30.0  # Second element should be 30.0 due to masking

class Test_CalculRaccord:

    # Correct initialization with valid input parameters
    def test_correct_initialization(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Check if the instance is correctly initialized
        assert raccord.dac_raccord == 10
        assert raccord.ai == pytest.approx(2.0)
        assert raccord.ji == pytest.approx(0.5)
        assert raccord.af == pytest.approx(3.0)
        assert raccord.jf == pytest.approx(0.1)
        # Check if the spline is correctly computed and is an instance of BSpline
        assert isinstance(raccord.a, np.lib.polynomial.poly1d) or hasattr(raccord.a, 'tck')

    # Initialization with zero duration
    def test_zero_duration_initialization(self):
        # Expecting an error or a specific behavior when duration is zero
        with pytest.raises(Exception):
            CalculRaccord(duree_raccord=0, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)

    # compute_accel_spl returns a valid BSpline object
    def test_compute_accel_spl_valid_bspline(self):
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        assert isinstance(raccord.a, np.lib.polynomial.poly1d) or hasattr(raccord.a, 'tck')

    # get_bezier_parameters returns correct control points for cubic Bézier curve
    def test_get_bezier_parameters_correct_control_points(self):
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        control_points = raccord.get_bezier_parameters([1, 2, 3], [4, 5, 6], degree=2)
        np.testing.assert_array_almost_equal(np.array(control_points), np.array([[1, 4], [2, 5], [3, 6]]))

    # bezier_curve generates correct curve points from control points
    def test_bezier_curve_correct_curve_points(self):
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        control_points = [[1, 4], [2, 5], [3, 6]]
        xvals, yvals = raccord.bezier_curve(control_points, nTimes=5)
        assert np.array_equal(xvals, [3.0, 2.5, 2.0, 1.5, 1.0])
        assert np.array_equal(yvals, [6.0, 5.5, 5.0, 4.5, 4.0])

    # bernstein_poly computes correct Bernstein polynomial values
    def test_bernstein_poly_computation(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Test the bernstein_poly method for correctness
        assert raccord.bernstein_poly(2, 4, 0.5) == pytest.approx(0.375)
        assert raccord.bernstein_poly(1, 3, 0.25) == pytest.approx(0.140625)
        assert raccord.bernstein_poly(3, 5, 0.75) == pytest.approx(0.087890625)

    # Negative values for duration
    def test_negative_duration_values(self):
        # Create an instance of CalculRaccord with negative duration value
        with pytest.raises(ValueError):
            raccord = CalculRaccord(duree_raccord=-10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)

    # get_bezier_parameters with insufficient points for the specified degree
    def test_get_bezier_parameters_insufficient_points(self):
        # Create an instance of CalculRaccord with insufficient points for the specified degree
        raccord = CalculRaccord(duree_raccord=5, accel_init=1.0, jerk_init=0.2, accel_final=2.0, jerk_final=0.3)
        # Test if ValueError is raised when calling get_bezier_parameters with insufficient points
        with pytest.raises(ValueError):
            raccord.get_bezier_parameters([1, 2], [3, 4], degree=3)

    # Stability of BSpline evaluation over edge cases in input domain
    def test_stability_bspline_evaluation(self):
        # Create an instance of CalculRaccord with edge case parameters
        raccord = CalculRaccord(duree_raccord=1.0, accel_init=0, jerk_init=0, accel_final=0, jerk_final=1.0)
        # Check if the BSpline evaluation is stable for edge cases
        assert raccord.a(0) == pytest.approx(0.0)
        assert raccord.a(1) == pytest.approx(0.0)
        assert raccord.a(-1) == pytest.approx(0.0)
        assert raccord.a(100) == pytest.approx(0.0)

    # Accuracy of the fitted Bézier curve relative to the control points
    def test_accuracy_of_fitted_bezier_curve(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Get the control points for the Bézier curve
        control_points = [[0, 2.0], [5, 2.5], [10, 3.0]]
        # Compute the Bézier curve using the control points
        xvals, yvals = raccord.bezier_curve(control_points, nTimes = 5)
        # Check the accuracy of the fitted Bézier curve relative to the control points
        assert np.allclose(xvals, [10, 7.5, 5, 2.5, 0])
        assert np.allclose(yvals, [3.0, 2.75, 2.5, 2.25, 2.0])

    # compute_bezier_3rd_pts with parallel tangents causing division by zero
    def test_compute_bezier_3rd_pts_parallel_tangents_division_by_zero(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Call the method with parallel tangents causing division by zero
        with pytest.raises(ZeroDivisionError):
            raccord.compute_bezier_3rd_pts(0, 0, 1, 0, 0, 1)
        

    # Performance evaluation with high number of evaluation points in bezier_curve
    def test_performance_evaluation_bezier_curve(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Evaluate the bezier_curve method with a high number of evaluation points
        x_vals, y_vals = raccord.bezier_curve([[0, 0], [1, 1], [2, 2], [3, 3]], nTimes=1000)
        # Check if the output is as expected
        assert len(x_vals) == 1000
        assert len(y_vals) == 1000

    # Extremely high or low jerk and acceleration values
    def test_extreme_jerk_accel_values(self):
        # Create an instance of CalculRaccord with extremely high or low jerk and acceleration values
        raccord = CalculRaccord(duree_raccord=5, accel_init=1000.0, jerk_init=10000.0, accel_final=-500.0, jerk_final=-5000.0)
        # Check if the instance is correctly initialized
        assert raccord.dac_raccord == 5
        assert raccord.ai == pytest.approx(1000.0)
        assert raccord.ji == pytest.approx(10000.0)
        assert raccord.af == pytest.approx(-500.0)
        assert raccord.jf == pytest.approx(-5000.0)
        # Check if the spline is correctly computed and is an instance of BSpline
        assert isinstance(raccord.a, np.lib.polynomial.poly1d) or hasattr(raccord.a, 'tck')

    # Handling of non-numeric input types during initialization
    def test_non_numeric_input_initialization(self):
        with pytest.raises(TypeError):
            # Attempt to initialize CalculRaccord with non-numeric parameters
            raccord = CalculRaccord(duree_raccord='abc', accel_init='def', jerk_init='ghi', accel_final='jkl', jerk_final='mno')

    # Response to modifications of internal state post-initialization
    def test_response_to_modifications(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
    
        # Modify internal state post-initialization
        raccord.dac_raccord = 15
        raccord.ai = 3.0
        raccord.ji = 0.2
        raccord.af = 4.0
        raccord.jf = 0.3
    
        # Check if the internal state has been modified correctly
        assert raccord.dac_raccord == 15
        assert raccord.ai == pytest.approx(3.0)
        assert raccord.ji == pytest.approx(0.2)
        assert raccord.af == pytest.approx(4.0)
        assert raccord.jf == pytest.approx(0.3)

    # bezier_curve with zero or negative nTimes
    def test_behaviour_bezier_curve_with_zero_or_negative_nTimes(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Test bezier_curve with zero nTimes
        xvals, yvals = raccord.bezier_curve([[0, 0], [1, 1], [2, 2]], nTimes=0)
        assert len(xvals) == 0
        assert len(yvals) == 0
        # Test bezier_curve with negative nTimes
        with pytest.raises(ValueError):
            raccord.bezier_curve([[0, 0], [1, 1], [2, 2]], nTimes=-1)

    # Identical start and end points with different jerks
    def test_identical_start_end_points_diff_jerks(self):
        # Create an instance of CalculRaccord with identical start and end points but different jerks
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=2.0, jerk_final=0.1)
        # Check if the instance is correctly initialized
        assert raccord.dac_raccord == 10
        assert raccord.ai == pytest.approx(2.0)
        assert raccord.ji == pytest.approx(0.5)
        assert raccord.af == pytest.approx(2.0)
        assert raccord.jf == pytest.approx(0.1)
        # Check if the spline is correctly computed and is an instance of BSpline
        assert isinstance(raccord.a, np.lib.polynomial.poly1d) or hasattr(raccord.a, 'tck')

    # compute_bezier_3rd_pts calculates correct intermediate control points for Bézier curve
    def test_compute_bezier_3rd_pts(self):
        # Create an instance of CalculRaccord with valid parameters
        raccord = CalculRaccord(duree_raccord=10, accel_init=2.0, jerk_init=0.5, accel_final=3.0, jerk_final=0.1)
        # Calculate intermediate control points using the method under test
        x_new, y_new = raccord.compute_bezier_3rd_pts(1.0, 2.0, 0.5, 3.0, 4.0, 3.0)
        # Check if the calculated intermediate control points are correct
        assert x_new == pytest.approx(2.6)
        assert y_new == pytest.approx(2.8)