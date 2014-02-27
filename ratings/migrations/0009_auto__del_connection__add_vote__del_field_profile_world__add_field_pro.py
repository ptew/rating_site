# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Connection'
        db.delete_table(u'ratings_connection')

        # Adding model 'Vote'
        db.create_table(u'ratings_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'ratings', ['Vote'])

        # Deleting field 'Profile.world'
        db.delete_column(u'ratings_profile', 'world')

        # Adding field 'Profile.profile_number'
        db.add_column(u'ratings_profile', 'profile_number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Connection'
        db.create_table(u'ratings_connection', (
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('rating_sum', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ratings', ['Connection'])

        # Deleting model 'Vote'
        db.delete_table(u'ratings_vote')

        # Adding field 'Profile.world'
        db.add_column(u'ratings_profile', 'world',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Profile.profile_number'
        db.delete_column(u'ratings_profile', 'profile_number')


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
        u'ratings.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.vote': {
            'Meta': {'object_name': 'Vote'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.User']"})
        }
    }

    complete_apps = ['ratings']