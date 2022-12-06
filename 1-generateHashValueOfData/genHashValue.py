import hashlib

while True:
    # Input the data from user
    data = input('Enter your data: ')

    #The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
    encoded_data = data.encode()

    # select the hash algorithm to generate hash value
    hash_algo = input('Enter hash algorithum [sha224, sha256, sha512, md5] : ')

    if hash_algo == 'sha224':
        hash_obj = hashlib.sha224(encoded_data)
    elif hash_algo == 'sha256':
        hash_obj = hashlib.sha256(encoded_data) #sha256 is most commonlly used hash algo
    elif hash_algo == 'sha512':
        hash_obj = hashlib.sha512(encoded_data)
    elif hash_algo == 'md5':
        hash_obj = hashlib.md5(encoded_data)
    else:
        print('please enter only listed options!')
        continue

    #the digest is returned as a string object of double length, containing only hexadecimal digits.    
    hash_value = hash_obj.hexdigest()
    print(hash_value)
    
    want_continue = input('\nDo you want to continue [y/n] : ').lower()
    print()
    
    if want_continue == 'n':
        break