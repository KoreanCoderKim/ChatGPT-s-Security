import hashlib
class HashSecurity:
    # 큰 소수 (충돌 방지를 위한 큰 값)
    P = 2**521 - 1  
    def ultra_secure_fixed_hash(s):
        H = 0

        # 각 문자에 대해 고정된 비선형 변환 적용
        for i, char in enumerate(s):
            K = ord(char)  # 문자 ASCII 값
            H += ((i + 1) ** (K * 2 + 5)) % HashSecurity.P  # 비선형 변환

        # H 값을 바이트로 변환
        H_bytes = H.to_bytes((H.bit_length() + 7) // 8, byteorder='big')

        # SHA3-512 해싱
        hash_output = hashlib.sha3_512(H_bytes).digest()

        return hash_output.hex()