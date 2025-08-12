<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>📝 Online Exam Management System</h1>
  <p>This Django-based project allows users to create and manage online exams, including multiple-choice and descriptive questions. It features user roles, profile management, secure authentication, and full API documentation.</p>

  <h2>🚀 Setup Instructions</h2>
  <ol>
    <li>Clone repo: <code>git clone https://github.com/Amin-Bajelan/System_online_exam_Django_CBV</code></li>
    <li>Install packages: <code>pip install -r requirements.txt</code></li>
    <li>Run migrations: <code>python manage.py migrate</code></li>
    <li>Start server: <code>python manage.py runserver</code></li>
    <h3>And for Docker setup</h3>
    <li>Build Docker image: <code>docker-compose build</code></li>
    <li>Run container: <code>docker-compose up -d</code></li>
    <li>Apply migrations inside container: <code>docker-compose exec backend python manage.py migrate</code></li>
    <li>And them for carete super user: <code>docker-compose exec container_name python manage.py createsuperuser</code></li>
   
  </ol>

  <h2>👨‍🏫 Professor Features</h2>
  <ul>
    <li>Create exams with multiple-choice or descriptive questions</li>
    <li>View student submissions and see who participated</li>
    <li>Assign scores to students</li>
    <li>Edit or delete exams and questions</li>
    <li>Perform full CRUD operations on exams and questions</li>
  </ul>

  <h2>🎓 Student Features</h2>
  <ul>
    <li>Register and create a personal profile</li>
    <li>Change password after registration</li>
    <li>Access exams assigned by professors</li>
    <li>Participate in exams during the valid time window</li>
    <li>View submitted answers and received scores</li>
  </ul>

  <h2>🔐 Authentication & API Access</h2>
  <ul>
    <li>JWT-based authentication for secure access</li>
    <li>Dedicated APIs for superusers and professors</li>
    <li>Full CRUD support for exams and questions via RESTful endpoints</li>
    <li>Swagger integration for interactive API documentation</li>
  </ul>

  <h2>🐳 Docker Integration</h2>
  <ul>
    <li>Fully Dockerized for easy setup and deployment</li>
    <li>Includes Dockerfiles and docker-compose configuration</li>
    <li>Supports local development and production environments</li>
  </ul>

  <h2>👨‍💻 Developer</h2>
  <p>Created by <strong>Mohamad Amin Bajelan</strong>. For collaboration or questions, feel free to reach out or visit the GitHub repository.</p>
</body>
</html>
