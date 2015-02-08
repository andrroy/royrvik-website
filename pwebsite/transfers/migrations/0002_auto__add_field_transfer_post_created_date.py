# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Transfer_Post.created_date'
        db.add_column(u'transfers_transfer_post', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Transfer_Post.created_date'
        db.delete_column(u'transfers_transfer_post', 'created_date')


    models = {
        u'transfers.ro_post': {
            'Meta': {'object_name': 'RO_Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'transfers.sc_rating': {
            'Meta': {'object_name': 'SC_Rating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of': ('django.db.models.fields.IntegerField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transfers.Transfer_Post']"}),
            'rating_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'transfers.transfer_post': {
            'Meta': {'object_name': 'Transfer_Post'},
            'context_post': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'context_poster': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'context_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_content': ('django.db.models.fields.TextField', [], {}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poster_url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['transfers']