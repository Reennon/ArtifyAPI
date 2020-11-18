from ArtifyAPI.constants import Constants


class Utils():
    @staticmethod
    def allowed_photo_type(filename):
        """
        Args:
            filename (string): photo name

        func check if photo file name extensions is correct.

        Returns:
            (bool): if file Ok it be True, in else False
        """

        if '.' in filename:
            extension = filename.rsplit('.', 1)[1].lower()
            if extension in Constants.ALLOWED_EXTENSIONS_FOR_PHOTO:
                return True
            else:
                return False
        else:
            return False
