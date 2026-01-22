#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectreg.settings')
django.setup()

from appreg.models import Farmer

farmers_data = [
    {'name': 'Farmer Ahmed', 'description': 'Experienced in crop cultivation and sustainable farming'},
    {'name': 'Farmer John', 'description': 'Specializes in organic farming and animal husbandry'},
    {'name': 'Farmer Mary', 'description': 'Expert in vegetable farming and market gardening'},
    {'name': 'Farmer David', 'description': 'Pioneering modern farming techniques and technology'},
]

print("Creating 4 farmers...")
for farmer_data in farmers_data:
    farmer, created = Farmer.objects.get_or_create(
        name=farmer_data['name'],
        defaults={'description': farmer_data['description']}
    )
    if created:
        print(f"✓ Created: {farmer.name}")
    else:
        print(f"✓ Already exists: {farmer.name}")

print("\n✓ All 4 farmers are ready!")
