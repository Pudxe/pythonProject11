# Generated by Django 4.1.7 on 2023-04-28 09:59

from django.db import migrations, models, transaction


def set_defaults(apps, schema_editor):
    TgUser = apps.get_model('bot', 'TgUser')

    with transaction.atomic():
        for tg_user in TgUser.objects.all():
            if tg_user.user is not None:
                tg_user.bot_state = 3
                tg_user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0003_rename_telegram_chat_id_tguser_tg_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tguser",
            name="bot_state",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Initial"),
                    (2, "Added"),
                    (3, "Confirmed"),
                    (4, "Wait Category"),
                    (5, "Wait Title"),
                    (6, "Canceled"),
                ],
                default=1,
                verbose_name="Bot State",
            ),
        ),
        migrations.RunPython(set_defaults),
    ]