import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Define parameters of beta distribution for prior
alpha_prior = 1
beta_prior = 1

# Generate sample from prior distribution
prior_samples = beta.rvs(alpha_prior, beta_prior, size=1000)

# Plot prior distribution
fig, ax = plt.subplots()
ax.hist(prior_samples, density=True, bins=30, alpha=0.5)
ax.set_xlabel('Probability of heads')
ax.set_ylabel('Probability density')
ax.set_title('Prior distribution')
plt.show()
plt.savefig('prior.png')
