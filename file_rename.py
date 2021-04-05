import os

def main():
    i = 0
    path = "/Users/matthewhenderson/test/images"
    for filename in os.listdir(path):
        dest = "img" + str(i) + ".jpg"
        source = path + '/' + filename
        # dest = path + dest
        os.rename(source, dest)
        i += 1
    
if __name__ == '__main__':
    main()