# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LabMember.date_added'
        db.add_column(u'lab_members_labmember', 'date_added',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2014, 8, 9, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'LabMember.last_updated'
        db.add_column(u'lab_members_labmember', 'last_updated',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'LabMember.trainee_type'
        db.alter_column(u'lab_members_labmember', 'trainee_type', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Deleting field 'LabMember.date_added'
        db.delete_column(u'lab_members_labmember', 'date_added')

        # Deleting field 'LabMember.last_updated'
        db.delete_column(u'lab_members_labmember', 'last_updated')


        # Changing field 'LabMember.trainee_type'
        db.alter_column(u'lab_members_labmember', 'trainee_type', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'lab_members.labmember': {
            'Meta': {'object_name': 'LabMember'},
            'current_position': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trainee_type': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['lab_members']