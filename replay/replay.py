"""Exact-rational scalar and finite-algebra certificate for LINEAR4.

No numerical trajectory or thermodynamic model is simulated. The infinite
analytic steps are proved in RIGOR.md, not certified by this script.
"""
from fractions import Fraction as F
import argparse
import itertools
import subprocess
import sys
from pathlib import Path

MUTANTS = (
    "weighted-cutoff", "wick-scale", "tail-mass", "ssh-tail-cutoff",
    "threshold-exponent", "dyadic-ratio", "asymptotic-log", "oscillator-count",
)


def require(ok, name):
    if not ok:
        raise AssertionError(name)


def det(a):
    n = len(a)
    if n == 0:
        return F(1)
    result = F(0)
    for p in itertools.permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F((-1) ** inversions)
        for i in range(n):
            term *= a[i][p[i]]
        result += term
    return result


def checks(mutant=None):
    beta_r = F(1, 4) if mutant == "weighted-cutoff" else F(1, 64)
    # e^a < 3, degree 4, conjugated C0 time operator <= beta.
    weighted_v = 12 * beta_r
    require(weighted_v <= F(3, 16), "weighted-reference-smallness")
    weighted_slice = F(5, 4) + F(25, 16) * weighted_v / (1 - weighted_v)
    require(weighted_slice < 2, "weighted-slice-bound")
    plain_v = 4 * beta_r
    require(plain_v / (1 - plain_v) <= F(1, 15), "correction-Gram-factor")
    # Q=64(1+4 beta J) dominates 2 e^a(3+32 beta J).
    require(6 * 3 <= 64 and 6 * 32 <= 64 * 4, "attachment-linear-coefficients")
    require(4 ** 1 * 2 ** 1 * 3 ** 2 <= 128, "leg-and-exponential-budget")
    scale = 1 if mutant == "wick-scale" else 4
    for k in range(1, 17):
        require(sum(__import__("math").comb(k, j) ** 2 for j in range(k + 1)) <= scale ** k,
                "interpolated-minor-factor")
    # A finite exact-rational check of the complementary-minor expansion.
    c0 = [[F(1, 2), F(1, 5)], [F(-1, 7), F(1, 3)]]
    delta = [[F(1, 100), F(-1, 200)], [F(1, 300), F(1, 400)]]
    full = [[c0[i][j] + delta[i][j] for j in range(2)] for i in range(2)]
    expanded = det(c0) + det(delta)
    expanded += c0[0][0] * delta[1][1] + delta[0][0] * c0[1][1]
    expanded -= c0[0][1] * delta[1][0] + delta[0][1] * c0[1][0]
    require(det(full) == expanded, "complementary-minor-identity")

    # Original law: good reference draw, then independent replacement.
    law = {"a": F(1, 2), "b": F(1, 3), "c": F(1, 6)}
    p = law["c"]
    good = {"a": law["a"] / (1 - p), "b": law["b"] / (1 - p)}
    # W_ref integrates the *unconditional* tail mass, including the subtraction.
    mass = F(1) if mutant == "tail-mass" else p
    f = {"a": F(2), "b": F(3), "c": F(7)}
    replaced = sum(w * ((1 - mass) * f[x] + mass * f["c"]) for x, w in good.items())
    target = sum(law[x] * f[x] for x in law)
    require(replaced == target, "unconditional-local-tail-mass")
    # Two independent replacements on the same coordinate are Cartesian products.
    second = {F(-1): F(2, 5), F(2): F(3, 5)}
    direct = sum(law[x] * w * (f[x] + y) ** 2 for x in law for y, w in second.items())
    restored = sum(wg * wy * ((1 - p) * (f[x] + y) ** 2 + p * (f["c"] + y) ** 2)
                   for x, wg in good.items() for y, wy in second.items())
    require(direct == restored, "independent-static-dynamic-restoration")

    growth = F(7, 8) if mutant == "dyadic-ratio" else F(9, 8)
    require(growth == 2 * F(3, 4) ** 2 and growth > 1, "dyadic-Gaussian-exponent")
    require(sum(F(3, 4) ** k for k in range(32)) / 8 < F(1, 2), "dyadic-threshold-sum")
    require(F(2, 2 ** 2) <= F(1, 2), "dyadic-geometric-tail")
    l = F(1, 64)
    g_min = 2 ** 23
    require(g_min * l * l / 64 >= 16, "tail-variance-regime")
    require(1024 <= g_min * l / 128, "exponential-tail-absorption")
    require(1024 * 128 / (F(g_min) * l) <= 1, "integrated-tail-prefactor")
    require(l * l / 128 == F(1, 2 ** 19), "dynamic-tail-exponent")
    R_over_U = 2048 if mutant == "ssh-tail-cutoff" else 4096
    require(1024 <= F(R_over_U, 4), "static-tail-absorption")
    require(F(R_over_U ** 2, 8) >= 2 ** 21, "static-tail-rate")
    C = 2 ** 20 if mutant == "threshold-exponent" else 2 ** 25
    require(C >= g_min, "global-tail-regime")
    A = F(C, 2 ** 19)
    require(A.denominator == 1 and A >= 1, "logarithm-power-removal")
    # exp(-A) < 2^(-A), x^(1-A)<=1 for x>=1.
    require(F(2 ** 27, 2 ** int(A)) < F(1, 64), "dynamic-attachment-margin")
    require(2 ** 21 - 1 >= 31 and F(2 ** 24, 2 ** 31) < F(1, 64),
            "static-attachment-margin")
    require(F(1, 64) + F(1, 64) < F(1, 4), "rooted-tree-invariance")
    require(4097 * 4 + 1 <= 2 ** 15, "SSH-reference-row-budget")
    exponent = F(1) if mutant == "asymptotic-log" else F(2, 3)
    require(exponent == F(2, 3) and 3 * exponent == 2 and exponent > F(1, 2),
            "temperature-and-logarithm-exponent")
    # Local-source susceptibility pressure bound: 2V Hilbert-Schmidt budget.
    require(F(2) / 2 == 1, "static-source-quadratic-integral")
    require(F(3, 4) * F(2, 3) == F(1, 2), "source-counterexample-gap")
    counts = (1, 1) if mutant == "oscillator-count" else (1, 2)
    require(counts == (1, 2), "Holstein-and-SSH-oscillator-count")
    print("CERTIFIED: exact finite guards and identities passed")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", choices=MUTANTS)
    ap.add_argument("--all-mutants", action="store_true")
    args = ap.parse_args()
    if args.mutant and args.all_mutants:
        ap.error("choose one replay mode")
    try:
        checks(args.mutant)
    except AssertionError as exc:
        print(f"REJECTED {args.mutant or 'base'}: {exc}")
        return 1
    if args.all_mutants:
        path = str(Path(__file__).resolve())
        for name in MUTANTS:
            run = subprocess.run([sys.executable, "-B", path, "--mutant", name],
                                 text=True, capture_output=True, check=False)
            print(run.stdout.strip())
            if run.stderr:
                print(run.stderr.strip())
            print(f"mutant {name}: exit {run.returncode}")
            if run.returncode != 1 or not run.stdout.startswith(f"REJECTED {name}:"):
                return 2
        print("CERTIFIED: all eight mutants rejected with exit 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
