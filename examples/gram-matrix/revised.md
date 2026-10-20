For a linear kernel, the Gram matrix records pairwise inner products between feature vectors. Let \(X\in\mathbb{R}^{m\times d}\) contain these vectors as its rows, and define \(K=XX^\top\).

**Corrected proposition.** The Gram matrix \(K\) is positive semidefinite. It is positive definite and invertible exactly when the rows of \(X\) are linearly independent.

The quadratic form gives the condition for strict positivity:
\[
a^\top K a=\lVert X^\top a\rVert^2\geq 0,
\qquad a\in\mathbb{R}^m.
\]
The inequality is strict for every nonzero \(a\) exactly when \(X^\top a=0\) has only the zero solution. This requires \(\operatorname{rank}(X)=m\), so \(m\leq d\). The identity also shows that \(K\) and \(X^\top\) have the same nullspace, giving \(\operatorname{rank}(K)=\operatorname{rank}(X)\).

Distinct nonzero rows can still be linearly dependent. For example,
\[
X=\begin{pmatrix}1&0\\2&0\end{pmatrix},
\qquad
K=\begin{pmatrix}1&2\\2&4\end{pmatrix}.
\]
For \(a=(2,-1)^\top\), we have \(X^\top a=0\) and \(Ka=0\). These distinct nonzero feature vectors therefore give a singular kernel matrix. More generally, dependent feature vectors prevent a unique solution to a kernel system \(Kc=y\). Depending on \(y\), the system has no solution or multiple solutions.

**Scientific changes.** The draft claimed that distinct nonzero rows guarantee strict positive definiteness and invertibility. I corrected this to linear independence of the rows. The quadratic-form identity proves positive semidefiniteness, and the nullspace argument gives the exact invertibility condition. I checked the counterexample with exact integer arithmetic: \(X^\top a=0\), \(a^\top Ka=0\), and \(\det K=0\).

I removed the unsupported novelty and performance claims. The draft reports checks on two random matrices, but supplies neither matrix nor its results. Those checks remain unverified and cannot establish the universal claim.
