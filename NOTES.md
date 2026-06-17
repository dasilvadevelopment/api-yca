# YCA Learning Notes

---

**Q: Next.js App Router or Pages Router?**
The folder + `index.tsx` + `[id].tsx` pattern is Pages Router. App Router is the newer default — uses an `app/` folder with `page.tsx` files. Components are server components by default and can fetch data directly. Use `"use client"` to opt into client-side behavior.

---

**Q: What auth options are there for DRF?**
- Session auth — good if frontend and backend are on the same domain
- Token auth — DRF has built-in, but community standard is JWT via `djangorestframework-simplejwt`. Better for Next.js + DRF since they run on different ports/domains.

---

**Q: Can I bulk download all cards from YGOPRODeck?**
Yes, there is an endpoint that returns every card in one shot. Good approach: store card ID and name locally, fetch full details on demand.

---

**Q: How do I make a "insert if not exists" operation in Django?**
Use `get_or_create` on Django querysets. Pair this with a management command (`python manage.py sync_cards`) for bulk operations like syncing cards from an external API.

---

**Q: How do I enforce that a combination of fields is unique in Django?**
Define a `UniqueConstraint` (or older `unique_together`) inside the model's `Meta` class.

---

**Q: How do I create a virtual environment?**
`python -m venv .venv` — then activate it. Activation command differs between PowerShell and bash.

---

**Q: How do I install Django REST Framework?**
`pip install djangorestframework` — then add `'rest_framework'` to `INSTALLED_APPS` in `settings.py`.

---

**Q: How do I create a Django project?**
`django-admin startproject <projectname> .` — the `.` puts project files in the current directory instead of a nested folder.

---

**Q: How do I install and configure CORS headers?**
`pip install django-cors-headers` — add to `INSTALLED_APPS` and add its middleware as high as possible in `MIDDLEWARE`, just above `CommonMiddleware`.

---

**Q: How do I create a Django app?**
`python manage.py startapp <appname>` — convention is lowercase, underscores for multi-word names.

---

**Q: How do I rename a Django project?**
Rename the project folder, then find and replace the old name in `settings.py`, `wsgi.py`, `asgi.py`, and `manage.py`.

---

**Q: Should I use one app or two for YGO and MTG cards?**
Two apps — the game-specific terminology (DEF vs toughness, ATK vs power, etc.) differs enough that sharing one app would cause friction all the way through to the frontend. Use a `common` app for a shared abstract base model.

---

**Q: What is the Django equivalent of a C# abstract class for models?**
Abstract model inheritance — define a base model and set `abstract = True` in its `Meta` class. Django won't create a table for it, but child models inherit all its fields.

---

**Q: How do I reference a model from another app in a ForeignKey?**
Use a string instead of the class directly: `models.ForeignKey('appname.ModelName', ...)` — avoids import issues.

---

**Q: What is the top-right icon in YGO (LIGHT/DARK/EARTH etc.) called?**
That is the **attribute**. Monster type (Spellcaster, Dragon, Synchro) is separate. Archetype refers to a card's in-game series (Blue-Eyes, Eldlich, etc.).

---

**Q: How do I make a field optional in Django?**
Add `null=True, blank=True` to the field.
- `null=True` — database level, allows NULL in the column
- `blank=True` — validation level, allows empty values in forms/serializers
Both are needed together for FK fields.

---

**Q: What are serializers in DRF?**
Serializers convert model instances to JSON (and back). `ModelSerializer` is the standard starting point — it maps directly to a model. Import with `from rest_framework import serializers` and inherit from `serializers.ModelSerializer`. Requires a `Meta` class with `model` and `fields`.

---

**Q: How do I include the actual related values instead of just IDs in a serializer?**
Add `depth = 1` to the `Meta` class. DRF will expand FK relationships one level deep, returning the full related object as a nested dict instead of just an ID.

---

**Q: What is ModelViewSet and why use it over ViewSet?**
`ModelViewSet` automatically provides `list`, `retrieve`, `create`, `update`, and `destroy` — no need to write any methods manually. Just set `queryset` and `serializer_class` as class attributes. The HTTP method determines the action (GET = list/retrieve, POST = create, etc.).

---

**Q: How do I set up URLs for a ModelViewSet?**
Use `DefaultRouter` from `rest_framework.routers`. Create a router instance, call `router.register('prefix', ViewSet)`, then include `router.urls` in `urlpatterns`. Prefix the whole thing with `api/` using `include()`.

---

**Q: When do I run migrations?**
After all apps are added to `INSTALLED_APPS` in `settings.py`. Run `python manage.py makemigrations` first to generate migration files, then `python manage.py migrate` to apply them to the database.

---
