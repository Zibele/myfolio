# Generated by Django 3.1.4 on 2021-01-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_folio_app', '0005_skill_display_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_svg',
            new_name='skill_svg_large',
        ),
        migrations.RenameField(
            model_name='techstack',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='techstack',
            old_name='skill_id',
            new_name='skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_svg_small',
            field=models.TextField(null=True),
        ),
    ]