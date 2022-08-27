# file = open("partho.txt", 'a')
# var = file.write("Hi this is partho. Partho is a good boy. He wants to be a Data Scientist")
# print(var)
# file.close()

f = open("partho.txt", "r+")
print(f.read())
f.write("Hello world \n")

# f.close()

