# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    forwards_data = {
        "plein": "0",
        "partiel": "1",
        "part": "3",
        "soir": "2",
        "ecole": "4",
        "vacances": "5",
        "decal": "6",
        "nuit": "7",
        "urgences": "8",
    }
    backwards_data = {
        "0": "plein",
        "1": "partiel",
        "3": "part",
        "2": "soir",
        "4": "ecole",
        "5": "vacances",
        "6": "decal",
        "7": "nuit",
        "8": "urgences",
    }

    @staticmethod
    def _convert_obj_field(obj, data):
        if obj.type_garde:
            obj.type_garde = data.get(obj.type_garde)
            obj.save()

    def forwards(self, orm):
        Famille = orm["famille.Famille"]
        Prestataire = orm["famille.Prestataire"]
        for o in Famille.objects.all():
            self._convert_obj_field(o, self.forwards_data)
        for o in Prestataire.objects.all():
            self._convert_obj_field(o, self.forwards_data)

    def backwards(self, orm):
        Famille = orm["Famille"]
        Prestataire = orm["Prestataire"]
        for o in Famille.objects.all():
            self._convert_obj_field(o, self.backwards_data)
        for o in Prestataire.objects.all():
            self._convert_obj_field(o, self.backwards_data)

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'famille.downloadablefile': {
            'Meta': {'object_name': 'DownloadableFile'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'file_content': ('famille.utils.fields.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'famille.enfant': {
            'Meta': {'object_name': 'Enfant'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'e_birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'birthday'", 'blank': 'True'}),
            'e_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'name'"}),
            'e_school': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'school'", 'blank': 'True'}),
            'famille': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enfants'", 'to': "orm['famille.Famille']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'famille.famille': {
            'Meta': {'object_name': 'Famille'},
            'animaux': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'France'", 'max_length': '20', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'devoirs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diploma': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'enfant_malade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'experience_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'experience_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'geolocation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['famille.Geolocation']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipn': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ipn.PayPalIPN']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'is_test': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'menage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'non_fumeur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'plan': ('django.db.models.fields.CharField', [], {'default': "'basic'", 'max_length': '20', 'blank': 'True'}),
            'plan_expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('famille.utils.fields.ContentTypeRestrictedFileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'psc1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'repassage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'studies': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tarif': ('django.db.models.fields.CharField', [], {'default': "'3,20'", 'max_length': '10', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tel_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'type_attente_famille': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'type_garde': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type_presta': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'visibility_family': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'visibility_global': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'visibility_prestataire': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'famille.famillefavorite': {
            'Meta': {'object_name': 'FamilleFavorite'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'famille': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'favorites'", 'to': "orm['famille.Famille']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'famille.familleplanning': {
            'Meta': {'object_name': 'FamillePlanning'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'famille': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planning'", 'to': "orm['famille.Famille']"}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['famille.Schedule']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weekday': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['famille.Weekday']", 'symmetrical': 'False'})
        },
        'famille.familleratings': {
            'Meta': {'object_name': 'FamilleRatings'},
            'amability': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ponctuality': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'reliability': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'serious': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': "orm['famille.Famille']"})
        },
        'famille.geolocation': {
            'Meta': {'object_name': 'Geolocation'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'has_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'famille.prestataire': {
            'Meta': {'object_name': 'Prestataire'},
            'animaux': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'France'", 'max_length': '20', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'devoirs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diploma': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'enfant_malade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'experience_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'experience_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'geolocation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['famille.Geolocation']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipn': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ipn.PayPalIPN']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'is_test': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'menage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'non_fumeur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'permis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'plan': ('django.db.models.fields.CharField', [], {'default': "'basic'", 'max_length': '20', 'blank': 'True'}),
            'plan_expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'profile_pic': ('famille.utils.fields.ContentTypeRestrictedFileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'psc1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'repassage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resume': ('famille.utils.fields.ContentTypeRestrictedFileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'studies': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tarif': ('django.db.models.fields.CharField', [], {'default': "'3,20'", 'max_length': '10', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tel_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'type_garde': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'visibility_family': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'visibility_global': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'visibility_prestataire': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'famille.prestatairefavorite': {
            'Meta': {'object_name': 'PrestataireFavorite'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'prestataire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'favorites'", 'to': "orm['famille.Prestataire']"}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'famille.prestataireplanning': {
            'Meta': {'object_name': 'PrestatairePlanning'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prestataire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planning'", 'to': "orm['famille.Prestataire']"}),
            'schedule': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['famille.Schedule']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weekday': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['famille.Weekday']", 'symmetrical': 'False'})
        },
        'famille.prestataireratings': {
            'Meta': {'object_name': 'PrestataireRatings'},
            'amability': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ponctuality': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'reliability': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'serious': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': "orm['famille.Prestataire']"})
        },
        'famille.reference': {
            'Meta': {'object_name': 'Reference'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'garde': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'missions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'prestataire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'references'", 'to': "orm['famille.Prestataire']"}),
            'referenced_user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'reference_of'", 'unique': 'True', 'null': 'True', 'to': "orm['famille.Famille']"}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'famille.schedule': {
            'Meta': {'object_name': 'Schedule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'famille.weekday': {
            'Meta': {'object_name': 'Weekday'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'ipn.paypalipn': {
            'Meta': {'object_name': 'PayPalIPN', 'db_table': "u'paypal_ipn'"},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'address_country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'address_country_code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'address_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'address_status': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_zip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount1': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount2': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount3': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'amount_per_cycle': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'auction_buyer_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'auction_closing_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'auction_multi_item': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'auth_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'auth_exp': ('django.db.models.fields.CharField', [], {'max_length': '28', 'blank': 'True'}),
            'auth_id': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'auth_status': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'business': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'case_creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'case_id': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'case_type': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'charset': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency_code': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '32', 'blank': 'True'}),
            'custom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'exchange_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '16', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flag_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'flag_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'for_auction': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'from_view': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'handling_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_payment_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'invoice': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'mc_amount1': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_amount2': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_amount3': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '32', 'blank': 'True'}),
            'mc_fee': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_gross': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_handling': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'mc_shipping': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'next_payment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'notify_version': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'num_cart_items': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'option_name1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'option_name2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'outstanding_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'parent_txn_id': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'payer_business_name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'payer_email': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'payer_id': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'payer_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'payment_cycle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'payment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'payment_gross': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'max_length': '17', 'blank': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'pending_reason': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'period1': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'period2': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'period3': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'period_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'profile_status': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'protection_eligibility': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reason_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'reattempt': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'receipt_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'receiver_email': ('django.db.models.fields.EmailField', [], {'max_length': '127', 'blank': 'True'}),
            'receiver_id': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'recur_times': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'recurring': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'recurring_payment_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'remaining_settle': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'residence_country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'retry_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rp_invoice_id': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'settle_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'settle_currency': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'shipping': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscr_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'subscr_effective': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'subscr_id': ('django.db.models.fields.CharField', [], {'max_length': '19', 'blank': 'True'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'test_ipn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_entity': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'transaction_subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'txn_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '19', 'blank': 'True'}),
            'txn_type': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'verify_sign': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['famille']
    symmetrical = True
