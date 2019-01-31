## Defines and returns the exception.

import sys
import linecache

def MyErrorException(Err, Name):
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print("\033[1;32;40m{}: {}, {},{}\n".format(Name, Err, filename, lineno))