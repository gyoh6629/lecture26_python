def copy_image_file(image_file):
    index = image_file.rfind('.')
    copy_file = image_file[:index] + '_copy' + image_file[index:]
    with open(image_file, 'rb') as f:
        copy = f.read()
    with open(copy_file, 'wb') as cf:
        cf.write(copy)
    return copy_file
