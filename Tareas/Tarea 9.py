# Creamos el archivo flag.txt
f = open('../flag.txt', 'a')
f.write("Este es un documento .txt\n")
f.close()

f = open('../flag.txt', 'r')
print(f.read())
f.close()

# Output: *Escribe "Este es un documento .txt" en el archivo flag.txt*