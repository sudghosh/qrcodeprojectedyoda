from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class website(models.Model):
    name = models.CharField(max_length=220)
    qrcodes = models.ImageField(upload_to='qr_codes',blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        print(str('https://'+self.name))
        qrcode_img = qrcode.make(str('https://'+self.name))
        canvas = Image.new('RGB', (290,290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcodes.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)