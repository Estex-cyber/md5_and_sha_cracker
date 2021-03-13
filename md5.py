import hashlib

pass_found_md5 = 0

input_hash_md5 = input("Enter hashed password: ")

pass_doc_md5 = input("Enter password file name including path: ")

try:
    pass_file_md5 = open(pass_doc_md5, 'r')
except:
    print("Error!")
    print(pass_doc_md5, "is not found")
    quit()

for word in pass_file_md5:
    enc_word_md5 = word.encode('utf-8')

    hash_word_md5 = hashlib.md5(enc_word_md5.strip())

    digest = hash_word_md5.hexdigest()

    if digest == input_hash_md5:
        print("Password found.\nThe password is:", word)
        pass_found_md5 = 1
        break

if not pass_found_md5:
    print("Password is not found")