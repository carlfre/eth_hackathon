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
) -> tuple[float, float, float, float]:

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
        tol=1e-8,
        options={"maxiter": 10000}

    )
    alpha, beta, gamma = res.x
    if debug:
        print(res)

    return alpha, beta, gamma, res.fun



def main():
    theta = 0.5
    phi = 0
    lamb = 0

    thetaprime = 0.5
    phistar = 0
    lambstar = 0
    alpha, beta, gamma,  difference = prod_U3s(
        theta,
        phi,
        lamb,
        thetaprime,
        phistar,
        lambstar
    )
    # print(difference)


    # A = U3(theta, phi, lamb)
    # print(np.allclose(U3(theta, phi, lamb) @ U3(thetaprime, phistar, lambstar), U3(alpha, beta, gamma)))
    # print(alpha, beta, gamma)


    # print(theta, phi, lamb)
    # print(thetaprime, phistar, lambstar)
    # print(alpha, beta, gamma)
    # # print("ajlj", (beta + gamma) % np.pi)
    # print(U3(theta, phi, lamb) @ U3(thetaprime, phistar, lambstar))
    # print(U3(alpha, beta, gamma))

    A1 = U3(np.pi/2, 0, np.pi)

    A2 = U3(np.pi/2, 0, 2*np.pi)
    B = U3(np.pi/2, 0, np.pi)

    print(np.linalg.norm(A2 @ A1 - B))

if __name__ == "__main__":
    main()
