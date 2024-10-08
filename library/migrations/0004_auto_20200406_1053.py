from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('library', '0003_issuedbook'),
    ]
    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='enrollment',
            field=models.CharField(choices=[('sdd323', '<bound method StudentExtra.get_name of <StudentExtra: subhi>> sdd323'), ('qq', '<bound method StudentExtra.get_name of <StudentExtra: sunita>> qq'), ('ee', '<bound method StudentExtra.get_name of <StudentExtra: sboot>> ee'), ('x', '<bound method StudentExtra.get_name of <StudentExtra: x>> x'), ('x', '<bound method StudentExtra.get_name of <StudentExtra: mloc>> x'), ('q', '<bound method StudentExtra.get_name of <StudentExtra: q>> q')], max_length=20),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(choices=[(123, 'rs 123'), (1233, 's chand 1233'), (1222, 'apti 1222')], max_length=20),
        ),
    ]
