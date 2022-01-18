"""

From https://www.youtube.com/watch?v=O-2l2Dy4XJM

Q: If you sample 10k users multiple times what would the distribution of false positives look like?
A: (a) Exponential (b) Normal (c) Binomial (d) None of the above

What does "false positive" mean? When the model predicts true, when it is actually false.
Use of word "positives" means  there are two possible values: true and false. This rules out (b) since a Normal distribution is for continuous variables
What is the "distribution of false positives?" P(FP)? P(yp=P|x,yt=N)?
Discrete probability distribution, since there are only 2 possible values so answer is (C) Binomial.

"""
