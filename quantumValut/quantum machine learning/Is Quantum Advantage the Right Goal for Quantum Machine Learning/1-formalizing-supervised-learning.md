
## The running example: spam filtering

Two separate things are going on when you build a spam filter:

- **How common is a given email, content-wise, in the real world?**
  → This is **p(x)**, the input distribution. Nothing to do with spam/not-spam — just "how often does this *type* of email occur at all." A normal work email: high p(x). Random gibberish nobody would send: near-zero p(x).

- **Is a given email actually spam?**
  → This is **f\***, the ground-truth rule. For any conceivable email, f\* gives the correct label.

These two are independent — an inbox could be 90% spam or 1% spam (very different p(x)) while the *rule* for what counts as spam (f\*) stays identical.

## The formal setup (Definition 1 in the paper)
- **X** — input space (all possible emails)
- **Y** — label space (spam / not-spam)
- **D** — the finite labeled dataset actually available
- **l(y, y')** — loss function measuring how wrong a prediction is

The task: find a model f̂ that minimizes the *expected loss*, integrated over the entire distribution p(x), compared against the true label f\*(x) — for every conceivable input, not just the ones you have.

## The core issue: true risk is unmeasurable
To know how good a spam filter *really* is, you'd need to test it against **every email that could ever exist**, weighted by real-world frequency, checked against a perfect oracle's labels. Both p(x) (the full real-world frequency) and f\* (the correct label for *every* possible input) are permanently inaccessible.

This idealized, uncomputable measure of performance is called **true risk** (expected risk). It's the "real" answer to "how good is this model" — but it can never actually be calculated.

> **Key takeaway:** even the textbook definition of "solving" a learning problem already contains two objects nobody can ever fully know. This is not a minor technicality — it's the reason ML theory exists at all (see next note: empirical risk & generalization).