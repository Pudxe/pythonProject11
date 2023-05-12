# Generated by Django 4.1.7 on 2023-04-22 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("goals", "0003_create_new_objects"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="categories",
                to="goals.board",
                verbose_name="Board",
            ),
        ),
        migrations.AlterField(
            model_name="participant",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="participants",
                to="goals.board",
                verbose_name="Board",
            ),
        ),
        migrations.AlterField(
            model_name="participant",
            name="role",
            field=models.SmallIntegerField(
                choices=[(1, "Owner"), (2, "Writer"), (3, "Reader")],
                default=1,
                verbose_name="Role",
            ),
        ),
    ]
