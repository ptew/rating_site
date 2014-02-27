# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserConnection'
        db.create_table(u'ratings_userconnection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.User'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
        ))
        db.send_create_signal(u'ratings', ['UserConnection'])

        # Deleting field 'User.view_count'
        db.delete_column(u'ratings_user', 'view_count')

        # Deleting field 'User.vote_count'
        db.delete_column(u'ratings_user', 'vote_count')

        # Deleting field 'Profile.vote_count'
        db.delete_column(u'ratings_profile', 'vote_count')

        # Deleting field 'Advice.vote_count'
        db.delete_column(u'ratings_advice', 'vote_count')

        # Deleting field 'Advice.view_count'
        db.delete_column(u'ratings_advice', 'view_count')


    def backwards(self, orm):
        # Deleting model 'UserConnection'
        db.delete_table(u'ratings_userconnection')

        # Adding field 'User.view_count'
        db.add_column(u'ratings_user', 'view_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.vote_count'
        db.add_column(u'ratings_user', 'vote_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profile.vote_count'
        db.add_column(u'ratings_profile', 'vote_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Advice.vote_count'
        db.add_column(u'ratings_advice', 'vote_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Advice.view_count'
        db.add_column(u'ratings_advice', 'view_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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
        u'ratings.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rep': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.userconnection': {
            'Meta': {'object_name': 'UserConnection'},
            'advice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Advice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.Profile']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ratings.User']"})
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