import re


class PrePro():

    @staticmethod
    def filter(code):
        code = re.sub(r'(#=)((.|/n)*?)(=#)', '', code)
        return code
