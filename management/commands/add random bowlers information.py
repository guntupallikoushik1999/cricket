from bowlers.models import Bowler
from faker import Faker
import random

fake = Faker()

countries = ["India", "Australia", "England", "Pakistan", "South Africa", "New Zealand", "Sri Lanka", "Bangladesh"]

for _ in range(100):  # Add 30 bowlers
    Bowler.objects.create(
        name=fake.name(),
        age=random.randint(19, 39),
        country=random.choice(countries),
        wickets_taken=random.randint(0, 500),
        bowling_average=round(random.uniform(15.0, 45.0), 2),
        bowling_strikerate=round(random.uniform(20.0, 60.0), 2),
        economy_rate=round(random.uniform(3.0, 7.0), 2)
    )
"""
to run this code, you need to have Django and Faker installed in your environment.
go to the root directory of your Django project and run the following command:
python manage.py shell < cricket/management/add_random_bowlers_information.py
or You can run this script using Django's shell command: python manage.py shell
```bash
paste the code into the shell and press Enter.
quit()
"""