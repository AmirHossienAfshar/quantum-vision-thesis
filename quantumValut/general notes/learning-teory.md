# Learning Theory — Core Concepts (Intuition First)

Notes from reading Schuld & Killoran, *"Is Quantum Advantage the Right Goal for Quantum Machine Learning?"* (PRX Quantum, 2022). Built around the spam/not-spam example.

## The Setup, in Plain Terms

Imagine you're building a spam filter. There are two separate things going on:

- **How common is a given email, content-wise, in the real world?**
  → This is **p(x)**. It has *nothing* to do with whether an email is spam — it's just "how often does this type of email show up at all." A boring work email about a meeting: high p(x). Some random string of gibberish nobody would ever send: near-zero p(x).

- **Is a given email actually spam or not?**
  → This is **f\***, the "ground truth" rule. For any email you could imagine, f\* gives you the correct answer.

These two are independent. You could have an inbox that's 90% spam or one that's 1% spam — completely different p(x) — while the *rule* for what counts as spam (f\*) stays exactly the same in both cases.

## The Impossible Standard: True Risk

To know exactly how good your spam filter *really* is, you'd need to test it against **every email that could ever exist**, weighted by how often each one actually occurs, and check it against the *true* correct label every time.

That's obviously impossible:
- You don't have every email that could ever be written.
- You don't have a magic oracle that tells you the correct label for emails nobody has labeled.

This impossible, idealized measure of performance is called **true risk** (or expected risk). It's the "real" answer to "how good is this model," but you can never actually calculate it.

## The Practical Workaround: Empirical Risk

Since you can't test against every possible email, you do the next best thing: you test your filter against the finite batch of labeled emails you actually have (your training/test set), and use *that* average error rate as a stand-in.

This is called **empirical risk** — literally just "how many mistakes did the model make on the data I actually collected."

**The catch:** doing well on your specific batch of emails doesn't guarantee doing well on emails you haven't seen. Maybe your training set happened to have a lot of "URGENT ACT NOW" style spam, so your filter gets great at catching that — but it's never seen a sneakier kind of spam disguised as a normal newsletter, and fails badly there.

## Generalization: The Gap Between the Two

**Generalization** is basically the question: *"If my model does well on the emails I trained it on, how confident can I be that it'll also do well on new emails it's never seen?"**

- A model that gets 100% accuracy on its training emails but then fails on new ones hasn't "learned" spam detection — it's just memorized its training set.
- A model that generalizes well has picked up on genuinely useful patterns (like "links to shady payment pages" or "impersonating a bank") rather than quirks specific to its training data.

**Generalization theory** is the whole branch of research trying to answer: *how much training data do I need, and what conditions guarantee that good performance on my dataset actually reflects good performance in the real world?*

## The Deep Learning Twist

For a long time, the accepted wisdom was: if your model fits your training data *too perfectly* (zero mistakes), it's probably memorizing rather than learning — like a student who memorizes exam answers word-for-word instead of understanding the material, and then bombs a slightly reworded question.

Deep learning threw a wrench in this. It turns out some very large, complex models (think: huge neural networks with way more parameters than training examples) can fit their training data *perfectly* — zero mistakes — and *still* perform excellently on brand-new data. This contradicts the old intuition and is still not fully explained theoretically. It's an active, unresolved puzzle in machine learning research.

## Why this matters in quantum computing terms

The paper's point: even in classical machine learning, "how good is my model, really?" is a slippery, not-fully-solvable question — true risk can't be measured directly, empirical risk is just an approximation, and deep learning has upended old assumptions about what "good generalization" even looks like.

Given that the classical target is already this messy and hard to pin down, it becomes very hard to rigorously argue a *quantum* algorithm is "better" at machine learning — there's no single, well-defined problem in the way there is for something like factoring large numbers, where speedups can be cleanly proven and measured.