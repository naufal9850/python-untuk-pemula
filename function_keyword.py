def belajar_python(name, age):
    print("Halo, Saya %s. Umur Saya %d" % (name, age))

# Contoh Function di atas. Jika kita memanggil Function dan mengirim Arguments tanpa nama "key" nya
# maka kita harus menuliskannya secara berurutan (name, age)
belajar_python("Naufal", 17) # Halo, Saya Naufal. Umur Saya 17

# Tetapi jika kita memanggil Function dan mengirim Arguments dengan nama "key" nya
# maka kita tidak harus menulliskannya secara berurutan (age, name)
belajar_python(age = 14, name="Dimas") # Halo, Saya Fika. Umur Saya 25
