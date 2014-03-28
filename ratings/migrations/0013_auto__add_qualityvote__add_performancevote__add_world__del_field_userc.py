# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QualityVote'
        db.create_table(u'ratings_qualityvote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.User'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'ratings', ['QualityVote'])

        # Adding model 'PerformanceVote'
        db.create_table(u'ratings_performancevote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.User'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'ratings', ['PerformanceVote'])

        # Adding model 'World'
        db.create_table(u'ratings_world', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('world_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
        ))
        db.send_create_signal(u'ratings', ['World'])

        # Deleting field 'UserConnection.profile'
        db.delete_column(u'ratings_userconnection', 'profile_id')

        # Deleting field 'UserConnection.advice'
        db.delete_column(u'ratings_userconnection', 'advice_id')

        # Adding field 'UserConnection.world_number'
        db.add_column(u'ratings_userconnection', 'world_number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Vote.value'
        db.add_column(u'ratings_vote', 'value',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Vote.is_performance'
        db.add_column(u'ratings_vote', 'is_performance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Vote.is_submission'
        db.add_column(u'ratings_vote', 'is_submission',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'QualityVote'
        db.delete_table(u'ratings_qualityvote')

        # Deleting model 'PerformanceVote'
        db.delete_table(u'ratings_performancevote')

        # Deleting model 'World'
        db.delete_table(u'ratings_world')

        # Adding field 'UserConnection.profile'
        db.add_column(u'ratings_userconnection', 'profile',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='value', to=orm['ratings.Profile']),
                      keep_default=False)

        # Adding field 'UserConnection.advice'
        db.add_column(u'ratings_userconnection', 'advice',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='yes', to=orm['ratings.Advice']),
                      keep_default=False)

        # Deleting field 'UserConnection.world_number'
        db.delete_column(u'ratings_userconnection', 'world_number')

        # Deleting field 'Vote.value'
        db.delete_column(u'ratings_vote', 'value')

        # Deleting field 'Vote.is_performance'
        db.delete_column(u'ratings_vote', 'is_performance')

        # Deleting field 'Vote.is_submission'
        db.delete_column(u'ratings_vote', 'is_submission')


    models = {
        u'ratings.advice': {
            'Meta': {'object_name': 'Advice'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_target': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time_frame': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.performancevote': {
            'Meta': {'object_name': 'PerformanceVote'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rep': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.qualityvote': {
            'Meta': {'object_name': 'QualityVote'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.userconnection': {
            'Meta': {'object_name': 'UserConnection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.User']"}),
            'world_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.vote': {
            'Meta': {'object_name': 'Vote'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_performance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_submission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.world': {
            'Meta': {'object_name': 'World'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'world_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ratings']