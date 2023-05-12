# Generated by Django 4.1.7 on 2023-04-28 10:21

from django.db import migrations, models, transaction


def set_defaults(apps, schema_editor):
    TgUser = apps.get_model('bot', 'TgUser')

    with transaction.atomic():
        for tg_user in TgUser.objects.all():
            if tg_user.user is not None:
                tg_user.bot_state = 2
                tg_user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0004_tguser_bot_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tguser",
            name="bot_state",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Added"),
                    (2, "Confirmed"),
                    (3, "Wait Category"),
                    (4, "Wait Title"),
                    (5, "Canceled"),
                ],
                default=1,
                verbose_name="Bot State",
            ),
        ),
        migrations.RunPython(set_defaults),
    ]
