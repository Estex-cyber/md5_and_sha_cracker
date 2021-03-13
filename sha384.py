import hashlib

pass_found_sha384 = 0

input_hash_sha384 = input("Enter hashed password: ")

pass_doc_sha384 = input("Enter password file name including path: ")

try:
    pass_file_sha384 = open(pass_doc_sha384, 'r')
except:
    print("Error!")
    print(pass_doc_sha384, "is not found")
    quit()

for word in pass_file_sha384:
    enc_word_sha384 = word.encode('utf-8')

    hash_word_sha384 = hashlib.sha384(enc_word_sha384.strip())

    digest_sha384 = hash_word_sha384.hexdigest()

    if digest_sha384 == input_hash_sha384:
        print("Password found.\nThe password is:", word)
        pass_found_sha384 = 1
        break

if not pass_found_sha384:
    print("Password is not found")