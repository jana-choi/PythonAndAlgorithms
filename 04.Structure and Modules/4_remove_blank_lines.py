import sys

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="UTF-8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()
    return lines

def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, encoding="UTF-8", mode="w")
        for line in lines:
            fh.write(line)
    except (EnvironmentError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()

def remove_blank_lines():
    if len(sys.argv) < 2:
        print("Usage: python {} [file ...]".format(sys.argv[0]))
    
    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)

if __name__ == "__main__":
    remove_blank_lines()