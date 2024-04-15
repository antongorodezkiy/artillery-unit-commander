import argparse

argparser = argparse.ArgumentParser(description = f"Artillery Unit Commander")
argparser.add_argument('-v', '--verbose', action = 'store_true')  # on/off flag
args = argparser.parse_args()