# Generated by Django 3.2 on 2022-12-25 16:56

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20221223_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('activep', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('commonclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.commonclass')),
                ('adr', models.CharField(max_length=500)),
                ('est_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'college',
            },
            bases=('app1.commonclass',),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('commonclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.commonclass')),
                ('dept_str', models.IntegerField()),
                ('College', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.college')),
            ],
            options={
                'db_table': 'dept',
            },
            bases=('app1.commonclass',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('commonclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.commonclass')),
                ('marks', models.IntegerField()),
                ('age', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
            ],
            options={
                'db_table': 'student',
            },
            bases=('app1.commonclass',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('commonclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.commonclass')),
                ('is_practical', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
                ('student', models.ManyToManyField(to='app1.Student')),
            ],
            options={
                'db_table': 'subject',
            },
            bases=('app1.commonclass',),
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('commonclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.commonclass')),
                ('exp', models.FloatField()),
                ('qual', models.CharField(max_length=50)),
                ('College', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.college')),
            ],
            options={
                'db_table': 'principal',
            },
            bases=('app1.commonclass',),
        ),
    ]
