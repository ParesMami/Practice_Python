# Say Hello to user

#defining a function here using def
def Hello(u):
    print('Hello, ', u)

#input here from user
# here I add strip to remove white spaces before and after the input string
#capitlize so first letter will be a capital letter
name = input('Hi, what is your name? ').capitalize().strip()
Hello(name)