from django.db import migrations, models
import library.models
class Migration(migrations.Migration):
    dependencies = [
        ('library', '0002_book'),
    ]
    operations = [
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment', models.CharField(choices=[('sdd323', 'sdd323 <bound method StudentExtra.get_name of <StudentExtra: subhi>>'), ('qq', 'qq <bound method StudentExtra.get_name of <StudentExtra: sunita>>'), ('ee', 'ee <bound method StudentExtra.get_name of <StudentExtra: sboot>>'), ('x', 'x <bound method StudentExtra.get_name of <StudentExtra: x>>'), ('x', 'x <bound method StudentExtra.get_name of <StudentExtra: mloc>>'), ('q', 'q <bound method StudentExtra.get_name of <StudentExtra: q>>')], max_length=20)),
                ('isbn', models.CharField(choices=[(123, 123), (1233, 1233), (1222, 1222)], max_length=20)),
                ('issuedate', models.DateField(auto_now=True)),
                ('expirydate', models.DateField(default=library.models.get_expiry)),
            ],
        ),
    ]
