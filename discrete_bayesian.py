"""
Misc. Notes-

Bayesian statistics treats probablity as a belief about a single event, it can
also be thought of as a measure of a strength of our knowledge.

Bayesian statistics also takes past inforamtion into account.
^^^This past information is usually referred to as the "prior"

The "posterior probablity distribution" aka "posterior" is a probability distribution
after incorporation the measurement information.

posterior = (likelihood * prior) / normalization
    
    where likelihood tells us how likely each position is given the measurement 
    (it is not a PDF because it doesn't sum to 1)
    
    also, normalization here means a factor which scales the values to they sum to 1.
    remember, BOTH the prior and posterior are probability distributions (and hence sum to 1)

Some lingo-

- the system behavior is modeled with the process model. The error in the model is called system
error or process error.

"""
