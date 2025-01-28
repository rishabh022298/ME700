'''Please ensure that pytest and numpy packages are installed before running this file. 
More information is provided in README.md
'''

import pytest
from bisection_method import *

'''
Function $$f(x) = x^3 - 27$$ is defined and test cases are written around
calculating its real root which is at $$x = 3$$.
'''
f = lambda x: x**3 - 27

'''
Test 1: Finding root for a known equation.
    This test checks if the calculated root using  bisection method is correct 
    or not. The lower and upper limits for this test are set 2 and 4 respectively.
'''
def test_for_calculating_root():
    root = bisection(f, 2, 4, tol = 1e-6, max_iter = 100)
    assert abs(root - 3) < 1e-6             

'''
Test 2: Finding root when upper limit is far from the root.
    This test is similar to Test 1. The only difference is that the upper limit 
    is kept farther away at 100. The lower limit is still at 2.
'''
def test_for_farther_upper_limit():
    root = bisection(f, 2, 100, tol = 1e-6, max_iter = 100)
    assert abs(root - 3) < 1e-6

'''
Test 3: Finding root when lower limit is far from the root.
    This test is similar to Test 1. The only difference is that the lower limit 
    is kept farther away at -100. The upper limit is 4.
'''
def test_for_farther_lower_limit():
    root = bisection(f, -100, 4, tol = 1e-6, max_iter = 100)
    assert abs(root - 3) < 1e-6

'''
Test 4: Finding root when both upper and lower limits are far away from the root.
    The lower and upper limit for testing the bisection method for $$f(x)$$ 
    are set as -100 and 100 respectively.
'''
def test_for_farther_limits():
    root = bisection(f, -100, 100, tol = 1e-6, max_iter = 100)
    assert abs(root - 3) < 1e-6

'''
Test 5: Test for $$a < b$$
    This test checks if the lower limit is actually smaller than the upper limit.
    The lower limit is set as 4 and the upper limit is set as 2. If $$a$$ is not 
    smaller than $$b$$ then an error message is expected.
'''
def test_for_correct_limits():
    with pytest.raises(ValueError, match = "a should be smaller than b."):
        bisection(f, 4, 2, tol = 1e-6, max_iter = 100)

'''
Test 6: When root is outside the lower and upper limit.
    The lower and upper limit are set as 4 and 6 so that the actual root $$x = 3$$ 
    does not lie between them. An error message is expected.
'''
def test_for_root_outside_the_limits():
    with pytest.raises(ValueError, match = "The values of the function at a and b should have different signs. Try changing the limits"):
        bisection(f, 4, 6, tol = 1e-6, max_iter = 100)

'''
Test 7: Finding root when lower limit is a root itself.
    The lower limit is set as 3 and upper limit is set as 4 for this test.
'''
def test_for_lower_limit_as_a_root_itself():
    root = bisection(f, 3, 4, tol = 1e-6, max_iter = 100)
    assert abs(root - 3) < 1e-6

'''
Test 8: Finding root when upper limit is a root itself.
    The lower limit is set as 2 and upper limit is set as 3 for this test.
'''
def test_for_upper_limit_as_a_root_itself():
    root = bisection(f, 2, 3, tol = 1e-6, max_iter = 100)
    assert abs(root - 3) < 1e-6

'''
Test 9: Convergence taking too long.
    This test checks if the convergence is taking too long. The tolerance is
    set 1e-16. The lower and upper limit are set as -100 and 100 respectively.
    An error message is expected.
'''
def test_for_convergence():
    with pytest.raises(RuntimeError, match = "Convergence is taking too long. Try increasing the tolerance or increasing the maximum number of iterations allowed."):
        bisection(f, -100, 100, tol = 1e-16, max_iter = 10)