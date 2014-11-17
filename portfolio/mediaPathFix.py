import os
from artist.models import *

cwd = os.path.abspath("/home/hcwiley/webapps/hcwiley_art_media/media")

for m in ParentMedia.objects.all():
  p = m.full_res_image.name
  p = p.replace("/media","")
  ending = p[p.find("artist_media/"):]
  p = os.path.join(cwd,ending)
  print("new path: %s" % p)
  m.full_res_image = p
  m.save()
