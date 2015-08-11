__author__ = 'alexander'

import sys
import os
import utils


def main(argv):
    tests = utils.load_tests(argv[1])
    test_file_name = utils.create_test_file(argv[2], tests)
    utils.run_tests(test_file_name)
    os.remove(test_file_name)


if __name__ == "__main__":
    main(sys.argv)
