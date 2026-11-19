# Replay supplement for A two-thirds-power adiabatic bound for electronic pair order

Davis Rens, SuperMatics Inc. ([ORCID](https://orcid.org/0000-0001-5839-5197)).

This repository accompanies the preprint [A two-thirds-power adiabatic bound for electronic pair order](https://doi.org/10.5281/zenodo.24372238). The replay supplement is [10.5281/zenodo.24372242](https://doi.org/10.5281/zenodo.24372242). The source repository is [two-thirds-pair-bound](https://github.com/SuperMatics-Inc/two-thirds-pair-bound). Related prior notes are [Suppression of electronic pair order for slow lattice phonons](https://doi.org/10.5281/zenodo.24366508) and [Pair density matrices and axial helicity for quantum bond phonons on cylinders](https://doi.org/10.5281/zenodo.24369897).

## Scope and evidence

The paper proves exponential clustering of fixed local electronic opposite-even-charge correlations in the spinful square-lattice Holstein and bond Su-Schrieffer-Heeger models with independent harmonic phonons, fixed hopping $t$, and no direct electron interaction above an explicit threshold proportional to $\Omega^{2/3}[\log(E/\Omega)]^{1/3}$, both grand canonically and in periodic thermodynamic canonical states at any interior density. A separate atomic-cutoff sharpness proposition limits the rare-history quadratic-reference method class only. The linear $\Omega$ ceiling remains open, and no claim is made about any material or measured transition temperature.

The replay scripts check finite algebraic identities, constants, and interval bounds by exact rational and interval arithmetic; they do not formalize the analytic or thermodynamic arguments.

| Result | Label | Evidence |
|---|---|---|
| Two-thirds-power adiabatic clustering bound for Holstein and bond SSH | PROVED | `paper/main.tex`, `replay/RIGOR.md`, and `replay/RESULT.md` |
| Finite rational identities, guards, and 8 mutation checks | CERTIFIED | `replay/replay.py --all-mutants` |
| Atomic-cutoff sharpness proposition for the method class | PROVED | `paper/main.tex` (Section 6.1, Appendix C) and `replay/linear5/SHARPNESS.md` |
| Sharpness constants, 7 interval covariance points, and 14 mutation checks | CERTIFIED | `replay/linear5/replay.py --all-mutants` |

## Contents and replay

- `paper/` contains the manuscript source and bibliography.
- `replay/` contains the exact-rational certificate and mutation checks (`replay/replay.py`), the companion proof (`replay/RIGOR.md`), and the snapshot for the sharpness proposition (`replay/linear5/`). Note that `replay/linear5/RIGOR.md` is a scope pointer only.
- `CITATION.cff` gives citation metadata. `MANIFEST.sha256` pins the released source tree.

With Python 3.12+, install `mpmath` and run both mutant-checking drivers from their respective directories:

```sh
python -m pip install mpmath==1.4.1
(cd replay && python -B replay.py --all-mutants)
(cd replay/linear5 && python -B replay.py --all-mutants)
sha256sum -c MANIFEST.sha256
```

The manuscript can be built from `paper/` with Tectonic:

```sh
tectonic --keep-logs main.tex
```

The GitHub Actions workflow verifies the source manifest, runs both replay scripts with `--all-mutants`, checks prose punctuation, and builds the manuscript with Tectonic. It uploads the resulting PDF as a workflow artifact.

## Licenses and provenance

The replay code and documentation in this repository are licensed under Apache-2.0; the preprint is distributed under CC-BY-4.0 through its Zenodo record.

AI agents generated proofs, certificates, code, and manuscript drafts and edits under D. Rens' direction and review.
