Database Schema
===============

This document describes the table layout and database structure of the OC Lettings Site project.

Main Tables
-----------

Table: lettings_address
~~~~~~~~~~~~~~~~~~~~~~~

This table stores property address information.

+----------------+------------------+------------------+------------------+
| Field          | Type             | Constraints      | Description      |
+================+==================+==================+==================+
| id             | Integer          | Primary Key      | Unique identifier|
|                |                  | Auto-increment   |                  |
+----------------+------------------+------------------+------------------+
| number         | PositiveInteger  | 1-9999          | Street number    |
+----------------+------------------+------------------+------------------+
| street         | CharField        | max_length=64    | Street name      |
+----------------+------------------+------------------+------------------+
| city           | CharField        | max_length=64    | City name        |
+----------------+------------------+------------------+------------------+
| state          | CharField        | max_length=2     | State code       |
|                |                  | min_length=2     | (2 characters)   |
+----------------+------------------+------------------+------------------+
| zip_code       | PositiveInteger  | 1-99999         | Postal code      |
+----------------+------------------+------------------+------------------+
| country_iso_code| CharField       | max_length=3     | ISO country code |
|                |                  | min_length=3     | (3 characters)   |
+----------------+------------------+------------------+------------------+

**Constraints:**
- `number`: Must be between 1 and 9999
- `state`: Must have exactly 2 characters
- `zip_code`: Must be between 1 and 99999
- `country_iso_code`: Must have exactly 3 characters

Table: lettings_letting
~~~~~~~~~~~~~~~~~~~~~~~

This table stores rental property information.

+----------------+------------------+------------------+------------------+
| Field          | Type             | Constraints      | Description      |
+================+==================+==================+==================+
| id             | Integer          | Primary Key      | Unique identifier|
|                |                  | Auto-increment   |                  |
+----------------+------------------+------------------+------------------+
| title          | CharField        | max_length=256   | Property title   |
+----------------+------------------+------------------+------------------+
| address_id     | Integer          | Foreign Key      | Reference to     |
|                |                  | OneToOneField    | the address      |
+----------------+------------------+------------------+------------------+

**Relationships:**
- One-to-One relationship with `lettings_address` via `address_id`

Table: profiles_profile
~~~~~~~~~~~~~~~~~~~~~~~

This table stores extended user profiles.

+----------------+------------------+------------------+------------------+
| Field          | Type             | Constraints      | Description      |
+================+==================+==================+==================+
| id             | Integer          | Primary Key      | Unique identifier|
|                |                  | Auto-increment   |                  |
+----------------+------------------+------------------+------------------+
| user_id        | Integer          | Foreign Key      | Reference to     |
|                |                  | OneToOneField    | the user         |
+----------------+------------------+------------------+------------------+
| favorite_city  | CharField        | max_length=64    | User's favorite  |
|                |                  | blank=True       | city             |
+----------------+------------------+------------------+------------------+

**Relationships:**
- One-to-One relationship with `auth_user` (Django default table) via `user_id`

Table: auth_user (Django default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table is managed by Django and stores basic user information.

+----------------+------------------+------------------+------------------+
| Field          | Type             | Constraints      | Description      |
+================+==================+==================+==================+
| id             | Integer          | Primary Key      | Unique identifier|
|                |                  | Auto-increment   |                  |
+----------------+------------------+------------------+------------------+
| username       | CharField        | max_length=150   | Username         |
|                |                  | unique           |                  |
+----------------+------------------+------------------+------------------+
| first_name     | CharField        | max_length=150   | First name       |
+----------------+------------------+------------------+------------------+
| last_name      | CharField        | max_length=150   | Last name        |
+----------------+------------------+------------------+------------------+
| email          | CharField        | max_length=254   | Email address    |
+----------------+------------------+------------------+------------------+
| password       | CharField        | max_length=128   | Hashed password  |
+----------------+------------------+------------------+------------------+
| is_active      | Boolean          | default=True     | Active account   |
+----------------+------------------+------------------+------------------+
| date_joined    | DateTimeField    | auto_now_add     | Registration date|
+----------------+------------------+------------------+------------------+

Relationship Diagram
--------------------

.. code-block:: text

    auth_user (1) ←→ (1) profiles_profile
         ↑
         |
         | (1)
         ↓
    lettings_letting (1) ←→ (1) lettings_address

**Relationship explanations:**

1. **auth_user ↔ profiles_profile**: One-to-One relationship
   - Each user can have only one profile
   - Each profile belongs to only one user

2. **auth_user → lettings_letting**: One-to-Many relationship (via admin)
   - Users can create/manage multiple properties
   - Each property can be managed by a user

3. **lettings_letting ↔ lettings_address**: One-to-One relationship
   - Each property has only one address
   - Each address corresponds to only one property

Constraints and Validation
-------------------------

**Data validation:**
- All required fields are defined with `null=False` (default)
- Numeric fields use validators for value ranges
- Text fields have defined maximum lengths
- Relationships are protected by foreign key constraints

**Referential integrity:**
- Cascade deletion for One-to-One relationships
- Protection against deletion of users with active profiles
- Protection against deletion of addresses with active properties
