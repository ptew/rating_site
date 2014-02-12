# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Profile.last_name'
        db.delete_column(u'ratings_profile', 'last_name')

        # Deleting field 'Profile.first_name'
        db.delete_column(u'ratings_profile', 'first_name')

        # Deleting field 'Profile.education'
        db.delete_column(u'ratings_profile', 'education')

        # Deleting field 'Profile.work'
        db.delete_column(u'ratings_profile', 'work')

        # Adding field 'Profile.rep'
        db.add_column(u'ratings_profile', 'rep',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profile.status'
        db.add_column(u'ratings_profile', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Advice.name'
        db.delete_column(u'ratings_advice', 'name')

        # Deleting field 'Advice.pub_date'
        db.delete_column(u'ratings_advice', 'pub_date')

        # Adding field 'Advice.company'
        db.add_column(u'ratings_advice', 'company',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=20),
                      keep_default=False)

        # Adding field 'Advice.ticker'
        db.add_column(u'ratings_advice', 'ticker',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=20),
                      keep_default=False)

        # Adding field 'Advice.view_count'
        db.add_column(u'ratings_advice', 'view_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Advice.price_target'
        db.add_column(u'ratings_advice', 'price_target',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Advice.time_frame'
        db.add_column(u'ratings_advice', 'time_frame',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Advice.content'
        db.alter_column(u'ratings_advice', 'content', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Profile.last_name'
        db.add_column(u'ratings_profile', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=20),
                      keep_default=False)

        # Adding field 'Profile.first_name'
        db.add_column(u'ratings_profile', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=20),
                      keep_default=False)

        # Adding field 'Profile.education'
        db.add_column(u'ratings_profile', 'education',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=25),
                      keep_default=False)

        # Adding field 'Profile.work'
        db.add_column(u'ratings_profile', 'work',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=25),
                      keep_default=False)

        # Deleting field 'Profile.rep'
        db.delete_column(u'ratings_profile', 'rep')

        # Deleting field 'Profile.status'
        db.delete_column(u'ratings_profile', 'status')

        # Adding field 'Advice.name'
        db.add_column(u'ratings_advice', 'name',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=20),
                      keep_default=False)

        # Adding field 'Advice.pub_date'
        db.add_column(u'ratings_advice', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default='none'),
                      keep_default=False)

        # Deleting field 'Advice.company'
        db.delete_column(u'ratings_advice', 'company')

        # Deleting field 'Advice.ticker'
        db.delete_column(u'ratings_advice', 'ticker')

        # Deleting field 'Advice.view_count'
        db.delete_column(u'ratings_advice', 'view_count')

        # Deleting field 'Advice.price_target'
        db.delete_column(u'ratings_advice', 'price_target')

        # Deleting field 'Advice.time_frame'
        db.delete_column(u'ratings_advice', 'time_frame')


        # Changing field 'Advice.content'
        db.alter_column(u'ratings_advice', 'content', self.gf('django.db.models.fields.CharField')(max_length=1000))

    models = {
        u'ratings.advice': {
            'Meta': {'object_name': 'Advice'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_target': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'performance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pieces_of_advice': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ratings.Advice']", 'through': u"orm['ratings.Connection']", 'symmetrical': 'False'}),
            'rep': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ratings']