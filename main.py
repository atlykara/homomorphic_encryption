import tenseal as ts

def main():
    print("=============== CKKS Homomorphic Encryption ===============\n")

    print("[1] Initializing CKKS context...")
    poly_modulus_degree = 8192
    coeff_mod_bit_sizes = [60, 40, 40, 60]
    scale = 2 ** 40

    context = ts.context(
        scheme=ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=poly_modulus_degree,
        coeff_mod_bit_sizes=coeff_mod_bit_sizes,
    )
    context.global_scale = scale

    context.generate_galois_keys()
    context.generate_relin_keys()
    print("[✓] CKKS context and keys successfully initialized.\n")

    # User input
    print("[2] Reading user input values... (integer)")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print("[✓] Input values received.\n")

    # Encode + Encrypt
    print("[3] Encrypting input values...")
    enc_a = ts.ckks_vector(context, [a])
    enc_b = ts.ckks_vector(context, [b])
    print("[✓] Encryption completed.\n")

    # Homomorphic operations
    print("[4] Performing homomorphic operations on encrypted data...")
    enc_add = enc_a + enc_b                  # a + b
    enc_sub = enc_a - enc_b                  # a - b
    enc_mul = enc_a * enc_b                  # a * b
    enc_a_sq = enc_a * enc_a                 # a^2
    enc_b_sq = enc_b * enc_b                 # b^2
    enc_mix = (enc_a + enc_b) * 5            # (a + b) * 5
    enc_diff_square = (enc_a - enc_b) * (enc_a + enc_b)  # a^2 - b^2
    enc_avg = (enc_a + enc_b) * 0.5          # (a + b) / 2
    print("[✓] Homomorphic computations completed.\n")

    # Decrypt results
    print("[5] Decrypting results...")
    out_add = enc_add.decrypt()[0]
    out_sub = enc_sub.decrypt()[0]
    out_mul = enc_mul.decrypt()[0]
    out_a_sq = enc_a_sq.decrypt()[0]
    out_b_sq = enc_b_sq.decrypt()[0]
    out_mix = enc_mix.decrypt()[0]
    out_diff_sq = enc_diff_square.decrypt()[0]
    out_avg = enc_avg.decrypt()[0]
    print("[✓] Decryption completed.\n")

    # Results
    print("~~~~~~~~~~~~~~~~~~~~ Final Results ~~~~~~~~~~~~~~~~~~~~")
    print("a + b =", out_add)
    print("a - b =", out_sub)
    print("a * b =", out_mul)
    print("a^2 =", out_a_sq)
    print("b^2 =", out_b_sq)
    print("(a + b) * 5 =", out_mix)
    print("a^2 - b^2 =", out_diff_sq)
    print("Average (a + b) / 2 =", out_avg)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

if __name__ == "__main__":
    main()