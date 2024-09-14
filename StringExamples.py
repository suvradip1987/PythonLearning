mystring = 'Welcome to Python'

multilineString = ''' This is an example on how to write multiline string in Python.
This is really cool.
'''

print (multilineString)


# How to Confirm That a Python String Contains Another String

raw_file_content = """Hi there and welcome.
... This is a special hidden file with a SECRET secret.
... I don't want to tell you The Secret,
... but I do want to secretly tell you that I have one."""

print('secret' in raw_file_content)

# slice example
slicedString= mystring[0:7]
print(slicedString.lower())

slicedString1= mystring[:7]
print(slicedString1.upper())

slicedString2= mystring[8:]
print(slicedString2)