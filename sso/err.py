## Defines and returns the exception.

import sys
import linecache

def MyErrorException(Err, Name):
    tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_frame
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename,lineno, f.f_globals)
    print("{}: {}, {},{}".format(Name, Err, filename, lineno))