class NewString(str):
    """
    New string class that inherits all attributes and methods of the object str
    """

    def multireplace(self, replacement_sumbols, new_sumbols):
        """
        Method for replacing specified characters in a string with new characters.
        Single replacement and new characters are objects that are
        single words, parts of words, letters, special characters,
        or combinations thereof, enclosed in string literals.


        There are three ways to specify replacement and new characters:
        1)  Replaced and new characters are grouped into lists, sets or tuples of the same length.
            In this case, each character being replaced is changed to
            a new character located in the same place (having the same index).

        2)  One replacement character and one new character specified.

        3)  One new character and multiple replacement characters are specified,
            grouped into a list, set, or tuple.
            In this case, each character being replaced is changed to the same new character.

        When setting parameters in other ways than the above three, an valueError exception is thrown.
        All values contained in the replacement_sumbols and new_sumbols will be converted to strings.
        If such conversion is impossible, an TypeError exception will be generated.

        :param init_sumbols: str, list, set, tuple
        :param new_sumbols: str, list, set, tuple
        :return: str
        """

        if isinstance()
