import one

print("top at two.py")

x = one.methodOne(50)
print(x)

if __name__=="__main__":
    print("two.py being called directly")
else:
    print("two.py being called from another module")