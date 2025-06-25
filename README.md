# IPO Portal

A Django-based web application for managing and viewing Initial Public Offerings (IPOs), company details, and related documents. The portal supports both admin and public views, with secure authentication and document management features.

## Features

- User registration, login, and admin approval workflow
- Admin dashboard for managing companies, IPOs, and documents
- CRUD operations for Companies, IPOs, and Documents
- Upload and download RHP and DRHP PDF documents for each IPO
- Public IPO list and detail pages with search and filter
- REST API endpoints for Companies, IPOs, and Documents
- Bootstrap-styled responsive UI

## Project Structure

```
intership project/
  ├── ipo/                # Main Django app
  ├── ipo_portal/         # Project settings and configuration
  ├── media/              # Uploaded files (e.g., company logos, PDFs)
  ├── staticfiles/        # Static assets (CSS, JS, images)
  ├── manage.py           # Django management script
  └── requirements.txt    # Python dependencies
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the application:**
   - Admin: `http://127.0.0.1:8000/admin/`
   - Main site: `http://127.0.0.1:8000/`

## Usage

- Register as a new user and wait for admin approval.
- Admins can manage companies, IPOs, and documents from the dashboard.
- Upload RHP and DRHP PDFs for each IPO.
- Public users can view IPO lists and details, and download available documents.

## API Endpoints

- `/api/companies/` — List, create, update, delete companies
- `/api/ipos/` — List, create, update, delete IPOs
- `/api/documents/` — List, create, update, delete documents

## Contribution Guidelines

1. Fork the repository and create your branch from `main`.
2. Commit your changes with clear messages.
3. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License.

---

**Note:** For production use, configure environment variables, static/media file handling, and security settings as needed. 
