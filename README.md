# Django Signals - Rectangle Area Calculation  

## Overview  
This project demonstrates how to use *Django signals* to automatically calculate the *area of a rectangle* when a model instance is created or updated.  

## Steps to Run  

1. *Clone the Repository*  
   ```sh
   git clone <your-repo-url>
   cd <your-project-folder>

2. Setup Virtual Environment & Install Dependencies

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
pip install -r requirements.txt


3. Run Migrations & Start Server

python manage.py migrate  
python manage.py runserver


4. Test in Django Shell

python manage.py shell

Create a Rectangle

from myapp.models import Rectangle  
rect = Rectangle.objects.create(length=5, width=3)  
print(rect.area)  # Output: 15




Expected Output

The area of the rectangle is automatically calculated and stored when a new instance is created.


Files Modified

models.py → Defines the Rectangle model

signals.py → Implements the signal for automatic area calculation

apps.py → Connects signals to the app



---
