def read_file(file_name):
    try:
        file = open(file_name, "r")
    except IOError:
        print("__CONTENT_START__\n__NO_SUCH_FILE__")
    else:
        print("__CONTENT_START__")
        print(file.read())
        file.close()
    finally:
        print("__CONTENT_END__")


read_file("not_exist_file.txt")
print()
read_file("exist_file.txt")

