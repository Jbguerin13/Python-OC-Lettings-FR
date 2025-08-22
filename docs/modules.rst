Modules
=======

This section covers the modules used in the OC Lettings Site.

Lettings Module
---------------

The Lettings module manages all property listings in the OC Lettings Site application.

**Property Structure:**
Properties (lettings) are grouped by houses and include:
- **Title**: The name or description of the property
- **Address**: Complete address information including:
  - **Number**: Street number (1-9999)
  - **Street**: Street name
  - **City**: City name
  - **State**: State abbreviation (2 characters)
  - **Zip Code**: Postal code (1-99999)
  - **Country**: Country ISO code (3 characters)

**Technical Implementation:**
The module consists of two main models:
- **Address Model**: Stores complete address information with validation
- **Letting Model**: Represents a property listing linked to an address through a OneToOneField

**Key Features:**
- Property Management: Centralized property listing management
- Address Validation: Comprehensive address validation with constraints
- Data Integrity: One-to-one relationship between properties and addresses
- Admin Interface: Full admin panel integration for property and address management

**Use Cases:**
- Property Listings: Displaying available properties for rent
- Address Management: Managing property addresses with validation
- Property Search: Finding properties by location, city, or country
- Admin Management: Managing properties and addresses through Django admin

.. automodule:: lettings
   :members:
   :undoc-members:
   :show-inheritance:

Profiles Module
---------------

The Profiles module manages all user profiles in the OC Lettings Site application.

**User Profile Structure:**
Each user profile contains the following information:
- **First Name & Last Name**: Retrieved from the associated Django User model
- **Email**: Retrieved from the associated Django User model  
- **Favorite City**: A custom field specific to the Profile model

**Technical Implementation:**
The Profile model extends the default Django User model through a OneToOneField relationship, ensuring:
- Each user can have exactly one profile
- Each profile belongs to exactly one user
- The profile inherits all user information (first name, last name, email, username, etc.)
- Additional custom data (favorite city) is stored in the Profile model

**Key Features:**
- User Management: Centralized user information management
- Profile Extension: Custom profile data without modifying the core User model
- Data Integrity: One-to-one relationship ensures data consistency
- Admin Interface: Full admin panel integration for profile management

**Use Cases:**
- User Registration: Creating new user accounts with profile information
- Profile Display: Showing user information on profile pages
- User Preferences: Storing user-specific data like favorite cities
- Admin Management: Managing users and profiles through Django admin

.. automodule:: profiles
   :members:
   :undoc-members:
   :show-inheritance: