# Sharpness of the small-amplitude rare-history cutoff

**PROVED, analytical; independent review pending.** The two-thirds exponent is sharp for a positive rare-restriction method which requires a quadratic reference cutoff `sup|v|≤κτ` and is uniform over atomic Holstein references. This is a method-class proposition, not a physical transition-temperature bound. Its second conclusion identifies why full imaginary-time reflection positivity cannot be applied after removing the static Matsubara coordinate.

## Proposition

Fix the coupling energy `U=F²/K>0`, a dimensionless cutoff `κ>0`, and a target bad-history budget `0<p_0<1`. Let `Ω>0`, `τ=k_B T>0`, `β=1/τ`, and `a=βΩ`. The atomic spinful Holstein oscillator has Hamiltonian

```
H=Ωa†a+g(a+a†)(n−1),       g²=UΩ/2,
```

with no hopping. In its real energy-coordinate Euclidean path write

```
b_0=β^(−1)∫_0^β b(u)du,       v(u)=b(u)−b_0.
```

The exact **interacting** law of `v`, grand canonically or in any number sector, is the centered continuous periodic Gaussian with covariance

```
D_Ω(s)= (UΩ/2) cosh[Ω(β/2−d(s,0))]/sinh(a/2)−U/β,    (S1)
```

where `d` is circle distance in `[0,β/2]`. Define the event class

```
B_r={sup_(0≤u≤β)|v(u)|>r},
E_r={|b(β/4)−b(0)|>2r}.
```

The whole-history event satisfies `E_r⊆B_r`. The local increment event `E_r` is measurable on the first half of the **full** `b` path and is therefore an admissible full-path reflection event. The event defined by a point value of the projected field `v` need not be such an event.

Put `Q=τ³/(UΩ²)`. Both `A_r=B_r` and `A_r=E_r` satisfy the upper bound

```
P(A_(κτ))≤min{1,3exp(−κ²Q/4)}.                       (S2)
```

They also satisfy the following lower bounds, interpreted trivially when the right side is negative:

```
P(A_(κτ))≥1−2κsqrt(128/21)sqrt(Q)       if 0<a≤1,     (S3)
P(A_(κτ))≥1−2κsqrt(35/3)τ/sqrt(UΩ)     if a≥1.       (S4)
```

Consequently the threshold for achieving any fixed budget `p_0` is of order `(UΩ²)^(1/3)`. More explicitly, for all sufficiently small Ω at fixed U, a necessary condition for `P(A_(κτ))≤p_0` is

```
Q≥21(1−p_0)²/(512κ²),                                (S5)
```

whereas

```
Q≥(4/κ²)log(3/p_0)                                   (S6)
```

is sufficient. These bounds establish the exact exponent, not an optimal numerical quantile constant. For example, at `κ=1`, `p_0=1/2`, the necessary constant is `Q≥21/2048`, and the simple sufficient value `Q=8` works.

The projected Gaussian law itself is **not reflection positive**. With time reflection `θu=β−u`,

```
E[v(β/4)v(3β/4)]
 =D_Ω(β/2)
 =Uτ[a/(2sinh(a/2))−1]<0                              (S7)
```

for every `a>0`. There is also a bounded half-path test on the projected path space with a strictly negative reflected quadratic form.

### Exact method-class consequence

Consider a method with all three hypotheses:

1. Every accepted quadratic reference obeys `βsup|v|≤κ`, with κ fixed independently of Ω. Its positive discarded-history activity dominates `P(B_(κτ))`, or dominates the local increment restriction `P(E_(κτ))` necessary for that cutoff.
2. Reflection/chessboard or Gaussian domination is used to bound that **positive** activity. No cancellation of signed connected insertion determinants is used to compensate it.
3. The bound is uniform over the auxiliary electronic references, including the atomic Holstein reference above. This is a reference-uniformity hypothesis, not a replacement of a fixed-positive-hopping square lattice by atoms.

Then the method cannot obtain a fixed small discarded-history budget at `τ=O(Ω)`, or at `τ=Ω` times any fixed power of a logarithm. Its sharp cutoff-probability exponent is `2/3`, by (S2)–(S6). A chessboard bound cannot improve this exponent without dropping at least one hypothesis. Moreover, chessboarding the zero-mode-conditioned Gaussian by full-path reflection positivity is invalid independently of its quantitative cost, by (S7).

## Proof

### 1. The interacting atomic dynamic law

The harmonic action in energy coordinates is

```
(1/(2U))∫_0^β [b(u)²+Ω^(−2)b'(u)²]du.
```

The free covariance solves `(-∂²+Ω²)C=UΩ²δ_periodic` with periodicity and derivative jump `−UΩ²` at zero. Solving on either side of zero gives the cosh term in (S1). Its Fourier coefficients are `UΩ²/[β(ω_n²+Ω²)]`, `ω_n=2πn/β`. The constant coefficient has variance `U/β` and is independent of all other Gaussian coefficients. Subtracting it gives (S1).

In the interacting atom the electronic occupation is conserved. Its contribution in sector `n` is `exp[−(n−1)∫b]`, times the fugacity and spin multiplicity. It depends only on `b_0`. Thus the nonzero Matsubara coefficients retain exactly the free Gaussian law after conditioning or summing over electron sectors and static coordinates. The same factorization holds on an atomic lattice under a constraint on the total particle number. There is no free-versus-interacting rarity assumption in the proposition.

### 2. Negative reflected covariance after projection

Reflection of the projected half-path linear functional `f(v)=v(β/4)` gives `Θf=v(3β/4)`. Its reflected expectation is (S7). Since `sinh x>x` for `x>0`, the bracket is strictly negative. To obtain a bounded counterexample use `f_R=max(−R,min(R,f))`. The truncations converge to `f` in Gaussian `L²`; Cauchy–Schwarz then gives convergence of their reflected products to the negative value (S7). A sufficiently large finite R is therefore a bounded counterexample.

This does not contradict reflection positivity of the full coupled oscillator-electron functional. In that functional `v(β/4)=b(β/4)−β^(−1)∫b` depends on the second half through the period average. It is not a half-path observable. Conditioning on the period average imposes a global constraint and invalidates the independent-half-bridge factorization. For reference, the small-a expansion is `D_Ω(β/2)=−UΩ²/(24τ)+O(UΩ⁴/τ³)`.

### 3. A local Gaussian increment gives the lower bounds

Let `Δ=b(β/4)−b(0)`. Its constant mode cancels, and by (S1) its variance is

```
σ²=UΩH(a),
H(a)=[cosh(a/2)−cosh(a/4)]/sinh(a/2)
    =(1−exp(−a/4))(1−exp(−3a/4))/(1−exp(−a)).        (S8)
```

It is centered Gaussian under the exact interacting atom. The following elementary bounds hold:

```
21a/128≤H(a)≤3a/14       for 0<a≤1,
H(a)≥3/35               for a≥1.                     (S9)
```

For the first line the cosh difference has positive Taylor coefficients and is at least `3a²/32`. For `0≤x≤1/2`, `(2n)!≥2^n` implies `cosh x≤1/(1−x²/2)≤8/7`. Integrating `sinh x≤x cosh(1/2)` between `a/4` and `a/2` bounds the numerator above by `3a²/28`. The denominator lies between `a/2` and `4a/7`. Taking ratios gives `21a/128` and `3a/14`. For the second line use the product form of H, its denominator at most one, and `1−exp(−x)≥x/(1+x)`: at `a≥1` its numerator is at least `(1/5)(3/7)=3/35`.

The Gaussian density at its maximum is `1/(sqrt(2π)σ)`, so

```
P(|Δ|≤2r)≤4r/(sqrt(2π)σ)≤2r/σ.
```

Using `r=κτ` and (S9) proves (S3)–(S4) for `E_r`; its containment in `B_r` proves the same lower bounds for `B_r`. In particular both bad-event probabilities tend to one whenever `τ=o((UΩ²)^(1/3))`: use Q→0 for `a≤1`, and `τ≤Ω` for `a≥1`.

Solving (S3) for a budget `p_0` gives (S5) in the `a≤1` branch. The `a≥1` branch contains no lower-temperature exception for sufficiently small Ω: (S4) tends uniformly to one there. This proves the necessary part of the threshold statement.

### 4. A Brownian-bridge domination gives the upper bound

Let `v_*` be a mean-zero periodic massless Gaussian with Fourier variances `UΩ²/(βω_n²)`, `n≠0`. These exceed the coefficients of (S1). Couple `v_*=v+z` with z independent centered Gaussian and the difference coefficients. Its Fourier standard deviations are summable, of order `n^(−2)`, so z is continuous by almost-sure absolute uniform convergence. Conditional Jensen for the convex functional `exp(λ||w||_∞²)` gives

```
Eexp(λ||v||_∞²)≤Eexp(λ||v_*||_∞²).
```

If B is a standard Brownian bridge on `[0,β]`, then

```
v_*=sqrt(U)Ω[B−β^(−1)∫B],
||v_*||_∞≤2sqrt(U)Ω||B||_∞.
```

To check the representation, double-center `min(u,w)−uw/β`. The covariance becomes `β/12−d/2+d²/(2β)`, with nonzero Fourier coefficients `1/(βω_n²)`. This is exactly the required covariance.

The one-sided bridge maximum has probability `P(sup B≥x)=exp(−2x²/β)`. Reflect a Brownian-motion path at its first crossing of level x. Such paths ending at zero correspond to paths ending at `2x`. The ratio of Gaussian transition densities at `2x` and zero, followed by conditioning the endpoint through a shrinking interval, is `exp[−(2x)²/(2β)]`. Symmetry and a union bound imply `P(||B||_∞≥x)≤2exp(−2x²/β)`.

Put `A=UΩ²β`. Hence `P(||v_*||_∞²>t)≤2exp[−t/(2A)]`. At `λ=1/(4A)`, tail integration gives

```
Eexp(||v_*||_∞²/(4A))
 ≤1+2(1/(4A))/(1/(2A)−1/(4A))=3.
```

Jensen transfers this moment bound to v. Markov's inequality proves `P(B_r)≤3exp[−r²/(4A)]`, which is (S2). Containment gives the bound for `E_r`. Solving this bound gives (S6). For the example `Q=8`, the finite exponential sum `exp(2)>1+2+2+8/6=19/3` gives `3exp(−2)<9/19<1/2`.

### 5. What a slab chessboard estimate can and cannot do

At `τ=Ω/a` with fixed `a>0`, the same local density bound gives

```
P(E_(κτ))≥1−[2κ/(a sqrt(H(a)))]sqrt(Ω/U)→1.          (S10)
```

More generally consider finitely many nontrivial increments within reflected slabs of width proportional to `1/Ω`. At fixed a each variance is `UΩH_j(a)` with `H_j(a)>0`. Their small-increment probabilities are at most `[2κ/(a sqrt(H_j(a)))]sqrt(Ω/U)`. The union bound shows that the probability of their simultaneous bad restrictions is at least

```
1−[Σ_j 2κ/(a sqrt(H_j(a)))]sqrt(Ω/U)→1.
```

No independence assumption enters. Thus an Ω-independent cost `exp(−c×number of slabs)` cannot hold for this event class at the small reference cutoff; inserting the fixed factor `βΩ=a` does not change the contradiction. Under any valid chessboard comparison `P(E)≤P(E_repeated)^(1/m)`, the repeated-restriction root must also tend to one. At the two-thirds threshold, `βΩ→0`, so the entire thermal circle is actually shorter than one slab of width `1/Ω`.

## Scope and exclusions

This proposition establishes the sharp **cutoff-probability exponent** for the three stated method hypotheses. It does not independently validate LINEAR4's interacting forest expansion, prove a transition at this scale, or establish sharpness of a physical upper bound.

It does **not** rule out:

- unrestricted mirrored references with natural temporal amplitude `sqrt(UΩ)` at fixed `βΩ`, which need not satisfy the small perturbative cutoff;
- reference refreshing with a non-pointwise temporal transport estimate;
- integrated determinant/minor estimates retaining cancellations or compensating electronic weights;
- an order-Ω connected lattice source-interpolation estimate;
- a linear or Ω-times-log ceiling for fixed `t>0` square-lattice physics at positive regular density.

The atom is an exact interacting auxiliary reference, not a physical counterexample to the fixed-positive-hopping conjecture. A method designed only for uniformly hopping-positive references, and proved without atomic-reference uniformity, is outside the proposition. No new third-party paper content is used; the covariance, atomic factorization and Gaussian bounds are derived above.

## Replay scope

The retained script is [replay.py](replay.py). The prescribed command is

```
UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with numpy --with scipy --with mpmath python -B replay.py --all-mutants
```

Its sharpness extension certifies the exact rational constants `3/16`, `21/128`, `3/14`, `3/35`, `1/24`, `3`, `21/2048`, the finite sufficient-Q check, the atomic zero-integral identity and the threshold exponent. It also uses outward interval arithmetic at seven exact values of a to check the covariance sign and variance inequalities. The all-a inequalities, reflection counterexample, Gaussian-process domination and atomic path factorization are proved analytically above, not certified by finitely many interval points.

New retained mutant modes are `increment-factor`, `brownian-centering`, `threshold-power`, `atomic-dynamic-tilt` and `projected-RP`, in addition to the nine earlier LINEAR5 modes. Independent review remains required before release.

## Observed replay evidence

The command above was executed from `ADIABATIC/LINEAR5/` and exited **0**, with reported wall time **1.56 seconds**. All fourteen child mutant commands `python -B replay.py --mutant NAME` exited **1**, at their intended guards. The five new modes were rejected at `quarter-period-increment-factor`, `Brownian-bridge-centering-loss`, `two-thirds-cutoff-threshold-exponent`, `atomic-nonzero-mode-factorization` and `negative-projected-reflected-covariance`, respectively. The seven interval points were `a=1/16,1/8,1/2,1,2,4,16`, at 60 decimal digits. No other tests, Lean checks or TeX builds were run. Laptop only, offline; spend $0.
