import numpy as np

from scipy.optimize import minimize


def U3(
    theta: float,
    phi: float,
    lamb: float,
) -> np.ndarray:
    return np.array(
        [
            [np.exp(-1j * (phi + lamb)/2) * np.cos(theta / 2), -np.exp(- 1j * (phi - lamb)/2) * np.sin(theta / 2)],
            [np.exp(1j * (phi - lamb)/2 ) * np.sin(theta / 2), np.exp(1j * (phi + lamb)/ 2) * (np.cos(theta / 2)),],
        ]
    )


def prod_U3s(
    theta: float,
    phi: float,
    lamb: float,
    thetaprime: float,
    phistar: float,
    lambstar: float,
    debug: bool = False,
) -> tuple[float, float, float]:

    U = U3(theta, phi, lamb)
    Uprime = U3(thetaprime, phistar, lambstar)
    U_prod_true = U @ Uprime

    alpha_start, beta_start, gamma_start = np.random.rand(3) * 2 * np.pi

    def objective(params):
        Uprod_estimate = U3(params[0], params[1], params[2])
        return np.linalg.norm(U_prod_true - Uprod_estimate)
    
    res = minimize(
        objective,
        [alpha_start, beta_start, gamma_start],
        method="BFGS",
        tol=1e-5,
        options={"maxiter": 10000}

    )
    alpha, beta, gamma = res.x
    if debug:
        print(res)
        
    return alpha, beta, gamma, res.fun



def main():
    theta = 1
    phi = 0.7
    lamb = 3

    thetaprime = 1
    phistar = 2
    lambstar = 3.4
    alpha, beta, gamma,  difference = prod_U3s(
        theta,
        phi,
        lamb,
        thetaprime,
        phistar,
        lambstar
    )
    print(difference)


    A = U3(theta, phi, lamb)
    print(np.allclose(U3(theta, phi, lamb) @ U3(thetaprime, phistar, lambstar), U3(alpha, beta, gamma)))


if __name__ == "__main__":
    main()
