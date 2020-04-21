from microapp import MicroappProject

import os

here = os.path.dirname(os.path.abspath(__file__))
zipped = os.path.join(here, "data.gz")
unzipped = os.path.join(here, "data")

def test_basic():

    prj = MicroappProject()
    cmd = "gunzip %s -o %s" % (zipped, unzipped)

    ret = prj.main(cmd)

    assert ret == 0
    assert os.path.exists(unzipped)

    os.remove(unzipped)
