import contextlib
import io

def main():
        print(add_noise("hello"))

f = io.StringIO()
with contextlib.redirect_stdout(f):
    from b import *

main()
