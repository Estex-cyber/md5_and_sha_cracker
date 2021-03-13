import hashlib

pass_found_sha256 = 0

input_hash_sha256 = input("Enter hashed password: ")

pass_doc_sha256 = input("Enter password file name including path: ")

try:
    pass_file_sha256 = open(pass_doc_sha256, 'r')
except:
    print("Error!")
    print(pass_doc_sha256, "is not found")
    quit()

for word in pass_file_sha256:
    enc_word_sha256 = word.encode('utf-8')

    hash_word_sha256 = hashlib.sha256(enc_word_sha256.strip())

    digest_sha256 = hash_word_sha256.hexdigest()

    if digest_sha256 == input_hash_sha256:
        print("Password found.\nThe password is:", word)
        pass_found_sha256 = 1
        break

if not pass_found_sha256:
    print("Password is not found")