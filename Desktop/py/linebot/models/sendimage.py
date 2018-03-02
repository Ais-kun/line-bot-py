class sendimage(send_imagedata):
	    """ImageSendMessage.

    https://devdocs.line.me/en/#image
    """

    def __init__(self, original_content_url=None, preview_image_url=None, **kwargs):
        """__init__ method.

        :param str original_content_url: Image URL.
            HTTPS
            JPEG
            Max: 1024 x 1024
            Max: 1 MB
        :param str preview_image_url: Preview image URL
            HTTPS
            JPEG
            Max: 240 x 240
            Max: 1 MB
        :param kwargs:
        """
        super(ImageSendMessage, self).__init__(**kwargs)

        self.type = 'image'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url