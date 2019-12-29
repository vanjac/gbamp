import glob, os

BUFFER_SIZE = 4096

def main():
    for rawpath in glob.glob("*.raw"):
        print(rawpath)
        with open(rawpath.replace(".raw", ".gba"), 'wb') as outfile:
            with open('gbamp.gba', 'rb') as basefile:
                while True:
                    data = basefile.read(BUFFER_SIZE)
                    if not data:
                        break
                    outfile.write(data)
            outfile.write(b'GBAM')
            num_samples = os.path.getsize(rawpath) // 2
            # round up to nearest 4
            if num_samples % 4 != 0:
                num_samples += 4 - (num_samples % 4)
            print(num_samples, "samples")
            outfile.write(num_samples.to_bytes(4, byteorder='little'))
            with open(rawpath, 'rb') as rawfile:
                write_channel(rawfile, outfile, num_samples)  # left
                rawfile.seek(1, 0)  # one byte from start
                write_channel(rawfile, outfile, num_samples)  # right

def write_channel(infile, outfile, length):
    bytes_written = 0
    while True:
        data = infile.read(BUFFER_SIZE)
        if not data:
            break
        outfile.write(data[::2])
        bytes_written += len(data)
    pad_bytes = bytes([0]) * (length - bytes_written)
    outfile.write(pad_bytes)

if __name__ == "__main__":
    main()
