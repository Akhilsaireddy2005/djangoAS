from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('library', '0004_auto_20200406_1053'),
    ]
    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='enrollment',
            field=models.CharField(choices=[('sdd323', 'subhi [sdd323]'), ('qq', 'sunita [qq]'), ('ee', 'sboot [ee]'), ('x', 'x [x]'), ('x', 'mloc [x]'), ('q', 'w [q]')], max_length=20),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(choices=[('123', 'rs [123]'), ('1233', 's chand [1233]'), ('1222', 'apti [1222]'), ('12338', 'j [12338]')], max_length=20),
        ),
    ]
