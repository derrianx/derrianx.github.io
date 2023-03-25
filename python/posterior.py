# Define observed data
# import libs
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = ['H', 'T', 'T', 'H', 'T', 'H', 'T','H','T','H', 'T','T','T','T','T','T','T','T','T','T']
num_heads = data.count('H')
num_tails = len(data) - num_heads

# Define prior distribution
prior_alpha = 1
prior_beta = 1
prior = np.random.beta(prior_alpha, prior_beta, size=1000)

# Define likelihood function
likelihood = np.random.binomial(n=1, p=prior[0], size=(1000, len(data)))
likelihood_heads = np.sum(likelihood, axis=1)
likelihood_tails = len(data) - likelihood_heads

# Calculate posterior distribution
posterior_alpha = prior_alpha + num_heads
posterior_beta = prior_beta + num_tails
posterior = np.random.beta(posterior_alpha, posterior_beta, size=1000)

# Plot posterior distribution
sns.kdeplot(posterior)
plt.savefig('posterior.png')
