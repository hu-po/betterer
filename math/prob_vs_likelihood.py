import torch


# Mouse weight mean of 32 std of 2.2
mice = torch.distributions.Normal(32, 2.2)
mouse = mice.sample()
print(f'mouse {mouse}')

# probability is area under fixed probability curve
# likelihood is y axis value for distribution given fixed data point
# likelihoods do not have to integrate (or sum) to 1, unlike probabilities.

mouse = 34.2
print(f'mice.cdf({mouse}) {mice.cdf(torch.tensor(mouse))}')

# classical probability - full knowledge of all outcomes and distribution (e.g. coin, dice, cards)
# frequentist probability 
# - suffiently large sample of outcomes describes underlying distribution 
# - conclusion relies on events we haven't observed (limit as n goes to infinity)
# bayesian probability 
# - subjective estimation of distribution based on current available samples
# - update a prior belief over time

# Bayes theorem
# A is hypothesis
# B is evidence
# Prior is P(A)
# Posterior is P(A|B)
# Likelihood is P(B|A)
# P(A|B) = P(A)P(B|A) / P(B)
# posterior = prior * likelihood of evidence / probability of evidence
