def list_to_string(content):
    """Join list elements together to create continuous text"""
    return '\n'.join(content)


def overwrite_and_reset(file, content):
    """Rewrite a file with `content` and then seek back to the start"""
    file.seek(0)
    file.truncate()
    file.write(content)
    file.seek(0)
