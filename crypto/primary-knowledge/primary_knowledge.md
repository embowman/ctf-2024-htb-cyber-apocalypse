## Primary Knowledge

This is a weak RSA problem. So I asked an AI for the steps to get a decryption key,
and the following is what I received:

```
1. Key Generation:
- Choose two large prime numbers, p and q
- Calculate phi(n) = (p-1) * (q-1) (Euler's totient function)
- Choose a public exponent, e, such that 1 < e < phi(n) and e is coprime to phi(n)
- Calculate the private exponent, d, as the modular multiplicative inverse of e modulo phi(n)

2. Encryption:
- Convert the plaintext message to an integer m
- Calculate the ciphertext c = m^e mod n

3. Decryption:
- Retrieve the ciphertext c
- Calculate the plaintext message m = c^d mod n
```

Without knowing p and q, I sought a way to calculate Euler's totient. I saw a lot of implementations
that I personally could not get to work. Then I found the sympy library, which also has a method
for calculating the modular inverse. Jackpot!

In my search, I also found Pollard's rho algorithm and included it just for fun (see [rho.py](./rho.py) 👀)
