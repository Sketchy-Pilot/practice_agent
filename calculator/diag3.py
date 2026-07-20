import os
print("cwd:", os.getcwd())
print("listdir:", os.listdir("."))
print("pkg exists:", os.path.isdir("pkg"))
print("pkg listdir:", os.listdir("pkg") if os.path.isdir("pkg") else "N/A")
print("__file__:", __file__)
