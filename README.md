Lyft Car Service

This is a Python module for managing vehicle service checks for a ridesharing company like Lyft. It implements a service check system using the abstract base class and inheritance patterns.

Features
Defines abstract base classes for engines, batteries, and overall vehicle serviceability
Implements concrete engine classes for different manufacturers with different service intervals
Implements concrete battery classes with time and mileage based service intervals
Allows creating vehicle objects composed of different engines and batteries
Encapsulates service check logic in the vehicle class
Includes a factory class to easily create configured vehicle instances.

Getting Started
The module depends on the Python datetime module. 


Why This Module
This code structures vehicle service checks to allow easily adding new vehicle types and customizing service intervals. Both time and mileage based intervals are supported.

Key advantages:

Single responsibility classes make the code modular and testable
The factory creates pre-configured vehicle instances
Additional vehicle types can be added by simply implementing new engine/battery classes.

Premodeled example
The included premodeled example code shows creating two types of vehicles with custom engines and batteries. It checks if service is due on each based on mileage and time since last service.

This allows flexibly configuring service parameters for different vehicle makes & models.

