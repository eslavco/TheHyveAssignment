import os
import sys


#  3F in hex
ERROR_BYTE = 63


def trivial_encoding(result_bytestring):
    return bytes([v for b in result_bytestring for v in (0, b)])


def sublist(list_a, list_b):
    if 0 == len(list_a):
        return 0

    if len(list_b) < len(list_a):
        return -1

    idx = -1
    while list_a[0] in list_b[idx + 1:]:
        idx = list_b.index(list_a[0], idx + 1)
        if list_a == list_b[idx:idx + len(list_a)]:
            return idx

    return -1


def short_encoding(result_bytestring):
    short_result = []
    mapped_bytes = []
    i = 0
    # iterate over each byte of result
    while i < len(result_bytestring):
        b = result_bytestring[i]
        # first check if the byte was mapped
        if not b in mapped_bytes:
            mapped_bytes.append(result_bytestring[i])
            short_result.extend((0, b))
            i += 1
        else:
            # check the mapped list and
            # get the index of longest sublist
            length_sublist = 0
            index_sublist = 0
            for j in range(len(result_bytestring[i:])):

                index = sublist(result_bytestring[i: i + j + 1], mapped_bytes)
                if index >= 0:
                    length_sublist = j + 1
                    index_sublist = index
                else:
                    break

            short_result.extend([len(mapped_bytes) - index_sublist, length_sublist])
            mapped_bytes.extend(result_bytestring[i:length_sublist + i])
            i += length_sublist
    return short_result


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
            result_bytestring.append(ERROR_BYTE)
    return result_bytestring


def main():
    # Reads the bystream and pass to decoder
    byte_stream = sys.stdin
    result_bytestring = decode(byte_stream)
    print(f" The corresponding string is {bytes(result_bytestring)}")

    # Assume that standard error needs to be show
    # only if binary data has an invalid or incomplete pairs

    if ERROR_BYTE in result_bytestring:
        env_variable = os.environ.get('USE_TRIVIAL_IMPLEMENTATION')

        short_encoding(result_bytestring)
        if not env_variable:
            # trivial encoding
            print(trivial_encoding(result_bytestring))
        else:
            print(short_encoding(result_bytestring))


if __name__ == '__main__':
    main()
