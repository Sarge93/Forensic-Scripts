import msoffcrypto

encrypted = open("C:\\Users\\John Doe\\Desktop\\c38-xlm-macros\\c38-xlm-macros\\sample1-fb5ed444ddc37d748639f624397cff2a.bin", "rb")
file = msoffcrypto.OfficeFile(encrypted)

file.load_key(password="VelvetSweatshop")  

with open("C:\\Users\\John Doe\\Desktop\\decrypted.bin", "wb") as f:
    file.decrypt(f)

encrypted.close()
