# Section III Verdict: "Still Wide Open," and the Quantum-Data Pivot

## The verdict
After laying out all four problems (artificial structuring, data-loading assumptions, average-case over-generalization, shaky small-scale benchmarks), the authors conclude: whether quantum computers can meaningfully help practical ML is **"still wide open"** and **"unlikely to be decided by theoretical proofs or small-scale experiments."** Not leaning positive or negative — genuinely undecidable with current tools. These tools should be seen as ways to build understanding and test hypotheses, not settle the big question.

## The sociological observation
The authors note a mood of **resignation** among colleagues/students as QML fails to produce quick commercial wins. The common response: give up on applying quantum computers to *classical* data (spam, images) entirely, and pivot to studying **"quantum data"** instead — data that is itself inherently quantum (e.g., output of a quantum experiment), where quantum computers have a more natural, undisputed edge.

## The authors' subtle jab
They question *why* the field is making this pivot: is "quantum data" genuinely the most promising direction for real applications — or simply the direction where existing proof techniques *happen to already work well*? This is a direct callback to the publication-bias theme (note 3) — even the field's strategic response to uncertainty might be shaped by what's provable/publishable, not by what's actually most useful.

## Wrap-up of Sections I–III
The throughline across these notes:
1. Learning theory's core evaluation metric (true risk) is fundamentally unmeasurable, and classical theory is still being rebuilt to explain deep learning (notes 1–2).
2. QML claims of "beating" classical ML use inconsistent metrics and suffer from positive publication bias (note 3).
3. The strongest rigorous proofs only work on artificially reverse-engineered problems, with no general framework to extend them to real data (note 4).
4. Even the "traditional approach" speedups rely on data-loading assumptions (QRAM) that remain practically unsolved (note 5).
5. Broad average/worst-case theoretical claims over huge model families may not reflect what specific, well-designed models can do (note 6).
6. Small-scale empirical benchmarks suffer from reproducibility and scaling-unknown issues (note 7).
7. The overall conclusion: the question is structurally undecidable with current tools — and even the field's pivot toward "quantum data" may be driven by convenience rather than genuine promise (this note).

*(Section IV — the paper's constructive counter-proposal of advantage-agnostic research directions — not covered in this note sequence.)*