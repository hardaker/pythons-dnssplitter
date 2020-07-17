import unittest
import io
import pyfsdb

def noop():
    return

class test_fsdb_splitter(unittest.TestCase):
    def test_fsdb_splitter(self):
        import dnssplitter

        psl = dnssplitter.DNSSplitter()

        input_stream=io.StringIO("#fsdb -F t one two\nwww.example.com\t2\nabc.def.example.co.uk\t1\naoeu.bogusss\t3\n")
        output_stream = io.StringIO()
        output_stream.close = noop

        psl.split_fsdb(input_stream, output_stream, ['one'])

        self.assertEqual(output_stream.getvalue(),
                         "#fsdb -F t one two one_prefix one_domain one_suffix\nwww.example.com\t2\twww\texample.com\tcom\nabc.def.example.co.uk\t1\tabc.def\texample.co.uk\tco.uk\naoeu.bogusss\t3\t\t\t\n#   | setup.py test\n",
                         "output headers are correct")
