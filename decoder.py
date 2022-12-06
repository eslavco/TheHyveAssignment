import sys
import os


def trivial_encoding(result_bytestring):
    return bytes([v for b in result_bytestring for v in (0, b)])


def short_encoding(result_bytestring):
    short_result = []
    mapped_bytes = []
    for i in range(len(result_bytestring)):
        b = result_bytestring[i]
        # first check if I mapped the byte already
        if not b in mapped_bytes:
            mapped_bytes.append(result_bytestring[i])
            short_result.append((0,b))
        else:
            for j in range(result_bytestring[i:]):
                if result_bytestring[i:]:

            #       TODO:   function is not finished
            #       we need to get the longest sublist from the mapped_bytes
            #       and return the index
                    pass


def decode(byte_stream):
    result_bytestring = []
    while (byte_pair := byte_stream.read(2)):
        try:
            pi, qi = byte_pair

            if pi == 0:
                result_bytestring.append(qi)
            elif pi > 0:
                result_bytestring.extend(result_bytestring[-pi:][:qi])
        except:
            # Append 3F byte instead that correspond to int 63
            result_bytestring.append(63)
    return result_bytestring



def main():
    # Reads the bystream and pass to decoder
    byte_stream = sys.stdin
    result_bytestring = decode(byte_stream)
    print(f" The corresponding string is {bytes(result_bytestring)}")

    # Check if we need output the standard error
    if 63 in result_bytestring:

        env_variable = os.environ.get('USE_TRIVIAL_IMPLEMENTATION')

        if not env_variable:
            # trivial encoding
            print(trivial_encoding(result_bytestring))
        else:
           print(short_encoding(result_bytestring))



if __name__ == '__main__':
    main()
