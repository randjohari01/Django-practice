from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ("news", "0009_publication_alter_article_options_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="person",      # the old class name you had
            new_name="personshirt", # your current class name
        ),
    ]
