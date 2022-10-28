import subprocess
import os
import sys
import re
import pytest
import src.cagrepmax

class color:
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def test_dinuc() :

    if not os.path.isdir("FASTA") :
        errmsg = "ERROR: FASTA directory is missing in the root of the repo"
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
        raise Exception("Autograding workflow problem")

    fnames = os.listdir("FASTA")

    for f in fnames :
        if (not f.endswith(".fa")) :
            errmsg = "ERROR: %s should not be present in the FASTA directory" %(f)
            print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            raise Exception("Autograding workflow problem")
        else :
            n = re.search('[1-3]_([0-9]+)_CAGs', f).group(1)
            if (n) :
                n = int(n)
            else :
                errmsg = "ERROR: %s has a malformed FASTA filename" %(f)
                print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
                raise Exception("Autograding workflow problem")

            ## call from the command line to verify whether the program correctly
            ## transfers command-line arguments to the main() function
            cmd = ['python3', 'src/cagrepmax.py', f]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o, e = proc.communicate()

            if (proc.returncode == 0) :
                r = int(o.decode('ascii'))

                if r != n :
                    errmsg = "ERROR: your program wrongly outputs a maximum of %d CAG repeats in FASTA file %s, while the maximum is %d !!" %(r, f, n)
                    print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
            else :
                errmsg = "ERROR: your program did not run correctly. Please see below:"
                print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)
                errmsg = e.decode('ascii')
                errmsg = errmsg.split('\n')
                for e in errmsg :
                    print(color.ERROR+color.BOLD+e+color.END, file=sys.stderr)
                r = -1
            
        assert r == n
