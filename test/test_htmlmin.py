# -*- coding: utf-8 -*-

import codecs
import os
import re
import unittest

from diminuendo import htmlmin


class TestAutoMinify(unittest.TestCase):
    """Test minifying different HTML blocks and automatically comparing
    them.

    Read :func:add_tests to understand the magics.

    """

def add_tests(cls):
    """Create dynamic test cases for each html file found in test/html
    and attach it as a method to a unittest TestCase class.

    .. warning:: HERE BE DRAGONS

    :param cls: a class to use to load the test cases
    :type cls: class
    """
    here = os.path.abspath(os.path.dirname(__file__))
    minifile_re = re.compile(r'.*-minified\.html')
    testfiles = [file for file in os.listdir(os.path.join(here,
                 'html')) if not minifile_re.match(file)]
    for testfile in testfiles:
        testname = testfile.rstrip('.html')
        # create a generic testcase comparing minified through
        # htmlmin.minify() and provided minified
        def testcase(self):
            htmlfile = os.path.join(here, 'html', testfile)
            minifile = os.path.join(here, 'html',
                                    testname + '-minified.html')
            self.assertEqual(
                htmlmin.minify(codecs.open(htmlfile).read()),
                codecs.open(minifile, encoding='utf-8').read().rstrip())

        testcase.__doc__ = "test {}".format(testname)
        testcase.__name__ = 'test_' + testname

        setattr(cls, testcase.__name__, testcase)

# dynamic loading of test cases
add_tests(TestAutoMinify)
