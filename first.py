passwd_file = open("kody.txt", "r")
#read_data = passwd_file.read()
print passwd_file.read()
#passwd_file.close()
if passwd_file == "sdasfasf":
    print("Poprawny kod")
else:
    print("Dupa")