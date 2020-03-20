# Generated by Django 3.0.1 on 2020-03-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthplanportal', '0006_auto_20200319_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthplan',
            name='Diagnostic_test_lab_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Diagnostic_test_xray_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Durable_medical_eqiupment_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Emergency_medical_transportation_HospitalStay_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Emergency_medical_transportation_IMA_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Emergency_room_care_Hospital_Stay_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Emergency_room_care_IMA_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Facility_fee_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Generic_drugs_pescrciption_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Home_health_care_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Imaging_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Inpatient_services_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Outpatient_services_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Physician_surgeon_fee_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Preffered_drugs_pescrciption_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Pregnant_childbirth_delivery_facility_services_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Pregnant_childbirth_delivery_professional_services_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Pregnant_office_visit_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Primary_care_visit_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Rehabilitation_services_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Skilled_nursing_care_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Specialist_visit_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AddField(
            model_name='healthplan',
            name='Urgent_care_IMA_Percentage',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Diagnostic_test_lab',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Diagnostic_test_xray',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Durable_medical_eqiupment',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_medical_transportation_HospitalStay',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_medical_transportation_IMA',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_room_care_Hospital_Stay',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Emergency_room_care_IMA',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Facility_fee',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Generic_drugs_pescrciption',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Home_health_care',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Imaging',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Inpatient_services',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Out_of_pocket_limit_family',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Out_of_pocket_limit_person',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Outpatient_services',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Overall_deductible_family',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Overall_deductible_person',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Physician_surgeon_fee',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Preffered_drugs_pescrciption',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Pregnant_childbirth_delivery_facility_services',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Pregnant_childbirth_delivery_professional_services',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Pregnant_office_visit',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Primary_care_visit',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Rehabilitation_services',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Skilled_nursing_care',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Specialist_visit',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='healthplan',
            name='Urgent_care_IMA',
            field=models.IntegerField(blank=True, default=-1),
        ),
    ]
