def filelength(filename):
    try:
        infile = open(filename, 'r')
        content = infile.read()
        infile.close()
        return len(content)
    except FileNotFoundError:
        print(f"File {filename} not found.")
