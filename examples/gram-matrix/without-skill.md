## Research passage

Let \(X\in\mathbb{R}^{m\times d}\) contain one sample encoding per row. Its Gram matrix \(K=XX^{\mathsf T}\) records the inner products between encodings. The matrix is symmetric and positive semidefinite because, for every \(a\in\mathbb{R}^{m}\),
\[
a^{\mathsf T}Ka=\lVert X^{\mathsf T}a\rVert_2^2\geq 0.
\]
Thus the inner products define a valid positive semidefinite kernel on the supplied encodings.

**Corrected invertibility condition.** The matrix \(K\) is strictly positive definite, and hence invertible, exactly when the rows of \(X\) are linearly independent. Equivalently, \(\operatorname{rank}(X)=m\), which requires \(m\leq d\). Indeed, the quadratic form vanishes exactly when \(X^{\mathsf T}a=0\). A nonzero vector \(a\) with this property expresses a linear dependence among the row encodings.

Distinct nonzero encodings can still be dependent. For example,
\[
X=\begin{pmatrix}1&0\\2&0\end{pmatrix},
\qquad
K=\begin{pmatrix}1&2\\2&4\end{pmatrix}
\]
has distinct nonzero rows, but \(K(2,-1)^{\mathsf T}=0\). Dependent row encodings therefore produce a singular Gram matrix. In that case, a linear system with coefficient matrix \(K\) cannot have a unique solution.

## Scientific changes

- **Correction:** Replaced the strict-positivity claim with positive semidefiniteness. Derived the exact condition for invertibility from the null space of \(X^{\mathsf T}\).
- Added a counterexample to the claim that distinct nonzero encodings ensure invertibility. The condition concerns dependence among row encodings. Dependent feature columns alone need not make \(K\) singular if \(X\) retains full row rank.
- Removed claims of robustness, scalability, and eliminated degeneracy. The supplied material provides no performance evidence. The draft reports two random checks without their inputs or results; those checks cannot establish the general claim.
