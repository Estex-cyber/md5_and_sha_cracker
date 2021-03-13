import hashlib

pass_found_sha224 = 0

input_hash_sha224 = input("Enter hashed password: ")

pass_doc_sha224 = input("Enter password file name including path: ")

try:
    pass_file_sha224 = open(pass_doc_sha224, 'r')
except:
    print("Error!")
    print(pass_doc_sha224, "is not found")
    quit()

for word in pass_file_sha224:
    enc_word_sha224 = word.encode('utf-8')

    hash_word_sha224 = hashlib.sha224(enc_word_sha224.strip())

    digest_sha224 = hash_word_sha224.hexdigest()

    if digest_sha224 == input_hash_sha224:
        print("Password found.\nThe password is:", word)
        pass_found_sha224 = 1
        break

if not pass_found_sha224:
    print("Password is not found")