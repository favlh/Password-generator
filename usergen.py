import random
import string

def password_generator(length=12):
    # Karakter yang digunakan dalam password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Menghasilkan password yang acak dan kompleks
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Contoh penggunaan:
for _ in range(10):
    print(password_generator(16))  # Menghasilkan password sepanjang 16 karakter
