# Reason 3: Average/Worst-Case Claims Over Huge Model Families

## The pattern
Some papers make claims about *entire enormous families* of quantum models at once rather than one specific model — e.g., "all models of the form f(x) = tr{ρ(x)M}" (any quantum model measuring observable M on a data-encoded state), or "all circuits sampled randomly according to the Haar measure" (a totally random circuit drawn from the space of all possible circuits).

**Example — barren plateaus:** a well-known result [McClean et al., ref 56] proves that, *on average*, across this huge family of random circuits, gradients vanish exponentially as circuits grow — making training exponentially hard. This gets widely cited as bad news for quantum ML broadly.

## The authors' objection
Proving something about the *average* behavior of an enormous, mostly-random family tells you almost nothing about whether a *specific, carefully designed* model within that family behaves completely differently.

**Analogy:** you could just as easily prove that "the average classical algorithm" has certain limitations — but that says nothing useful about a specific, well-engineered algorithm like boosting or GANs, which behave in atypically good ways compared to a "random" algorithm from the same broad family.

## The takeaway
Broad average/worst-case statements over huge, mostly-arbitrary sets of models risk being treated as conclusive about quantum ML's potential — when they might just describe the unremarkable "typical" member of an enormous haystack, while a good specific quantum model (the "needle") could behave completely differently and remain undiscovered.