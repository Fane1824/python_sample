import matplotlib.pyplot as plt
from q1_b import pi_errors_pseudo, pi_errors_random, k

plt.figure(figsize=(10, 6))
plt.plot(range(1, k + 1), pi_errors_pseudo, label='Pseudo-Random Number Generator')
plt.plot(range(1, k + 1), pi_errors_random, label='random.random()')
plt.xlabel('Iterations')
plt.ylabel('Error in Estimation of Pi')
plt.title('Estimated Error in Estimation of Pi using Monte Carlo Method')
plt.legend()
plt.grid(True)
plt.show()