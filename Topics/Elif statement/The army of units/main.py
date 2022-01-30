

units = int(input())
if units < 1:
    print("no army")
elif units < 10:
    print("few")
elif units < 50:
    print("pack")
elif units < 500:
    print("horde")
elif units < 1000:
    print("swarm")
else:
    print("legion")