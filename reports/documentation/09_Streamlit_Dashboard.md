# Dashboard Setup

## Objective

The objective of this section is to create the folder structure required for the Streamlit dashboard.

A well-organized dashboard improves maintainability, scalability, and readability. Instead of placing all dashboard logic in a single Python file, we organize the application into reusable modules.

This modular design allows:

- Easier maintenance
- Code reusability
- Better debugging
- Separation of UI and business logic
- Easier FastAPI integration
- Easier Docker deployment

At the end of this section, the project will have a dedicated `dashboard` module that will contain all Streamlit-related code.