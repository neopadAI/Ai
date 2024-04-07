module = []
data_name = 'data.json'
secret_name = 'secret.json'
def set(key, name, author):
    module = {
        "key": key,
        "name": name,
        "author": author,
        "type": "AI"
    }

    with open(data_name, 'w', encoding='utf-8') as file:
        file.write(
"""{
    "name": """ + '"' + module["name"] + """",
    "author": """ + '"' + module["author"] + """",
    "type": """ + '"' + module["type"] + """"
}""")
    
    with open(secret_name, 'w', encoding='utf-8') as file:
        file.write(
"""{
    "key": """ + '"' + module["key"] + """"
}""")
    
    return module
