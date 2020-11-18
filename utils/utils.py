from ArtifyAPI import constants

def allowed_photo_type(filename):
    """
    Args:
        filename (string): photo name

    func check if photo file name extensions is correct.

    Returns:
        (bool): if file Ok it be True, in else False
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in constants.ALLOWED_EXTENSIONS_FOR_PHOTO

