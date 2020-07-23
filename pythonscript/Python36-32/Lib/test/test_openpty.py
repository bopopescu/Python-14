# Test to see if openpty works. (But don't worry if it isn't available.)

import os, unittest

if not hasattr(os, "openpty"):
    raise unittest.SkipTest("os.openpty() not available.")


class OpenptyTest(unittest.TestCase):
    def test(self):
        main, subordinate = os.openpty()
        self.addCleanup(os.close, main)
        self.addCleanup(os.close, subordinate)
        if not os.isatty(subordinate):
            self.fail("Subordinate-end of pty is not a terminal.")

        os.write(subordinate, b'Ping!')
        self.assertEqual(os.read(main, 1024), b'Ping!')

if __name__ == '__main__':
    unittest.main()