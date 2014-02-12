# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'ratings_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('participation_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('view_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ratings', ['User'])

        # Deleting field 'Profile.status'
        db.delete_column(u'ratings_profile', 'status')

        # Deleting field 'Profile.rep'
        db.delete_column(u'ratings_profile', 'rep')

        # Deleting field 'Profile.performance'
        db.delete_column(u'ratings_profile', 'performance')

        # Adding field 'Profile.world'
        db.add_column(u'ratings_profile', 'world',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'ratings_user')

        # Adding field 'Profile.status'
        db.add_column(u'ratings_profile', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profile.rep'
        db.add_column(u'ratings_profile', 'rep',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profile.performance'
        db.add_column(u'ratings_profile', 'performance',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Profile.world'
        db.delete_column(u'ratings_profile', 'world')


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