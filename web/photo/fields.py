from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os


def _add_thumb(s):  # s는 이미지 파일명 => filename.jpg
    parts = s.split(".")
    parts.insert(-1, "thumb")  # filename.jpg => filename.thumb.jpg
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)  # PIL라이브러리를 이용해 썸네일 생성
        # Resolve "cannot write mode RGBA"
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background = background.convert('RGB')
        background.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
        background.save(self.thumb_path, 'JPEG')
        # background.save(self.thumb_path, 'PNG')

    def delete(self, save=True):  # 원본이미지와 썸네일 이미지를 동시에 삭제
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


class ThumbnailImageField(ImageField):
    # 새로운 filefield 클래스를 정의할 경우 그에 상응하는 File 처리 클래스를 attr_class 속성에 지정
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)

