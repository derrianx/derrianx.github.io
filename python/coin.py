# Description: Coin flip simulator
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# generate a array of coin flip results
array = np.array(['H', 'T', 'T', 'H', 'T', 'H', 'T','H','T','H', 'T','T','T','T','T','T','T','T','T','T'])

# write a python function that uses bayes theorem to estimate the probability of hettings heads or tails
def bayes(array):
    # count the number of heads and tails in the array
    heads = array.count('H')
    tails = array.count('T')
    # calculate the probability of heads and tails
    prob_heads = heads / len(array)
    prob_tails = tails / len(array)
    # calculate the probability of heads given tails and tails given heads
    prob_heads_given_tails = prob_heads / prob_tails
    prob_tails_given_heads = prob_tails / prob_heads
    # return the probability of heads and tails
    return prob_heads, prob_tails, prob_heads_given_tails, prob_tails_given_heads




# print the probability of heads and tails

# use a seaborn countplot to visualize the results
sns.histplot(array, stat="probability", discrete=True)
# is an error but it works when save the png
# display the plot

plt.savefig('coin.png')
