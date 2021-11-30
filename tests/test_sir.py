import pytest
import numpy as np

def test_sir1() :
    import src.sir

    ## set time points between 0 and 30 in steps (h) of 1
    t = np.arange(0, 30, 1)

    ## call with rho=1.5 and alpha=0.9
    I = src.sir.main(t, 1.5, 0.9)

    assert np.around(I[10], 3) == 0.093 and np.around(I[15], 3) == 0.349 and np.around(I[29], 1) == 0.4

def test_sir2() :
    import src.sir

    ## set time points between 0 and 30 in steps (h) of 1
    t = np.arange(0, 30, 1)

    ## call with rho=1.5 and alpha=1.9
    I = src.sir.main(t, 1.5, 1.9)

    assert np.around(I[0], 3) == 0.001 and np.around(I[15], 3) == 0.000 and np.around(I[29], 3) == 0.000

def test_sir3() :
    import src.sir

    ## set time points between 0 and 30 in steps (h) of 1
    t = np.arange(0, 30, 1)

    ## call with rho=2 and alpha=0.5
    I = src.sir.main(t, 2, 0.5)

    assert np.around(I[5], 3) == 0.093 and np.around(I[10], 3) == 0.742 and np.around(I[29], 3) == 0.750

def test_sirv1() :
    import src.sirv

    ## set time points between 0 and 30 in steps (h) of 1
    t = np.arange(0, 30, 1)

    ## call with rho=1.5, alpha=0.9 and R=0
    I = src.sirv.main(t, 1.5, 0.9, 0)

    assert np.around(I[10], 3) == 0.093 and np.around(I[15], 3) == 0.349 and np.around(I[29], 1) == 0.4

def test_sirv2() :
    import src.sirv

    ## set time points between 0 and 30 in steps (h) of 1
    t = np.arange(0, 30, 1)

    ## call with rho=1.5, alpha=0.9 and R=0.1
    I = src.sirv.main(t, 1.5, 0.9, 0.1)

    assert np.around(I[10], 3) == 0.038 and np.around(I[15], 3) == 0.159 and np.around(I[29], 1) == 0.3

def test_sirv3() :
    import src.sirv

    ## set time points between 0 and 30 in steps (h) of 1
    t = np.arange(0, 30, 1)

    ## call with rho=1.5, alpha=0.9 and R=0.2
    I = src.sirv.main(t, 1.5, 0.9, 0.2)

    assert np.around(I[10], 3) == 0.013 and np.around(I[15], 3) == 0.043 and np.around(I[29], 3) == 0.191
