from hashlib import sha256
MAX_NONCE = 100000000000
def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()
def mine(block_number, transactions, previous_hash,prefix_zeroes):
    prefix_string = '0'*prefix_zeroes
    for nonce in range(MAX_NONCE):
        text = str(block_number)+transactions+previous_hash+str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_string):
            print("yya yo sucessfully mined bitcoin with nonce value: {}".format(nonce))
            return new_hash
    raise BaseException(f"Couldn't find correct has trying anfte+r+ +{MAX_NONCE} times")

if __name__ == '__main__':
    import time
    transactions='''
    Dhaval->Bhavin`->20,
    Mando->Cara->45
    '''
    difficulty= 20
    start = time.time()

    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficulty)
    total_time = str((time.time()-start))
    print(total_time)

    print(new_hash)