import numpy as np
from scipy.optimize import minimize


def prod_U3s(
        params1: tuple[float, float, float],
        params2: tuple[float, float, float],
        params3: tuple[float, float, float]
) -> tuple[float, float, float]:

    U1 = U3(*params1)
    U2 = U3(*params2)
    U3 = U3(*params3)


    
    
    
    # U_prod_true = U1 @ U2 @ U3
    # U = U3(theta, phi, lamb)
    Uprime = U3(thetaprime, phistar, lambstar)
    U_prod_true = U @ Uprime

    x_start, y_start, z_start = np.random.rand(3) * 2 * np.pi
    alpha_start, beta_start, gamma_start = np.random.rand(3) * 2 * np.pi


    def objective(params):
        Uprod_estimate = U3(params[0], params[1], params[2])
        return np.linalg.norm(U_prod_true - Uprod_estimate)
    
    res = minimize(
        objective,
        [alpha_start, beta_start, gamma_start],
        method="BFGS",
        tol=1e-10,
        options={"maxiter": 10000}

    )
    alpha, beta, gamma = res.x

    print(res)
    return alpha, beta, gamma, res.fun