from urllib.request import urlopen
import hashlib

sha256hash = input("\033[4mpsf\033[0m set(\033[91mhash/sha256\033[0m) > ")
url = str(input("\033[4mpsf\033[0m use(\033[91mpasswd/link/raw=true\033[0m) > "))
passlist = str(urlopen(url).read (), 'utf-8')
for password in passlist.split('\n'):
    hashgess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    if hashgess == sha256hash:
        print("Accurate Password is: " + str(password))
        quit()
    else:
        print("Checking for password: " + str(password) + " Matching failed.")
print("Password is Not Found in List.")
