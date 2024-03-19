'''
f= open("test.txt" , 'w') #'w', 'a', 'r'
f.write("#this is the first line\n")
f.write("#*this is the second line\n")
f.close
'''
with open("test.txt" , 'a') as f:
    f.write("first line\n")
    f.write("second line")
f.close
print(dir(f))

