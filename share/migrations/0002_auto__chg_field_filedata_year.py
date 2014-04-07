# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FileData.year'
        db.alter_column(u'share_filedata', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'FileData.year'
        db.alter_column(u'share_filedata', 'year', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        u'share.filedata': {
            'Meta': {'object_name': 'FileData'},
            'approved': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'course_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'department_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'file_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'uploader_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'uploader_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['share']