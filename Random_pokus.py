from dataclasses import replace
from xml.sax.saxutils import prepare_input_source


my_text = open("test.txt")

x = my_text.read()
x = x.replace("a","b")
my_text = my_text.write("ahoj")
print(x)