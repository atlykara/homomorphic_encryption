### Homomorphic Encryption (CKKS + TenSEAL) ###

This project demonstrates basic encrypted computation using the **CKKS homomorphic encryption scheme** with the **TenSEAL** library.  
The application encrypts two user-provided numbers, performs addition and multiplication on encrypted data, and decrypts the results.

----------------------------------------------------------------

I run the project on **WSL2 (Ubuntu)** using a **Python virtual environment (venv)** for isolated TenSEAL installation.

## Environment Setup (WSL2 + Ubuntu)

# 1. TenSEAL requires CMake and build tools, which are available natively on Ubuntu:

```bash
    sudo apt update
    sudo apt install -y build-essential cmake python3-dev python3-pip git
```
# 2. Create and activate a virtual environment for clean setup

```bash
    python3 -m venv venv
    source venv/bin/activate
```
# 3. Install Python requirements (Numpy & TenSEAL)

```bash
    pip install -r requirements.txt
```

## How to Run ##

```bash
    python3 main.py
```

The program will:
    -Ask for two input numbers
    -Encrypt both values with CKKS
    -Perform while encrypted:
        (a + b)
        (a - b)
        (a * b)
        (a^2)
        (b^2)
        (a + b) * 5
        (a^2 - b^2)
        (a + b) / 2
    -Decrypt and print the results

# Note: CKKS uses approximate arithmetic, so small floating-point differences are expected.

### Project Structure ####
```bash
homomorphic_encryption/
│
├── main.py
├── requirements.txt
└── README.md
```