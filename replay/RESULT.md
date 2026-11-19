# PROVED improvement: a two-thirds-power adiabatic upper bound

**PROVED (analytical; independent review pending).** For **both** pure spinful square-lattice Holstein and bond-SSH models, exponential decay of fixed local electronic opposite-even-charge correlations holds when `τ³≥2²⁵UΩ²[1+log(1+E/τ)]`, where `τ=k_B T`, `U=F²/K` is the **phonon relaxation/coupling energy, not an on-site Hubbard repulsion**, and `E=t` (Holstein) or `t+U` (SSH). Consequently the electronic pairing-temperature diagnostic satisfies `k_B T_pair≤τ_*∼[(2/3)2²⁵U]^(1/3)Ω^(2/3)[log(E/Ω)]^(1/3)=o(√Ω)` at fixed `t,U>0`. Here `τ_*` is the unique positive root of the stated threshold. The estimate holds grand canonically and in periodic thermodynamic canonical states at any fixed interior density, including coexistence. It improves the previous upper-bound exponent, **does not establish a physical transition asymptotic**, and **does not prove** `τ≤CΩ`. A second, source-pressure route yields a proved static quadratic-source lemma and a proved abstract obstruction to extracting susceptibility from the source-uniform additive free-energy sandwich alone. Full proofs are in [RIGOR.md](RIGOR.md); finite constants and eight mutant guards are [CERTIFIED by exact-rational replay](replay.py).

## Parent results and hypotheses: one-page summary

The exact current square-lattice theorem is the **consolidated** [released source, §§Theorems–2.4](../../../PUBLISH/adiabatic-merged/repo/RIGOR.md), not the older exponent in [ADIABATIC/RESULT.md](../RESULT.md). With two spin species, nearest-neighbor square tori, `t>0`, identical independent neutral harmonic oscillators, no extra electron interactions, `U=F²/K`, `Ω=ℏ√(K/m)`, and fixed `t,U` as `Ω→0`, its sufficient condition is

| Model | `E_j` | `L_j` | Previous sufficient clustering condition |
|---|---:|---:|---|
| Holstein, `b_x n_x`, hopping `−t` | `t` | `2²⁶` | `τ⁴≥L_jUΩ²(E_j+τ)` |
| Bond SSH, hopping `−t+b_e` | `t+U` | `2⁴⁰` | same |

The positive threshold has asymptotic `(L_j U E_j)^(1/4)√Ω+O(Ω)`. The theorem bounds periodic thermodynamic equal-time correlations of fixed finite-support electronic opposite nonzero even-charge fields, grand canonically at any real finite chemical potential and canonically at any interior limiting density `0<n<2`. Algebraic charge-two correlations, including oscillations and logarithms, define `T_pair`. It is not a positive-mass flux-curvature or whole Yang-matrix theorem and excludes order detected only by phonon-dressed fields. At the annealed static endpoint `Ω=0`, `0≤Γ≤I` and positive-temperature equilibrium electronic helicity vanishes. The older parent condition `τ⁶≥K_jUΩ²(E_j+τ)³` gave exponent `1/3`; its updated consolidation uses weighted covariance `ℓ²` and gives exponent `1/2`. The bare comparator `C_infΩ√λ_FS` remains open at fixed positive **regular bare filling**. Regularity is needed for that finite Fermi-surface comparator, not for either clustering theorem.

[LINEAR2/RIGOR.md](../LINEAR2/RIGOR.md) proves three method barriers. **B1:** Holstein dressed hopping has norm one and order-`t` kinetic energy at `n=1/2`, `0<U≤t/4`, `τ≤t/64`; its vacuum Franck–Condon factor cannot replace a diamagnetic kinetic term. An exponentially small atomic pair-transfer coefficient does not control fixed hopping, since the full complement has gap `min(U,Ω)`. Adjacent SSH bond bilinears do not commute, so simultaneous elementary shifts fail. **B2:** resonant conditional static blocks have a *signed* nonzero-mode derivative `D≥Uβ³Ω²/63375` when `βΩ≤1`, `τ≤t`, and a divergent `U/Ω` lower bound at `τ=cΩ`. Removing the zero mode alone does not make a reference-uniform first derivative small. **B3:** an auxiliary positive rooted-tree model satisfying the parent's weighted covariance bound has convergence boundary `τ∼(eUJ/6)^(1/4)√Ω`. This is sharpness of that positive estimator, not a physical lower bound.

[LINEAR3/RIGOR.md, §§6–7](../LINEAR3/RIGOR.md) proves all-positive-temperature cylinder absence results but no improved isotropic exponent. Its signed comparison is `0≤F_static−F_quantum≤Mτ log[sinh(Ω/(2τ))/(Ω/(2τ))]≤M min(Ω/2,Ω²/(24τ))`, also with any chosen subset frozen, real Peierls fields, canonical number, and bounded electronic sources. The square obstructions are **O1:** the Hermitian `cosh` complex-gauge cost still has order-`βt` coefficient at fixed regular density; it discards paramagnetic cancellation. **O2:** an extensive `Vε` pressure envelope, even signed and uniform in flux, cannot bound an `O(1)` harmonic-twist curvature; a local Ward identity kills gradients, not torus winding. **O3:** the LINEAR2 conditional-derivative and positive-tree obstructions still apply to their stated estimator classes. **O4 (missing estimate):** winding-sensitive interpolation or genuinely connected control beyond those envelopes was absent. None of these is a no-go theorem for every possible adiabatic bound.

## Complete hypotheses of the new theorem

- **Models:** Holstein and independent **bond** SSH, two equal spin species, square nearest-neighbor tori with periodic boundary conditions. No Hubbard repulsion, Coulomb term, other direct electron interaction, magnetic field, or anharmonic phonon term. Holstein density shifts can be absorbed by translating the coordinate and shifting chemical potential.
- **Scales and units:** `t>0`, `U=F²/K>0`, `Ω=ℏ√(K/m)>0`, `τ=k_B T>0`. `U` is an electron–phonon energy. `2²⁵=33,554,432` is a conservative common dimensionless constant. Every logarithm has dimensionless argument.
- **Density and filling:** grand-canonical bound uniform in real chemical potential; canonical statement in translation-invariant periodic thermodynamic limits with `N/V→n∈(0,2)`, including densities of neutral coexistence. No assumption about regular bare filling, localization, CDW order, or uniqueness. The empty/full and `U=0` free cases are separate trivial charge-correlation cases. The stated nontrivial root and asymptotic assume `U>0`.
- **Phonons and cutoffs:** the physical Gaussian laws are unbounded and **never truncated**. The proof chooses an auxiliary bounded dynamic reference `||v||∞≤τ/64`, and for SSH only an auxiliary static reference `|b_0|≤4096(t+U+τ)`. Independent exact local tail replacements restore the full original laws. Holstein static coordinates have no reference cutoff. There is no physical low-phonon-number projection and no implicit restriction `βΩ≤1`.
- **Observable and limits:** fixed finite-support electronic fields of opposite nonzero even charge. Canonical limits take volume first at fixed source and separation, then source to zero, then separation to infinity. No positive-mass finite-volume canonical clustering estimate is asserted. The result bounds the defined electronic `T_pair`, not a Drude weight, binding energy, Eliashberg eigenvalue, helicity-only transition, or order visible solely in dressed fields.

## Two attack routes and the explicit barrier-evasion map

### Route A: bounded dynamic reference plus exact rare-history expansion — successful

The new estimate keeps **typical nonzero-mode histories nonperturbatively** in a time-dependent quadratic electron reference. Their free-Gaussian amplitude is controlled by an increment-variance estimate. Only local rare histories with amplitude above `τ/64` are expanded. Their coefficient envelope is exponentially small in `g=τ³/(UΩ²)`, rather than proportional to the old `Uβ³Ω²` vertex mass. Summing spatial attachments costs `Q=O(1+βE)` and is overcome by `g≥2²⁵[1+log(1+βE)]`.

| Prior barrier/obstruction | Why Route A is outside its inference class |
|---|---|
| B1: dressing, atomic gap, and noncommuting SSH shifts | No polaron projection, vacuum overlap, atomic hopping expansion, stiffness estimate, or simultaneous bond displacement. The exact time ordering retains noncommuting SSH bonds. |
| B2: conditional nonzero-mode first derivative | No covariance Taylor expansion around a static reference. The whole bounded dynamic history is solved as a quadratic reference; only Gaussian tails are expanded. A large derivative at an individual resonant static block is not a lower bound on a rare-history coefficient. |
| B3: positive tree with old envelope | Trees remain positive **after** the new history split, but their local coefficient is `O(exp[−g/2¹⁹])`, not `O(Uβ³Ω²)`. Thus the hypothesis calibrating the parent's square-root tree scale is not the one being used. |
| O1: nonvanishing `cosh` cost | No Hermitian-flux comparison or diamagnetic replacement. |
| O2: extensive pressure versus winding, Ward identity | Direct connected charged correlations are bounded; pressure is used only for canonical transfer of a finite-range bilocal source, with a controlled linear coefficient. No flux differentiation occurs. |
| O3: reference derivatives and envelopes | Same distinctions as B2 and B3; additionally the reference Wick-minor bound handles its time dependence explicitly. |
| O4: absent new connected control | Supplied: [standalone Lemma 1](RIGOR.md#lemma-1-wick-control-for-a-bounded-time-dependent-quadratic-reference) has a `4^k` interpolated minor bound and linear weighted attachments; [standalone Lemma 2](RIGOR.md#lemma-2-exact-independent-local-tail-replacement) restores every tail exactly and provides the exponentially small vertex envelope. |

The constant proof, tree factorials, source analyticity, conditional zero-source positivity, and thermodynamic number transfer are in RIGOR §§2–5. The argument does **not** give a linear bound: at `τ=cΩ`, its control parameter is `g=c³Ω/U→0`, so typical dynamic histories are not a small perturbation on the temperature scale.

### Route B: direct pair-source pressure sandwich — partial lemma and a new barrier

Instead of winding, introduce the grand-canonical bulk source `−h Σ_x(η_x c†_(x↑)c†_(x↓)+h.c.)`, `|η_x|≤1`, including momentum phases. This route uses the full signed quantum/static sandwich and a static conditional Gaussian fermion variance estimate. It gives `0≤p_static(h)−p_static(0)≤βh²` and `0≤p_quantum(h)−p_quantum(0)≤βh²+ε`, `ε=(M/V)min(Ω/2,Ω²/(24τ))`. RIGOR §6 proves both and a source-information obstruction.

| Prior barrier/obstruction | Why Route B is outside its inference class |
|---|---|
| B1 and O1 | No hopping projection, atomic denominators, or flux/`cosh` stiffness cost. |
| B2 and O3's derivative part | The full physical trace is sandwiched; no reference-uniform perturbative first derivative is used. |
| B3 and O3's envelope part | No absolute rooted-tree or covariance row-sum criterion. |
| O2 | Bulk pair susceptibility, not an `O(1)` harmonic torus flux response, is the target. No differentiation in flux or use of the gradient Ward identity. |
| O4 | It seeks the connected, source-dependent interpolation difference, not a winding comparison. That extra estimate is **still missing**, explicitly identified below. |

**PROVED barrier within the stated source-sandwich information class:** even real-analytic, even, convex pressures with uniformly bounded slopes and `0≤p_q(h)−p_s(h)≤ε` for every `h` can have unbounded `p_q''(0)` while `p_s''(0)=1`. The explicit log-sum-exp family in RIGOR §6 proves this; it is not an electron–phonon model realization. Thus a susceptibility proof needs a **quadratic**, not merely additive, estimate on the source-dependent interpolation difference. The source route alone also needs a fixed-number treatment of the anomalous source; Route A supplies canonical conclusions independently, without such a source.

## What is new, what is known, what remains open

**New PROVED results in this slice:** the bounded time-dependent reference Wick lemma; exact local-history tail lemma with the displayed coefficient budget; the sufficient `τ³` logarithmic threshold for both models and hence the improved two-thirds-power upper bound; the static source quadratic bound with uniform phase weights; and the analytic convex-pressure counterexample to susceptibility extraction from the additive sandwich alone. The last is an information-class barrier, not a physical counterexample.

**Known/imported framework, re-derived where needed:** exact harmonic Gaussian time histories, free quadratic Wick algebra, forest identities, static fermion trace bounds, and thermodynamic canonical pressure duality. The original endpoint result, LINEAR2 barriers, and LINEAR3 pressure sandwich are not new claims here. No new third-party paper content or reference is required; all prior statements are traced to the parent proof files. No priority claim or measurement is made.

**OPEN:** `τ≤CΩ` at fixed positive regular bare filling and coupling; any strict comparison with the bare `C_infΩ√λ_FS` at such a fixed filling; sharpness of either exponent in the physical models; positive-mass helicity or whole Yang-matrix bounds on squares; and Route B's source-dependent quadratic interpolation estimate. The new rate is better than `√Ω` but still divided by `Ω` grows as `Ω^(−1/3)log^(1/3)`. No physical lower bound, ordered phase, or counterexample to a linear ceiling is established.

## Certification and exercised commands

Only the assignment's small, offline replay was executed. In this directory:

```
UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project \
  --with numpy --with scipy --with mpmath python -B replay.py --all-mutants
```

**Exit 0**, with `CERTIFIED: exact finite guards and identities passed`, followed by the eight child commands `python -B replay.py --mutant NAME` (the same UV-provisioned interpreter), each exiting **1** at its intended guard:

| Mutant | Exit | Rejected guard |
|---|---:|---|
| `weighted-cutoff` | 1 | weighted-reference-smallness |
| `wick-scale` | 1 | interpolated-minor-factor |
| `tail-mass` | 1 | unconditional-local-tail-mass |
| `ssh-tail-cutoff` | 1 | static-tail-absorption |
| `threshold-exponent` | 1 | global-tail-regime |
| `dyadic-ratio` | 1 | dyadic-Gaussian-exponent |
| `asymptotic-log` | 1 | temperature-and-logarithm-exponent |
| `oscillator-count` | 1 | Holstein-and-SSH-oscillator-count |

The certificate uses exact `fractions.Fraction`, finite determinant identities, complementary-minor counts, a finite-alphabet two-stage tail-law identity, and rational scalar budgets; exponential comparisons use the analytically proved `2<e<3` and logarithm inequalities. It does not computer-formalize continuous Gaussian histories, Wick/forest identities, the thermodynamic limit, or analytic asymptotics. These are written proofs and require independent mathematical review. The replay records each child exit code and rejects a malformed/error-only mutant result. A directory-creation command also exited 0.

**Not run:** independent review/numcheck (Main owns those), Lean analytic formalization, model simulations, plots, PDF/TeX build, repo tests/build/lint/formatters, or broader gates. No branch or commit: the assigned workspace is not a Git repository. No publication, deployment, or cloud/paid compute; spend $0. Only files created under this slice: `RESULT.md`, `RIGOR.md`, and `replay.py` (eight retained mutant modes, no throwaway files).
