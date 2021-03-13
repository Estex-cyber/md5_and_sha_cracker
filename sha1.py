import hashlib

pass_found_sha1 = 0

input_hash_sha1 = input("Enter hashed password: ")

pass_doc_sha1 = input("Enter password file name including path: ")

try:
    pass_file_sha1 = open(pass_doc_sha1, 'r')
except:
    print("Error!")
    print(pass_doc_sha1, "is not found")
    quit()

for word in pass_file_sha1:
    enc_word_sha1 = word.encode('utf-8')

    hash_word_sha1 = hashlib.sha1(enc_word_sha1.strip())

    digest_sha1 = hash_word_sha1.hexdigest()

    if digest_sha1 == input_hash_sha1:
        print("Password found.\nThe password is:", word)
        pass_found_sha1 = 1
        break

if not pass_found_sha1:
    print("Password is not found")