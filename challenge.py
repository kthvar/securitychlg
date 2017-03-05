import requests
from Crypto.PublicKey import RSA
 
def generate_nums(num, min=0, max=15, columns=1, base=16, format='plain', rnd='new'):
    """
    helper function to return a list of 'num' integers from 'min' to 'max'
    """

    # api-endpoint
    URL = "http://random.org/integers/"
     
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'num': num,
        'min': min,
        'max': max,
        'col': columns,
        'base': base,
        'format': format,
        'rnd': rnd
    }
     
    # sending get request and saving the response as response object
    response = requests.get(url = URL, params = PARAMS)
    data = response.text
    data = str(data)
    nums = data.split("\n")
    nums.pop()  # the last number is an empty string
    ret_str = ""
    for num in nums:
        ret_str += num
    return ret_str

nums = generate_nums(1024)
print(nums)

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    return private_key, public_key

p, N = generate_RSA()