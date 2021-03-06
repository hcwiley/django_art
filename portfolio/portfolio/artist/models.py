from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
import datetime
import shutil, uuid, os

class ParentMedia(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  video_link = models.CharField(max_length=255, blank=True, null=True, default="")
  image = models.ImageField(upload_to='artist_media/', default="", null=True, blank=True, editable=False)
  thumbnail = models.ImageField(upload_to='artist_media/', default="", null=True, blank=True, editable=False)
  full_res_image = models.ImageField(upload_to='artist_media/', default="", null=False, blank=False)
  is_default_image = models.BooleanField(default=False)

  class Meta:
    ordering = ['name']
    verbose_name = u'All media'
    verbose_name_plural = u'All media'

  def __unicode__(self):
    return self.name

  def thumb(self):
    return "%s%s" % (settings.MEDIA_URL, self.thumbnail.name)

  def img(self):
    return "%s%s" % (settings.MEDIA_URL, self.image.name)

  def full_res(self):
    p = self.full_res_image.path
    fold = os.path.dirname(p)
    fold = fold.split("/")
    fold = fold[len(fold)-1]
    return "%s%s/%s" % (settings.MEDIA_URL, fold,os.path.basename(p))

  def height(self):
    try:
      return self.image.height
    except:
      return ""

  def admin_thumb(self):
    html = ''
    if self.thumbnail:
      html += "<div class='col-xs-12'><div class='col-xs-6'><a class='btn btn-block btn-sm btn-success' href='/image/rotate/left/%s'>rotate left</a></div>"% (self.id)
      html += "<div class='col-xs-6'><a class='btn btn-block btn-sm btn-danger' href='/image/rotate/right/%s'>rotate right</a></div></div>"% (self.id)
      html += "<img src='%s'/>" % ( self.thumb())
      return html
    return ""
  admin_thumb.allow_tags = True


  def video(self):
    html = ""
    if self.video_link.count("vimeo") > 0:
      html = '<iframe src="//player.vimeo.com/video/%s" width="100%%" height="400px" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>' % (self.video_link[self.video_link.rindex("/") + 1 :])
    elif self.video_link.count("you") > 0:
      if self.video_link.count("?v=") > 0:
        video = self.video_link[self.video_link.rindex("=") + 1:]
      else:
        video = self.video_link[self.video_link.rindex("/") + 1:]
      html = '<iframe width="100%%" height="400px" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % video
    return html

  def save(self, *args, **kwargs):
    super(ParentMedia, self).save()
    if not self.thumbnail:
      orig = p = self.full_res_image.path
      ext = p[p.rfind("."):].lower()
      p = p.rstrip(os.path.basename(orig))
      u = str(uuid.uuid4())[:18]
      p = "%s/%s%s" % (p,u,ext)
      shutil.move(orig, p)
      p = "artist_media/%s%s" % (u,ext)
      self.full_res_image = p
    self.saveImage()
    self.saveThumbnail()

  def rotateImage(self):
    from PIL import Image
    path = self.full_res_image.path
    image = Image.open(path)
    try:
      if self.left:
        print "turn left"
        image = image.rotate(90)
    except:
      pass
    try:
      if self.right:
        print "turn right"
        image = image.rotate(-90)
    except:
      pass
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    path = path[1].strip("/")
    self.full_res_image = "%s" % (path)
    super(ParentMedia, self).save()

  def saveImage(self):
    from PIL import Image
    path = self.full_res_image.path
    image = Image.open(path)
    size = (950,950)
    image.thumbnail(size, Image.ANTIALIAS)

    dot = path.rindex('.')
    path = (path[:dot], path[dot:])
    path = "%s-small%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    path = path[1].strip("/")
    self.image = "%s" % (path)
    super(ParentMedia, self).save()

  def saveThumbnail(self):
    from PIL import Image
    path = self.full_res_image.path
    image = Image.open(path)

    size = (450,450)

    image_ratio = image.size[0] / float(image.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > image_ratio:
      image = image.resize((size[0], int(round(size[0] * image.size[1] / image.size[0]))),
          Image.ANTIALIAS)
      # Crop in the top, middle or bottom
      box = (0, int(round((image.size[1] - size[1]) / 2)), image.size[0],
              int(round((image.size[1] + size[1]) / 2)))
      image = image.crop(box)
    elif ratio < image_ratio:
      image = image.resize((int(round(size[1] * image.size[0] / image.size[1])), size[1]),
          Image.ANTIALIAS)
      box = (int(round((image.size[0] - size[0]) / 2)), 0,
              int(round((image.size[0] + size[0]) / 2)), image.size[1])
      image = image.crop(box)
    else :
      image = image.resize((size[0], size[1]),
            Image.ANTIALIAS)

    #image.thumbnail((450,450), Image.ANTIALIAS)
    dot = path.rindex('.')
    path = (path[:dot], path[dot:])
    path = "%s-thumb%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    path = path[1].strip("/")
    self.thumbnail = "%s" % (path)
    super(ParentMedia, self).save()

class Artist(AbstractUser):
  # custom fields
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  tagline = models.CharField(max_length=255, blank=True, null=True, default="")
  slug = models.CharField(max_length=100, blank=True, null=True, default="", editable=False)
  bio = models.TextField(blank=True, null=True, default="")
  artist_statement = models.TextField(blank=True, null=True, default="")
  website = models.CharField(max_length=100, blank=True, null=True, default="")
  cv = models.FileField(upload_to='artist_media/', blank=True, null=True, default="")
  head_shot = models.ForeignKey(ParentMedia, blank=True, null=True)
  cover_photo = models.ForeignKey(ParentMedia, blank=True, null=True, related_name='cover_photo')

  class Meta:
    ordering = ['name']

  def __unicode__(self):
    return self.name

  def cv_link(self):
    return "%s%s" % (settings.MEDIA_URL, self.cv.name)

  def cv_name(self):
    if self.cv:
      return "%s-CV%s" % (self.name, self.cv.name[self.cv.name.rindex("."):])
    else:
      return ""

  def web(self):
    if self.website.count("http") > 0:
      return self.website
    else:
      return "http://%s" % self.website

  def thumb(self):
    image = self.artistmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.artistmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/artists/%s" % (self.slug)

class ArtistMediaCategory(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  slug = models.CharField(max_length=100, blank=True, null=True, default="", editable=False)
  position = models.PositiveSmallIntegerField("Position", default=1)

  class Meta:
    ordering = ['position']
    verbose_name = u'Category of Art'
    verbose_name_plural = u'Categories of Art'
  
  def __unicode__(self):
    return self.name


  def medias(self):
    return ArtistMedia.objects.filter(category=self)

  def save(self):
    super(ArtistMediaCategory, self).save()
    self.slug = slugify(self.name)
    super(ArtistMediaCategory, self).save()

  def get_absolute_url(self):
    return "/%s" % (self.slug)

  def thumb(self):
    image = self.artistmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.artistmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

class ArtistMedia(ParentMedia):
  category = models.ForeignKey(ArtistMediaCategory)
  position = models.PositiveSmallIntegerField("Position", default=1)
  description = models.TextField(blank=True, null=True, default="")
  dimensions = models.CharField(max_length=100, blank=True, null=True, default="")
  medium = models.CharField(max_length=100, blank=True, null=True, default="")
  year = models.CharField(max_length=4, blank=True, null=True, default="")
  aux_images = models.ManyToManyField(ParentMedia, related_name='aux_images', null=True, blank=True)
  
  class Meta:
    ordering = ('position', )
    verbose_name = u'Piece'
    verbose_name_plural = u'Pieces'

  def __unicode__(self):
    return self.name

  def save(self):
    super(ArtistMedia, self).save()

class Link(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  url = models.CharField(max_length=255, blank=True, null=True, default="")

  class Meta:
    ordering = ('name', )

  def __unicode__(self):
    return self.name

class Show(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  location = models.CharField(max_length=255, blank=True, null=True, default="")
  date = models.DateField(default=datetime.date.today)
  link = models.ForeignKey(Link, blank=True, null=True)

  class Meta:
    ordering = ('-date', )

  def __unicode__(self):
    return "%s (%s)" % (self.name, self.date)

  def pretty_date(self):
    return self.date.strftime("%B, %Y")

class Press(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  content = HTMLField(blank=True, null=True, default='')
  date = models.DateField(default=datetime.date.today)
  is_archived = models.BooleanField(default=False)

  class Meta:
    ordering = ['-date']
    verbose_name = u'Press About your art'
    verbose_name_plural = u'Press About your art'
  
  def __unicode__(self):
    return "%s (%s)" % (self.name, self.date)

  def thumb(self):
    image = self.pressmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.pressmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/press/%s-%s" % (self.date, self.pk)

class PressMedia(ParentMedia):
  press_article = models.ForeignKey(Press)
class PressLink(Link):
  press_article = models.ForeignKey(Press)
