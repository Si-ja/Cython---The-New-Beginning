#%%
from hello_py import say_hello_to as hello_py
from hello_c import say_hello_to as hello_c

answer_1 = hello_py(name="World", iterations=20)
answer_2 = hello_c(name="James (?)", iterations=20)

print(f"Py answer: {answer_1}\nC answer: {answer_2}")

"""
Should give the output:
===================================
Py answer: Hello World
C answer: Hello James (?)
===================================
"""
# %%
