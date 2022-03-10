import numpy as np
import cvxpy as cvx

np.random.seed(12345)
n = 10
k = 6
mu = np.abs(np.random.randn(n, 1))
Sigma = np.random.randn(n, n)
Sigma = Sigma.T.dot(Sigma)
w = cvx.Variable(n)

ret = mu.T*w
risk = cvx.quad_form(w, Sigma)
objective = cvx.Maximize(ret - risk)

binary = cvx.Bool(n)  # !!!

constraints = [cvx.sum_entries(w) == 1, w>= 0, w - binary <= 0., cvx.sum_entries(binary) == k] # !!!

prob = cvx.Problem(objective, constraints)
prob.solve(verbose=True)

print(prob.status)

output = []
for i in range(len(w.value)):
    output.append(round(w[i].value,2))


print('Number of non-zero elements : ',sum(1 for i in output if i > 0))