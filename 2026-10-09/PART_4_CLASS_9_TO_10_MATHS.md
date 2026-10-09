# 📖 BPSC TRE 4.0 — Part IV: Class 9 to 10 Secondary Mathematics (English Edition)
**Total Subject Marks:** 80 Marks  
**Standard:** NCERT & SCERT Class 9–10 Core Standards + Higher Secondary Analytical Depth

---

## 🔢 Chapter 1: Real Numbers

### 1. Euclid's Division Lemma
For any two given positive integers $a$ and $b$, there exist unique non-negative integers $q$ (quotient) and $r$ (remainder) satisfying:
$$a = bq + r, \quad \text{where } 0 \le r < b$$

- **Iterative Application for HCF:**
  - Repeatedly apply the lemma to divisor $b$ and remainder $r$ until $r = 0$. The divisor at the step where remainder becomes zero is the $\text{HCF}(a, b)$.
- **Integer Forms:**
  - Every positive even integer is of the form $2q$.
  - Every positive odd integer is of the form $2q + 1$ (or $4q+1, 4q+3$, or $6q+1, 6q+3, 6q+5$).

### 2. Fundamental Theorem of Arithmetic
> Every composite number can be uniquely expressed (factorized) as a product of prime powers, apart from the order in which the prime factors occur.

- **Fundamental Identity for Two Numbers:**
  $$\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b$$
  *(Caution: This relationship does not hold directly for three or more numbers!)*

### 3. Irrationality of Radicals & Real Axioms
- If $p$ is a prime number and $p$ divides $a^2$, then $p$ divides $a$ (where $a$ is a positive integer).
- **Core Irrational Numbers:** $\sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{p}$ are irrational.
- **Algebraic Properties:**
  - Sum or difference of a non-zero rational number $r$ and an irrational number $s$ ($r \pm s$) is always **irrational**.
  - Product or quotient of a non-zero rational number $r$ and an irrational number $s$ ($r \cdot s$, $r/s$) is always **irrational**.
  - Sum, difference, product, or quotient of two irrational numbers may be rational OR irrational.

### 4. Decimal Expansion Criteria
Let $x = \frac{p}{q}$ be a rational number in simplest form ($\gcd(p, q) = 1$).
1. **Terminating Decimal:** $x$ has a terminating decimal expansion if and only if the prime factorization of denominator $q$ is strictly of the form:
   $$q = 2^n \cdot 5^m, \quad \text{where } n, m \text{ are non-negative integers.}$$
   - The decimal terminates after exactly $\max(n, m)$ decimal places.
2. **Non-terminating Repeating Decimal:** If prime factors of $q$ contain any prime other than $2$ or $5$ (e.g., $3, 7, 11$), the decimal expansion is non-terminating and periodic.

---

## 📈 Chapter 2: Polynomials & Parabolic Algebra

### 1. Degree and Geometrical Representation
- For $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ ($a_n \neq 0$), degree is $n$.
- **Geometrical Meaning of Zeroes:** The number of real zeroes of $P(x)$ equals the exact number of times the Cartesian curve $y = P(x)$ intersects the $X$-axis.
  - Linear ($ax + b$): Exactly 1 zero (straight line).
  - Quadratic ($ax^2 + bx + c$): Parabola with at most 2 real zeroes. Opens upward ($U$-shape) if $a > 0$; opens downward ($\cap$-shape) if $a < 0$.
  - Cubic ($ax^3 + bx^2 + cx + d$): At most 3 real zeroes.

### 2. Relationships Between Zeroes and Coefficients

#### (A) Quadratic Polynomial: $P(x) = ax^2 + bx + c$ ($a \neq 0$)
Let $\alpha$ and $\beta$ be the zeroes:
1. **Sum of zeroes:**
   $$\alpha + \beta = -\frac{b}{a}$$
2. **Product of zeroes:**
   $$\alpha \beta = \frac{c}{a}$$
3. **Sum of Reciprocals Identity:**
   $$\frac{1}{\alpha} + \frac{1}{\beta} = \frac{\alpha + \beta}{\alpha \beta} = \frac{-b/a}{c/a} = -\frac{b}{c}$$
4. **Reconstructing Polynomial from Zeroes:**
   $$P(x) = k \cdot [x^2 - (\alpha + \beta)x + \alpha \beta]$$

#### (B) Cubic Polynomial: $P(x) = ax^3 + bx^2 + cx + d$ ($a \neq 0$)
Let $\alpha, \beta, \gamma$ be the zeroes:
1. **Sum of zeroes:** $\alpha + \beta + \gamma = -\frac{b}{a}$
2. **Sum of pairwise products:** $\alpha \beta + \beta \gamma + \gamma \alpha = \frac{c}{a}$
3. **Product of zeroes:** $\alpha \beta \gamma = -\frac{d}{a}$
4. **Special Case:** If one zero is $0$ (say $\gamma = 0$), then $\alpha \beta + 0 + 0 = \frac{c}{a} \implies \text{Product of the other two zeroes} = \frac{c}{a}$.

---

## ⚡ Chapter 3: Discriminant Analysis ($D = b^2 - 4ac$)

| Discriminant Value | Nature of Roots | Parabola X-axis Intersections |
|:---|:---|:---|
| $D > 0$ (Perfect Square) | Two distinct, rational roots | Intersects at 2 distinct rational points |
| $D > 0$ (Not Perfect Square) | Two distinct, irrational conjugate roots ($p \pm \sqrt{q}$) | Intersects at 2 irrational points |
| $D = 0$ | Two equal, real roots ($x = -b / 2a$) | Touches the X-axis at exactly 1 vertex point |
| $D < 0$ | No real roots (Complex conjugate roots) | Does not touch or intersect the X-axis at all |
