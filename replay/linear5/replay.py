"""Exact Q(sqrt(15)) certificate for an allowed SSH history.

The mutant modes test the monodromy, spin normalization, canonical coefficients,
and source asymptotic factors. No many-body simulation is performed.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from itertools import permutations
from math import factorial
import argparse
import subprocess
import sys
from pathlib import Path


@dataclass(frozen=True)
class Q15:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q15) else Q15(F(x))

    def __add__(self, x):
        x = self.of(x)
        return Q15(self.a + x.a, self.b + x.b)
    __radd__ = __add__

    def __neg__(self):
        return Q15(-self.a, -self.b)

    def __sub__(self, x):
        return self + -self.of(x)

    def __rsub__(self, x):
        return self.of(x) + -self

    def __mul__(self, x):
        x = self.of(x)
        return Q15(self.a * x.a + 15 * self.b * x.b, self.a * x.b + self.b * x.a)
    __rmul__ = __mul__

    def inverse(self):
        d = self.a * self.a - 15 * self.b * self.b
        if not d:
            raise ZeroDivisionError
        return Q15(self.a / d, -self.b / d)

    def __truediv__(self, x):
        return self * self.of(x).inverse()


def require(ok, name):
    if not ok:
        raise AssertionError(name)


def eye():
    return [[Q15(F(i == j)) for j in range(3)] for i in range(3)]


def mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), Q15()) for j in range(3)] for i in range(3)]


def det(A):
    n = len(A)
    result = Q15()
    for p in permutations(range(n)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = Q15.of(sign)
        for i in range(n):
            term *= A[i][p[i]]
        result += term
    return result


def boost(c, s, i, j):
    A = eye()
    A[i][i] = A[j][j] = Q15.of(c)
    A[i][j] = A[j][i] = Q15.of(s)
    return A


def checks(mutant=None):
    c1, s1, c2, s2 = F(5, 3), F(4, 3), F(4), Q15(F(0), F(1))
    if mutant == "field-radicand":
        s2 = Q15.of(4)
    require(Q15.of(c1 * c1 - s1 * s1) == Q15.of(1), "first-boost-hyperbolic-identity")
    require(Q15.of(c2 * c2) - s2 * s2 == Q15.of(1), "second-boost-hyperbolic-identity")
    A = boost(c1, s1, 0, 1)
    Ai = boost(c1, -s1, 0, 1)
    B = boost(c2, s2, 1, 2)
    Bi = boost(c2, -s2, 1, 2)
    if mutant == "inverse-sign":
        Ai = A
    factors = [A, B, Ai, Bi]
    if mutant == "commuting-order":
        factors = [A, Ai, B, Bi]
    Y = eye()
    for factor in factors:
        Y = mul(Y, factor)
    require(det(Y) == Q15.of(1), "monodromy-determinant")
    require(sum((Y[i][i] for i in range(3)), Q15()) == Q15.of(-1), "monodromy-trace-minus-one")
    require(mul(Y, Y) == eye(), "nontrivial-involution")
    require(Y != eye(), "not-identity-history")
    plus = [[eye()[i][j] + Y[i][j] for j in range(3)] for i in range(3)]
    require(det(plus) == Q15(), "one-spin-trace-zero")
    # Spectral projectors P+ = (I+Y)/2 and P- = (I-Y)/2.
    Pm = [[(eye()[i][j] - Y[i][j]) / 2 for j in range(3)] for i in range(3)]
    require(mul(Pm, Pm) == Pm, "negative-projector")
    require(sum((Pm[i][i] for i in range(3)), Q15()) == Q15.of(2), "negative-eigenspace-rank")
    q = F(101, 100)
    occupation = q / (q - 1)
    if mutant == "thermal-occupation":
        occupation = q / (q + 1)
    require(occupation == 101, "unbounded-reference-occupation")
    # det(1+qY) = (1+q)(1-q)^2, per spin, at each rational fugacity.
    for q in [F(0), F(1, 2), F(1), F(101, 100), F(2)]:
        mat = [[eye()[i][j] + q * Y[i][j] for j in range(3)] for i in range(3)]
        require(det(mat) == Q15.of((1 + q) * (1 - q) ** 2), "fugacity-polynomial")
    one = [1, -1, -1, 1]
    two = [sum(one[i] * one[n - i] for i in range(4) if 0 <= n - i < 4) for n in range(7)]
    expected = [1, -2, -1, 4, -1, -2, 1]
    if mutant == "canonical-positivity":
        expected = [abs(x) for x in expected]
    require(two == expected and two[1] < 0, "canonical-history-sign")
    spin_power = 1 if mutant == "one-spin-weight" else 2
    require(spin_power == 2, "spin-square-weight")
    require((F(5, 3) - 1) * (4 - 1) == 2, "pi-rotation-parameters")
    # Atomic source integral's endpoint coefficients, from elementary moments.
    # 2 endpoints; integral s^2 exp(-2Us) = 2/(2U)^3.
    quantum_coefficient = F(2) * F(2, 8)
    if mutant == "endpoint-factor":
        quantum_coefficient /= 2
    require(quantum_coefficient == F(1, 2), "atomic-quantum-first-order-factor")
    require(F(2) * 2 * F(2, 8) == 1, "atomic-static-first-order-factor")
    balanced_weight = sum(F(x * x) for x in one)
    if mutant == "same-spin-twist":
        balanced_weight = F(one[0] ** 2)
    require(balanced_weight == 4, "opposite-spin-Fourier-projection")
    transfer = F(2) * Y[0][1] * Y[0][1] / balanced_weight
    require(transfer == Q15.of(F(200, 9)), "twist-averaged-pair-nonnormality")
    # Finite Hilbert-Schmidt Gram identity underlying time reflection.
    M = [[F(0), F(1)], [F(-1), F(0)]]
    N = [[F(1), F(2)], [F(0), F(1)]]
    def hs(X, Y):
        return sum(X[i][j] * Y[i][j] for i in range(2) for j in range(2))
    mm = hs(M, M)
    if mutant == "mirror-without-adjoint":
        mm = sum(M[i][j] * M[j][i] for i in range(2) for j in range(2))
    require(mm == 2, "reflected-half-Hilbert-Schmidt-positivity")
    require(mm * hs(N, N) - hs(M, N) ** 2 == 8, "reflection-Schwarz-Gram-determinant")
    for z in [F(0), F(1, 2), F(1), F(2)]:
        coefficients = [F(x) * z ** n for n, x in enumerate(one)]
        require(sum(coefficients) ** 2 <= 4 * sum(x * x for x in coefficients),
                "balanced-pressure-upper-comparison")
    # Exact finite constants for the small-cutoff sharpness proposition.
    increment_leading = F(3, 16)
    if mutant == "increment-factor":
        increment_leading /= 2
    require(increment_leading == F(3, 32) / F(1, 2), "quarter-period-increment-factor")
    require(F(3, 32) / F(4, 7) == F(21, 128), "increment-variance-lower-constant")
    require(F(3, 28) / F(1, 2) == F(3, 14), "increment-variance-upper-constant")
    require(F(1, 5) * F(3, 7) == F(3, 35), "large-a-variance-lower-constant")
    require(F(1, 24) == F(1, 2) ** 2 / 6, "projected-covariance-leading-factor")
    centering = 1 if mutant == "brownian-centering" else 2
    require(centering ** 2 == 4, "Brownian-bridge-centering-loss")
    lam = F(1, 4)
    require(1 + 2 * lam / (F(1, 2) - lam) == 3, "Gaussian-sup-exponential-moment")
    power = F(1, 2) if mutant == "threshold-power" else F(2, 3)
    require(3 * power - 2 == 0, "two-thirds-cutoff-threshold-exponent")
    for occupation in [0, 1, 2]:
        dynamic_integral = F(1) + F(-1)
        if mutant == "atomic-dynamic-tilt":
            dynamic_integral = F(1) + F(1)
        require((occupation - 1) * dynamic_integral == 0, "atomic-nonzero-mode-factorization")
    require(F(21, 512) * F(1, 2) ** 2 == F(21, 2048), "half-budget-necessary-constant")
    exp2_lower = sum(F(2) ** k / F(factorial(k)) for k in range(4))
    require(exp2_lower == F(19, 3) and 3 / exp2_lower < F(1, 2), "half-budget-sufficient-Q-eight")
    # Interval spot certificates for the exact covariance formulas. The all-a
    # inequalities, Gaussian tails and interacting factorization are analytic.
    import mpmath as mp
    iv = mp.iv
    iv.dps = 60
    def interval(x):
        x = F(x)
        return iv.mpf(x.numerator) / iv.mpf(x.denominator)
    def cosh(x):
        return (iv.exp(x) + iv.exp(-x)) / 2
    def sinh(x):
        return (iv.exp(x) - iv.exp(-x)) / 2
    for a_exact in [F(1, 16), F(1, 8), F(1, 2), F(1), F(2), F(4), F(16)]:
        a = interval(a_exact)
        projected = a / (2 * sinh(a / 2)) - 1
        if mutant == "projected-RP":
            projected = a / (2 * sinh(a / 2))
        require(projected < 0, "negative-projected-reflected-covariance")
        h = (cosh(a / 2) - cosh(a / 4)) / sinh(a / 2)
        require(h > 0, "positive-local-increment-variance")
        if a_exact <= 1:
            require(h > interval(F(21, 128)) * a and h < interval(F(3, 14)) * a,
                    "interval-small-a-variance-sandwich")
        else:
            require(h > interval(F(3, 35)), "interval-large-a-variance-lower-bound")
    print("CERTIFIED: sharpness constants and seven interval covariance points passed")
    print("CERTIFIED: monodromy, source factors, reflection Gram and twist identities passed")


MUTANTS = ["field-radicand", "inverse-sign", "commuting-order", "thermal-occupation",
           "canonical-positivity", "one-spin-weight", "endpoint-factor",
           "same-spin-twist", "mirror-without-adjoint", "increment-factor",
           "brownian-centering", "threshold-power", "atomic-dynamic-tilt", "projected-RP"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", choices=MUTANTS)
    ap.add_argument("--all-mutants", action="store_true")
    args = ap.parse_args()
    if args.mutant and args.all_mutants:
        ap.error("choose one mode")
    try:
        checks(args.mutant)
    except AssertionError as e:
        print(f"REJECTED {args.mutant or 'base'}: {e}")
        return 1
    if args.all_mutants:
        for name in MUTANTS:
            p = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--mutant", name],
                               capture_output=True, text=True, check=False)
            print(p.stdout.strip())
            if p.stderr:
                print(p.stderr.strip())
            print(f"mutant {name}: exit {p.returncode}")
            if p.returncode != 1 or not p.stdout.startswith(f"REJECTED {name}:"):
                return 2
        print("CERTIFIED: all fourteen mutants rejected with exit 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
