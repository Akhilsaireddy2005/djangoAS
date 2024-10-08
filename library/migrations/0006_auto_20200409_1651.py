from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('library', '0005_auto_20200407_0839'),
    ]
    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='enrollment',
            field=models.CharField(choices=[], max_length=30),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(choices=[('323', 'aptitude [323]'), ('767', 'java [767]'), ('678', 'chacha chaudhry [678]'), ('765', 'c++ [765]'), ('909', 'Python [909]'), ('34567', 'html [34567]')], max_length=30),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='branch',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='enrollment',
            field=models.CharField(max_length=40),
        ),
    ]
