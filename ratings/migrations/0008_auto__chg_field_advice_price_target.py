# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Advice.price_target'
        db.alter_column(u'ratings_advice', 'price_target', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Advice.price_target'
        db.alter_column(u'ratings_advice', 'price_target', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'ratings.advice': {
            'Meta': {'object_name': 'Advice'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_target': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time_frame': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.connection': {
            'Meta': {'object_name': 'Connection'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'rating_sum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pieces_of_advice': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ratings.Advice']", 'through': u"orm['ratings.Connection']", 'symmetrical': 'False'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'world': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ratings']