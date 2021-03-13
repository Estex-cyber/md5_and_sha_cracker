import hashlib

pass_found_sha512 = 0

input_hash_sha512 = input("Enter hashed password: ")

pass_doc_sha512 = input("Enter password file name including path: ")

try:
    pass_file_sha512 = open(pass_doc_sha512, 'r')
except:
    print("Error!")
    print(pass_doc_sha512, "is not found")
    quit()

for word in pass_file_sha512:
    enc_word_sha512 = word.encode('utf-8')

    hash_word_sha512 = hashlib.sha512(enc_word_sha512.strip())

    digest_sha512 = hash_word_sha512.hexdigest()

    if digest_sha512 == input_hash_sha512:
        print("Password found.\nThe password is:", word)
        pass_found_sha512 = 1
        break

if not pass_found_sha512:
    print("Password is not found")