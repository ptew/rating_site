# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Advice.advice_content'
        db.delete_column(u'ratings_advice', 'advice_content')

        # Adding field 'Advice.content'
        db.add_column(u'ratings_advice', 'content',
                      self.gf('django.db.models.fields.CharField')(default='Ok', max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Advice.advice_content'
        db.add_column(u'ratings_advice', 'advice_content',
                      self.gf('django.db.models.fields.CharField')(default='Yes', max_length=1000),
                      keep_default=False)

        # Deleting field 'Advice.content'
        db.delete_column(u'ratings_advice', 'content')


    models = {
        u'ratings.advice': {
            'Meta': {'object_name': 'Advice'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
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
            'education': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'performance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pieces_of_advice': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ratings.Advice']", 'through': u"orm['ratings.Connection']", 'symmetrical': 'False'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['ratings']