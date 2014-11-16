# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParentMedia'
        db.create_table(u'artist_parentmedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('video_link', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('full_res_image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
            ('is_default_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'artist', ['ParentMedia'])

        # Adding model 'Artist'
        db.create_table(u'artist_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('artist_statement', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, null=True, blank=True)),
            ('head_shot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.ParentMedia'], null=True, blank=True)),
            ('cover_photo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cover_photo', null=True, to=orm['artist.ParentMedia'])),
        ))
        db.send_create_signal(u'artist', ['Artist'])

        # Adding M2M table for field groups on 'Artist'
        db.create_table(u'artist_artist_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm[u'artist.artist'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'artist_artist_groups', ['artist_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Artist'
        db.create_table(u'artist_artist_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm[u'artist.artist'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'artist_artist_user_permissions', ['artist_id', 'permission_id'])

        # Adding model 'ArtistMediaCategory'
        db.create_table(u'artist_artistmediacategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'artist', ['ArtistMediaCategory'])

        # Adding model 'ArtistMedia'
        db.create_table(u'artist_artistmedia', (
            (u'parentmedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artist.ParentMedia'], unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.ArtistMediaCategory'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('dimensions', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('medium', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(default='', max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'artist', ['ArtistMedia'])

        # Adding M2M table for field aux_images on 'ArtistMedia'
        db.create_table(u'artist_artistmedia_aux_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artistmedia', models.ForeignKey(orm[u'artist.artistmedia'], null=False)),
            ('parentmedia', models.ForeignKey(orm[u'artist.parentmedia'], null=False))
        ))
        db.create_unique(u'artist_artistmedia_aux_images', ['artistmedia_id', 'parentmedia_id'])

        # Adding model 'Link'
        db.create_table(u'artist_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'artist', ['Link'])

        # Adding model 'Show'
        db.create_table(u'artist_show', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Link'], null=True, blank=True)),
        ))
        db.send_create_signal(u'artist', ['Show'])

        # Adding model 'Press'
        db.create_table(u'artist_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('content', self.gf('tinymce.models.HTMLField')(default='', null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('is_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'artist', ['Press'])

        # Adding model 'PressMedia'
        db.create_table(u'artist_pressmedia', (
            (u'parentmedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artist.ParentMedia'], unique=True, primary_key=True)),
            ('press_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Press'])),
        ))
        db.send_create_signal(u'artist', ['PressMedia'])

        # Adding model 'PressLink'
        db.create_table(u'artist_presslink', (
            (u'link_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artist.Link'], unique=True, primary_key=True)),
            ('press_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Press'])),
        ))
        db.send_create_signal(u'artist', ['PressLink'])


    def backwards(self, orm):
        # Deleting model 'ParentMedia'
        db.delete_table(u'artist_parentmedia')

        # Deleting model 'Artist'
        db.delete_table(u'artist_artist')

        # Removing M2M table for field groups on 'Artist'
        db.delete_table('artist_artist_groups')

        # Removing M2M table for field user_permissions on 'Artist'
        db.delete_table('artist_artist_user_permissions')

        # Deleting model 'ArtistMediaCategory'
        db.delete_table(u'artist_artistmediacategory')

        # Deleting model 'ArtistMedia'
        db.delete_table(u'artist_artistmedia')

        # Removing M2M table for field aux_images on 'ArtistMedia'
        db.delete_table('artist_artistmedia_aux_images')

        # Deleting model 'Link'
        db.delete_table(u'artist_link')

        # Deleting model 'Show'
        db.delete_table(u'artist_show')

        # Deleting model 'Press'
        db.delete_table(u'artist_press')

        # Deleting model 'PressMedia'
        db.delete_table(u'artist_pressmedia')

        # Deleting model 'PressLink'
        db.delete_table(u'artist_presslink')


    models = {
        u'artist.artist': {
            'Meta': {'ordering': "['name']", 'object_name': 'Artist'},
            'artist_statement': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'cover_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cover_photo'", 'null': 'True', 'to': u"orm['artist.ParentMedia']"}),
            'cv': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'head_shot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.ParentMedia']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'artist.artistmedia': {
            'Meta': {'ordering': "('position',)", 'object_name': 'ArtistMedia', '_ormbases': [u'artist.ParentMedia']},
            'aux_images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'aux_images'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['artist.ParentMedia']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.ArtistMediaCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'parentmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artist.ParentMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'artist.artistmediacategory': {
            'Meta': {'ordering': "['position']", 'object_name': 'ArtistMediaCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'artist.link': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'artist.parentmedia': {
            'Meta': {'ordering': "['name']", 'object_name': 'ParentMedia'},
            'full_res_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_default_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'artist.press': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Press'},
            'content': ('tinymce.models.HTMLField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'artist.presslink': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PressLink', '_ormbases': [u'artist.Link']},
            u'link_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artist.Link']", 'unique': 'True', 'primary_key': 'True'}),
            'press_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.Press']"})
        },
        u'artist.pressmedia': {
            'Meta': {'ordering': "['name']", 'object_name': 'PressMedia', '_ormbases': [u'artist.ParentMedia']},
            u'parentmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artist.ParentMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'press_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.Press']"})
        },
        u'artist.show': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Show'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.Link']", 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['artist']