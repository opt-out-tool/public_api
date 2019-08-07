# Generated by Django 2.2.3 on 2019-08-07 09:47

import django.contrib.postgres.fields
import src.opt_out.public_api.api.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('self_submission', models.BooleanField()),
                ('is_part_of_larger_attack', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('job', models.CharField(max_length=160)),
                ('perpetrator', models.CharField(
                    choices=[('person you know', src.opt_out.public_api.api.enums.PerpetratorType('person you know')), (
                    'multiple persons you know',
                    src.opt_out.public_api.api.enums.PerpetratorType('multiple persons you know')),
                             ('single stranger', src.opt_out.public_api.api.enums.PerpetratorType('single stranger')), (
                             'multiple strangers',
                             src.opt_out.public_api.api.enums.PerpetratorType('multiple strangers'))], max_length=40)),
                ('interaction', models.CharField(choices=[('post daily to my friends',
                                                           src.opt_out.public_api.api.enums.InteractionType(
                                                               'post daily to my friends')), ('post daily for work',
                                                                                              src.opt_out.public_api.api.enums.InteractionType(
                                                                                                  'post daily for work')),
                                                          ('post rarely for my friends',
                                                           src.opt_out.public_api.api.enums.InteractionType(
                                                               'post rarely for my friends')), ('post rarely for work',
                                                                                                src.opt_out.public_api.api.enums.InteractionType(
                                                                                                    'post rarely for work')),
                                                          ('never post',
                                                           src.opt_out.public_api.api.enums.InteractionType(
                                                               'never post'))], max_length=40)),
                ('reaction_type', models.CharField(choices=[('my behaviour has not changed',
                                                             src.opt_out.public_api.api.enums.ReactionType(
                                                                 'my behaviour has not changed')), (
                                                            'i avoid controversial topics and self-censor',
                                                            src.opt_out.public_api.api.enums.ReactionType(
                                                                'i avoid controversial topics and self-censor')), (
                                                            'i took a break from platform',
                                                            src.opt_out.public_api.api.enums.ReactionType(
                                                                'i took a break from platform')), (
                                                            'i no longer post pictures of myself',
                                                            src.opt_out.public_api.api.enums.ReactionType(
                                                                'i no longer post pictures of myself')), (
                                                            'i no longer use platform',
                                                            src.opt_out.public_api.api.enums.ReactionType(
                                                                'i no longer use platform'))], max_length=40)),
                ('experienced',
                 django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), size=None)),
                ('feeling', models.CharField(max_length=300)),
            ],
        ),
    ]
