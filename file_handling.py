# Create a new file
#f = open("/Users/mikiyas/Downloads/sample.txt", 'x')

# write This is a test on created file
f = open("/Users/mikiyas/Downloads/sample.txt", 'w')
f.write("This is a test!")
f.close()

# open the append and read

f = open("/Users/mikiyas/Downloads/sample.txt", 'r')
print(f.read())
