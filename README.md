# django-Rest-Framework-Student-Fee-Management-API

#  Student Fee Management API

A streamlined **RESTful API** built with **Django REST Framework** to manage student academic programs and fee statuses.

---

###  Key Features
* **Student Tracking**: Manage profiles, roll numbers, and payment status.
* **Automated Routing**: Uses DRF `DefaultRouter` for clean URL endpoints.
* **Interactive Docs**: Integrated **Swagger UI** and **Redoc** for real-time testing.
* **Serialization**: Robust data validation via `ModelSerializer`.

---

###  Technical Implementation
* **Models**: Defines `Program` and `Student` entities with a `ForeignKey` relationship.
* **ViewSets**: Implements `ModelViewSet` to handle CRUD logic with minimal code.
* **Admin**: Models are registered in `admin.py` for easy backend management.

---
   `python manage.py runserver`
4. **Explore**: 
   Visit `/swagger/` for interactive documentation.
