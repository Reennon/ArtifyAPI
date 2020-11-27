from constants import Constants


class Utils:
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
            return extension in Constants.ALLOWED_EXTENSIONS_FOR_PHOTO
        else:
            return False

    def allowed_script_type(filename):
        """
        Args:
            filename (string): photo name

        func check if script file name extensions is correct.

        Returns:
            (bool): if file Ok it be True, in else False
        """

        if '.' in filename:
            extension = filename.rsplit('.', 1)[1].lower()
            return extension in Constants.ALLOWED_EXTENSIONS_FOR_SCRIPT
        else:
            return False

    @staticmethod
    def allowed_module_type(filename):
        """
        Args:
            filename (string): module name

        func check if module file name extensions is correct.

        Returns:
            (bool): if file Ok it be True, in else False
        """

        if '.' in filename:
            extension = filename.rsplit('.', 1)[1].lower()
            return extension in Constants.ALLOWED_EXTENSIONS_FOR_MODULE
        else:
            return False