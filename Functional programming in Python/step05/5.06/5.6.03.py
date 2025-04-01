def get_extensions(file_list):
    def _get_extension(filename):
        if "." in filename:
            return filename.split(".")[-1]
        else:
            return ""

    return [_get_extension(filename) for filename in file_list]
