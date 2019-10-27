import sys

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError,TypeError)  as e:
        print("Conversion error:{}"\
            .format(str(e)))
        raise

if __name__ == "__main__":
    convert(sys.argv[1])