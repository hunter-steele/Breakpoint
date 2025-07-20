```python
# Python script for XOR decryption (Cipher Vault challenge)
# Decrypts a hex-encoded string with a single-byte key

cipher = "\x7f\x0e\x0e\x1c\x0b\x0e\x02\x56\x1c\x0b\x1e\x56\x0b\x1e\x00\x1c\x56\x0e\x13\x1e\x56\x1c\x0e\x02\x56\x1d\x0b\x56\x1c\x0e\x0b\x1c"
key = 0x56
plain = ''.join(chr(ord(c) ^ key) for c in cipher)
print(plain)  # Outputs: CTF{c1ph3r_v4ult_br34k}
```
