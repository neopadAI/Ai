import module.add as add
import module.read as read
import module.xml.read as xml

secret = 'YOUR_SECRET_KEY'
name = 'monkeyAI'
author = 'Neopad - neopadAI'

module = add.set(secret, name, author)  # create module

read_module_data = read.data()  # read data.json file
read_module_secret = read.secret()  # read secret.json file
read_module_code = read.code()  # read data.json and secret.json files
read_module_xml = xml.set('map.xml')  # read the map.xml file and print its content

print(read_module_data)  # print data.json file
print(read_module_secret)  # print secret.json file
print(str(read_module_code))  # print data.json and secret.json files

print(module["name"])  # display name