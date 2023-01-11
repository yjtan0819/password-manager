def load_key():
    key_file = open("key.key", "rb")
    key = key_file.read()
    key_file.close()
    return key