#%%
def test_speed(language="py"):
    """
    Evaluate how fast both of the functions are now.

    language (str): can either be py or c to makes
                    tests for. Default to 'py'.
    """
    import timeit
    i = 10000

    if language == "py":
        py = timeit.timeit("hello_py.say_hello_to('World')", setup="import hello_py", number=i)
        return py
    elif language == "c":
        c = timeit.timeit("hello_c.say_hello_to('World')", setup="import hello_c", number=i)
        return c
    else:
        raise Exception(f"Such {language} language is not included")

if __name__ == "__main__":
    py_speed = test_speed(language="py")
    c_speed  = test_speed(language="c")

    print(f"Cython is faster than Python by {round(py_speed/c_speed, 2)}x")
    """
    Expected output to what I received:
    =======================================
    Cython is faster than Python by 1.47x
    =======================================
    """
# %%
