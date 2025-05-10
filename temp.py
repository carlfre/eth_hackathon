import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=1000)

I = np.eye(2, dtype=complex)

def direct_sum(A: np.ndarray, B: np.ndarray):

    n = A.shape[0]
    m = B.shape[0]

    return np.block([[A, np.zeros((n, m))], [np.zeros((m, n)), B]])


def Z():
    return np.array([[1, 0], [0, -1]], dtype=complex)

def CZ():
    return direct_sum(I, Z())


def Rz(theta: float):

    return np.diag([np.exp(-1j * theta / 2), np.exp(1j * theta / 2)])


def U3(theta: float, phi: float, lamb: float):
    return np.array([[np.cos(theta / 2), -np.exp(1j * lamb) * np.sin(theta / 2)],
                     [np.exp(1j * phi) * np.sin(theta / 2), np.exp(1j * (phi + lamb)) * np.cos(theta / 2)]
                     ], dtype=complex)

def CRz(theta: float):
    return direct_sum(I, Rz(theta))

theta = np.pi / 4

A = CRz(theta)
print(A)


closest = None

min_dist = float('inf')


dists = []
for theta in np.linspace(0, 2 * np.pi, 20):
    for phi in np.linspace(0, 2 * np.pi, 20):
        for lamb in np.linspace(0, 2 * np.pi, 20):
            U = U3(theta, phi, lamb)

            candidate = CZ() @ np.kron(U, I) @ CZ()
            # print()
            print(candidate)
            if np.linalg.norm(A - candidate) < min_dist:
                min_dist = np.linalg.norm(A - candidate)
                params = (theta, phi, lamb)
                closest = U

print("Closest U3 parameters:", params)
print(min_dist)
print( A)



            # for thetaprime in np.linspace(0, 2 * np.pi, 5):
            #     for phiprime in np.linspace(0, 2 * np.pi, 5):
            #         for lambprime in np.linspace(0, 2 * np.pi, 5):
            #             Uprime = U3(thetaprime, phiprime, lambprime)




                        



# b1 = np.kron(I, Rz(theta/2)) 
# b2 = CZ()
# b3 = np.kron(I, Rz(-theta/2))
# b4 = CZ()


# B = b1 @ b2 @ b3 @ b4

# print(B)




# a = np.ones((3, 3))
# b = np.ones((2, 2))

# print(direct_sum(a, b))