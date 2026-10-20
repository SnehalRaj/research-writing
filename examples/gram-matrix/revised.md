## Research passage

A Gram matrix defines a positive semidefinite kernel for any collection of real vector encodings. Let \(X\in\mathbb{R}^{m\times d}\) contain the encodings as rows, and set \(K=XX^\top\). The matrix \(K\) is symmetric. Its quadratic form shows why it is positive semidefinite: for every \(a\in\mathbb{R}^m\),

\[
a^\top K a
=a^\top XX^\top a
=\lVert X^\top a\rVert_2^2
\geq 0.
\]

The inequality is strict for every nonzero \(a\) exactly when the rows of \(X\) are linearly independent. Under this condition, \(K\) is positive definite and invertible. This requires \(m\leq d\), together with full row rank.

If the row encodings are linearly dependent, some nonzero \(a\) satisfies \(X^\top a=0\), which also gives \(Ka=0\). The resulting Gram matrix is singular. This always occurs when \(m>d\). Distinct, nonzero encodings can still be linearly dependent, so those conditions alone do not ensure invertibility.

## Scientific changes and checks

- **Correction:** The draft claimed strict positive definiteness for distinct, nonzero rows. I replaced this assumption with linear independence of the rows. The original proof's strict inequality fails whenever a nonzero vector lies in the null space of \(X^\top\).
- **Exact counterexample:** Take \(X=(1,2)^\top\), whose two rows are distinct and nonzero. Then
  \[
  K=\begin{pmatrix}1&2\\2&4\end{pmatrix},
  \qquad a=\begin{pmatrix}2\\-1\end{pmatrix},
  \qquad Ka=0,
  \qquad a^\top Ka=0.
  \]
  I verified these products with integer arithmetic. No numerical tolerance is needed.
- **Preserved result:** Every real Gram matrix is positive semidefinite. Full row rank gives the exact condition for invertibility. A dependence among the encodings produces a zero eigenvalue.
- **Evidence limits:** The draft reports two random checks but supplies neither the matrices nor their outputs. These reported checks cannot establish the unrestricted theorem. I removed the unsupported novelty, scalability and degeneracy claims.

The source fidelity, mathematics, argument and exposition pass the review. I checked the Markdown and equations in source; rendered presentation remains unchecked. Author acceptance is pending.
