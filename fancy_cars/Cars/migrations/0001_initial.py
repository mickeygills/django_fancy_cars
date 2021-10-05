# Generated by Django 3.2.7 on 2021-10-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('Aston Martin', 'Aston Martin'), ('Bentley', 'Bentley'), ('Bugatti', 'Bugatti'), ('Ferrari', 'Ferrari'), ('Pagani', 'Pagani'), ('Lamborghini', 'Lamborghini'), ('McLaren', 'McLaren'), ('Mercedes AMG', 'Mercedes AMG'), ('Mercedes-Maybach', 'Mercedes-Maybach'), ('Pininfarina', 'Pininfarina'), ('Rolls Royce', 'Rolls Royce'), ('W Motors', 'W Motors')], max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('color', models.CharField(choices=[('White Metallic', 'White Metallic'), ('Black', 'Black'), ('Gray', 'Gray'), ('Blue and Silver', 'Blue and Silver'), ('Red', 'Red'), ('Gold and Green', 'Gold and Green'), ('Brown', 'Brown'), ('Orange', 'Orange')], max_length=100)),
                ('year', models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], default='2021', max_length=100)),
                ('nation_of_orign', models.CharField(choices=[('France', 'France'), ('Germany', 'Germany'), ('Italy', 'Italy'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom')], max_length=100)),
                ('horsepower', models.IntegerField(blank=True, default=0)),
                ('image', models.ImageField(blank=True, upload_to='carImages')),
                ('description', models.TextField()),
            ],
        ),
    ]