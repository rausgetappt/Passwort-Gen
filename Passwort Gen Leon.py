import random

ascii_range = range(0, 128)  # ändere die Range auf 0 bis 127

password = []
while len(password) < 10:
    char = chr(random.choice(ascii_range))
    if ord(char) >= 32:  # überprüfe, ob der ASCII-Wert über 32 liegt
        password.append(char)

password_str = "".join(password)

print(password_str)