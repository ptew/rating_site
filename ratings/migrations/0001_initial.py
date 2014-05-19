# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'ratings_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rep', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ratings', ['Profile'])

        # Adding model 'Advice'
        db.create_table(u'ratings_advice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ticker', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('price_target', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('time_scale', self.gf('django.db.models.fields.CharField')(default='6 months', max_length=20)),
        ))
        db.send_create_signal(u'ratings', ['Advice'])

        # Adding model 'User'
        db.create_table(u'ratings_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('participation_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'ratings', ['User'])

        # Adding model 'Vote'
        db.create_table(u'ratings_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_performance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_submission', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ratings', ['Vote'])

        # Adding model 'UserConnection'
        db.create_table(u'ratings_userconnection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.User'])),
            ('world_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ratings', ['UserConnection'])

        # Adding model 'World'
        db.create_table(u'ratings_world', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('world_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
        ))
        db.send_create_signal(u'ratings', ['World'])

        # Adding model 'Next'
        db.create_table(u'ratings_next', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('sequence_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ratings', ['Next'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'ratings_profile')

        # Deleting model 'Advice'
        db.delete_table(u'ratings_advice')

        # Deleting model 'User'
        db.delete_table(u'ratings_user')

        # Deleting model 'Vote'
        db.delete_table(u'ratings_vote')

        # Deleting model 'UserConnection'
        db.delete_table(u'ratings_userconnection')

        # Deleting model 'World'
        db.delete_table(u'ratings_world')

        # Deleting model 'Next'
        db.delete_table(u'ratings_next')


    models = {
        u'ratings.advice': {
            'Meta': {'object_name': 'Advice'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_target': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time_scale': ('django.db.models.fields.CharField', [], {'default': "'6 months'", 'max_length': '20'})
        },
        u'ratings.next': {
            'Meta': {'object_name': 'Next'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ratings.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rep': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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