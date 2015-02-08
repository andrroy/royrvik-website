# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transfer_Post'
        db.create_table(u'transfers_transfer_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('poster_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('context_url', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('context_post', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('context_poster', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('post_content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'transfers', ['Transfer_Post'])

        # Adding model 'SC_Rating'
        db.create_table(u'transfers_sc_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number_of', self.gf('django.db.models.fields.IntegerField')()),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transfers.Transfer_Post'])),
        ))
        db.send_create_signal(u'transfers', ['SC_Rating'])

        # Adding model 'RO_Post'
        db.create_table(u'transfers_ro_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'transfers', ['RO_Post'])


    def backwards(self, orm):
        # Deleting model 'Transfer_Post'
        db.delete_table(u'transfers_transfer_post')

        # Deleting model 'SC_Rating'
        db.delete_table(u'transfers_sc_rating')

        # Deleting model 'RO_Post'
        db.delete_table(u'transfers_ro_post')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_content': ('django.db.models.fields.TextField', [], {}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poster_url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['transfers']