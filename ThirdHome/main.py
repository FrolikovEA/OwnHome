class AttrPhoto:
    testFile = None
    testAtttr = None


class AttrMove:
    pass


class AttrImage:
    pass


class GettingFileDisk:
    def save(self):
        pass

    def getFile(self):
        pass


class GettingFileCloud:
    def save(self):
        pass

    def getFile(self):
        pass


class BaseFile:
    def __init__(self, name: str, size: int, data_create: str, owner: str, **kwargs):
        self.name = name
        self.size = size
        self.date_create = data_create
        self.owner = owner
        self.add_new_attr(kwargs)

    def add_new_attr(self, kwargs):
        for item_param in kwargs.items():
            if hasattr(self, item_param[0]):
                setattr(self, item_param[0], item_param[1])


class PhotoFile(BaseFile, AttrPhoto, GettingFileDisk):
    def convert_to_png(self):
        pass


class MoveFile(BaseFile, AttrMove, GettingFileDisk):
    pass


class ImageFile(BaseFile, AttrMove, GettingFileDisk):
    pass


A = PhotoFile(name="sdf", size=100, data_create="10.20.2015", owner="Mi", testFile="sdf", testAtttr="ddd")
