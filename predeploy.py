import os, sys, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beckend.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.db import connection
from django.db.migrations.recorder import MigrationRecorder

recorder = MigrationRecorder(connection)

target = ('fronend', '0029_payment_and_more')
if not recorder.migration_qs.filter(app='fronend', name='0029_payment_and_more').exists():
    recorder.record_applied('fronend', '0029_payment_and_more')
    print('Faked migration: fronend.0029_payment_and_more')
else:
    print('Migration already applied: fronend.0029_payment_and_more')
