def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "HELLO"
    print(s)

    # Combining bytes and string -> decode
    b_decoded = b.decode('utf-8')
    print('Decoding:', b_decoded + s)

    # Encode string
    s_encoded = s.encode('utf-8')
    print('Encoding:', b + s_encoded)

    s_encoded32 = s.encode('utf-32')
    print('Encoding 32:', b + s_encoded32)

if __name__ == "__main__":
    main()