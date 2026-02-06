# MatrixMischief 😈📐

> Linear Algebra… but implemented the hard way. On purpose.

**MatrixMischief** is a from-scratch linear algebra library written in pure Python, created for those brave (or curious) enough to ask:

**“What if I didn’t use NumPy… and suffered a little for knowledge?”**

This project is educational, slightly chaotic, and mathematically responsible*.

\*Most of the time.

---

## 🧠 Why this exists

Because calling `np.linalg.solve()` is cool…  
but *knowing why it works* is cooler.

MatrixMischief is about:

- Understanding what really happens in vector and matrix operations  
- Writing linear algebra with your own two hands  
- Appreciating how much work libraries do for you  
- Developing emotional resilience while debugging matrix multiplication

---

## ✨ Current Features

### 🔢 Vectors (the friendly ones)

- Vector addition ➕  
- Vector subtraction ➖  
- Scalar multiplication ✖️  
- Dot product (a.k.a. mathematical trust fall)  
- Euclidean norm (vector length, not emotional strength)

### 🧮 Matrices (the dramatic ones)

- Matrix addition  
- Matrix multiplication (yes, the triple loop of destiny)  
- Transpose (flips tables politely)

---

## 🧪 Example Usage

### Vectors

```python
from vector import Vector

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(v1 + v2)      # Vector([5, 7, 9])
print(v1.dot(v2))   # 32
print(v1.norm())    # 3.741...