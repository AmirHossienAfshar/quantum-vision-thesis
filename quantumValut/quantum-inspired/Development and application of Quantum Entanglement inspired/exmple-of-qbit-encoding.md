
## Q-bit encoding

> That matrix is the Q-bit encoding of a *single particle*.

Each **row = one dimension (one variable)**
Each **column = one Q-bit (one bit position in the binary encoding)**

Now let’s make that completely explicit and consistent with Section 2.3.1.

---

## 1. What the symbols mean in Equation (7)

You have a particle:

$$
X = [x_1, x_2, \dots, x_D]
$$

where:

* **D = number of dimensions** (decision variables)
* each (x_d) is a *real number*

After encoding, the particle becomes this matrix:

$$
\begin{bmatrix}
x_1^1 & x_1^2 & \dots & x_1^n \\
x_2^1 & x_2^2 & \dots & x_2^n \\
\vdots & \vdots & \ddots & \vdots \\
x_D^1 & x_D^2 & \dots & x_D^n
\end{bmatrix}
$$


### Meaning:

* $x_d^k \in {0,1}$
	* **Row index (d)** → dimension number
* **Column index (k)** → bit position
* **n = total number of Q-bits per dimension**

This is **exactly** Section 2.3.1:

```
n = 1 sign bit
  + (# integer bits)
  + (# fractional bits)
```

---

## 2. How this matches the sign / integer / fractional split

Let’s say:

* 1 sign bit
* 4 integer bits
* 3 fractional bits

Then:

```
n = 8
```

Each row is laid out as:

```
[ sign | integer bits | fractional bits ]
```

So column meanings are **fixed across all rows**:

| Column index | Meaning    |
| ------------ | ---------- |
| 1            | sign       |
| 2–5          | integer    |
| 6–8          | fractional |

---

## 3. Fully worked example (one particle)

### Problem

Optimize a 3-D function:

$$
f(x_1, x_2, x_3)
$$

### Particle position

$$
X = [-5.25,\ 3.75,\ -1.5]
$$

### Encoding parameters

* 1 sign bit
* 3 integer bits
* 2 fractional bits
  → **n = 6**

---

### Encode each dimension

#### (x_1 = -5.25)

```
sign = 1
integer = 101   (5)
fraction = 01   (0.25)
```

Row 1:

```
[1 1 0 1 0 1]
```

---

#### (x_2 = +3.75)

```
sign = 0
integer = 011
fraction = 11
```

Row 2:

```
[0 0 1 1 1 1]
```

---

#### (x_3 = -1.5)

```
sign = 1
integer = 001
fraction = 10
```

Row 3:

```
[1 0 0 1 1 0]
```

---

### Final Q-bit matrix for **one particle**

$$
X =
\begin{bmatrix}
1 & 1 & 0 & 1 & 0 & 1 \\
0 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 1 & 1 & 0
\end{bmatrix}
$$

That matrix is **one particle** in Q-bit space.

---

## 4. Where entanglement fits in this matrix

When they say they use $|\phi_{00}\rangle$:

* They choose **pairs of columns**
* For those columns:
  $$
  x_d^{k_1} = x_d^{k_2}
  $$

So certain column pairs are constrained to be equal.

Example:

```
fraction bit 1 ↔ fraction bit 2
```

Then each row must satisfy:

```
[ ... 0 0 ] or [ ... 1 1 ]
```

---

## 5. How local search operates on this matrix

Local search does:

1. Pick **one entry** (x_d^k)
2. Flip it (0↔1)
3. If that column is entangled → flip its partner column too
4. Decode the row back to a real number
5. Evaluate fitness
6. Keep if better

That’s why they loop over:

* **all Q-bits** (columns)
* **all dimensions** (rows)

