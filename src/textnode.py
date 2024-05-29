
class TextNode:
	def __init__(self, TEXT, TEXT_TYPE, URL=None):
		self.__text = TEXT;
		self.__text_type = TEXT_TYPE;
		self.__url = URL;

	def __eq__(self):
		return self.__text == self.__text_type and self.__text == self.__url;

	def __repr__(self):
		return f"TextNode({self.__text}, {self.__text_type}, {self.__url})"\
	