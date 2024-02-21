class AttrPhoto:
    testFile = None
    testAtttr = None


class AttrMove:
    pass


class AttrImage:
    pass


class GettingFileDisk:
    def _save_byte(self):
        pass

    def get_file_byte(self):
        pass


class GettingFileCloud:
    def _save_byte(self):
        pass

    def get_file_byte(self):
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

    def _save_attr(self):
        pass


class SpecificFileSaveAndGettingForDisk(BaseFile, GettingFileDisk):
    def save(self):
        super()._save_byte()
        super()._save_attr()


class SpecificFileSaveAndGettingForCloud(BaseFile, GettingFileCloud):
    def save(self):
        super()._save_byte()
        super()._save_attr()


class PhotoFile(SpecificFileSaveAndGettingForDisk, AttrPhoto):
    def convert_to_png(self):
        pass


class MoveFile(SpecificFileSaveAndGettingForDisk, AttrMove):
    pass


class ImageFile(SpecificFileSaveAndGettingForCloud, AttrMove):
    pass


A = PhotoFile(name="sdf", size=100, data_create="10.20.2015", owner="Mi", testFile="sdf", testAtttr="ddd")
A.get_file_byte()
A.save()
