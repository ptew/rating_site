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
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('work', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('performance', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ratings', ['Profile'])

        # Adding model 'Advice'
        db.create_table(u'ratings_advice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('advice_text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'ratings', ['Advice'])

        # Adding model 'Connection'
        db.create_table(u'ratings_connection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Profile'])),
            ('advice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Advice'])),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_sum', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ratings', ['Connection'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'ratings_profile')

        # Deleting model 'Advice'
        db.delete_table(u'ratings_advice')

        # Deleting model 'Connection'
        db.delete_table(u'ratings_connection')


    models = {
        u'ratings.advice': {
            'Meta': {'object_name': 'Advice'},
            'advice_text': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ratings.Profile']", 'through': u"orm['ratings.Connection']", 'symmetrical': 'False'}),
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
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['ratings']