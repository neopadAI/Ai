module = []
data_name = 'data.json'
secret_name = 'secret.json'
def data(data_=''):
    with open(data_name, 'r', encoding='utf-8') as file:
        for data_file in file:
            data_ = str(data_) + str(data_file)
        return str(data_)
    
def secret(secret_=''):
    with open(secret_name, 'r', encoding='utf-8') as file:
        for secret_file in file:
            secret_ = str(secret_) + str(secret_file)
        return str(secret_)
    
def code():
    __data__ = data()
    __secret__ = secret()
    __code__ = __data__ + ",\n" + __secret__
    return __code__