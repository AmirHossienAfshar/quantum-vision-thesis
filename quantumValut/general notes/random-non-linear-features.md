# Random non-linear features

**Core idea:** you don't always need to *learn* useful features. Passing
data through a **fixed, random, non-linear transformation** often already
produces a representation that's more useful for a downstream task (e.g.
classification) than the raw input — with zero training on that
transformation.

## Why it works (intuition)

A random non-linear projection typically:
- **increases dimensionality**, spreading data into a higher-dimensional
  space
- **makes patterns more linearly separable** — classic kernel-methods
  result: complex non-linear boundaries in the original space can look
  like simple straight lines after a non-linear projection into higher
  dimensions
- gives diverse "views" of the data, similar to how ensembling helps even
  without any single feature being finely tuned

So instead of spending compute *optimizing* a transformation, you fix a
random one — cheap, and often surprisingly close to as good.

## Classic examples

### Random convolutional filters
Normally a CNN *learns* its filters via backprop. But research (Jarrett et
al., Ranzato et al., Saxe et al.) showed **untrained, randomly initialized
conv filters** already produce decent features — part of a CNN's power
comes from the architecture itself (local receptive field + convolution +
pooling), not purely the learned weights.

### Echo State Networks (reservoir computing)
- Recurrent hidden layer ("the reservoir") has **fixed random weights**,
  never trained
- Only the final linear readout layer is trained
- The random recurrent reservoir "echoes" a time series through complex
  non-linear dynamics; by the time it reaches the readout, temporal
  patterns are linearly separable enough for a simple linear layer to
  handle

## The generalized pattern

```
raw input -> fixed random non-linear transform -> (only train this simple part) -> output
```

Skip training the expensive/early part, keep only the cheap/late part
trainable. A recurring "free lunch" trick across several corners of ML.

## Where this shows up in my QML reading

Used as the explicit motivating analogy in Henderson et al.'s
quanvolutional neural networks paper: the claim is that a **fixed, random
quantum circuit** could serve the same role as a random conv filter / ESN
reservoir — except potentially reaching a richer class of non-linear
functions than a classical random transform can, via entanglement.

Full paper notes → [[../Quantum Machine Learning/Quanvolutional Neural Networks/0-about-paper|Quanvolutional Neural Networks (Henderson et al.)]]

## Open question worth remembering

"Richer/harder to classically simulate" is not automatically the same
claim as "better for machine learning." The paper's whole empirical
section is really testing whether those two things happen to coincide —
worth staying skeptical of by default, not assuming.
