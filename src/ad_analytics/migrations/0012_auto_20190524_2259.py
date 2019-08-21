# Generated by Django 2.1.7 on 2019-05-24 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad_analytics', '0011_auto_20190522_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='ad_analytics.Company'),
        ),
        migrations.AddField(
            model_name='campaigncollaborators',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collaborators', to='ad_analytics.Company'),
        ),
        migrations.AddField(
            model_name='click',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='ad_analytics.Company'),
        ),
        migrations.AddField(
            model_name='impression',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='ad_analytics.Company'),
        ),
    ]