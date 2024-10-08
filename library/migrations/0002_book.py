from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('library', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biographie'), ('history', 'History')], default='education', max_length=30)),
            ],
        ),
    ]
