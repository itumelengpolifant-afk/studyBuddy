# Study Buddy

Study Buddy is a web application that helps students organise study groups: scheduling sessions, voting on times, recording attendance, sharing notes and chatting in one place. It is built for students, group owners, tutors and administrators at a learning institution.


**Learner:** Itumeleng Precious Olifant · **Student number:** BCS/SD/10225 · **Supervisor:** Mr Jeff

## Problem

Students usually organise study groups through scattered chat messages, which makes it hard to agree on a time, track who attends and keep notes in one place. Study Buddy gives each group a single place to schedule sessions, vote on times, take attendance, share notes and communicate, with reports so group owners and administrators can see participation.

## Features

- Register and log in with role-based access
- Create modules and study groups, and join a group with a join code
- Schedule study sessions with a venue, date and time
- Vote on proposed time slots for a session
- Record attendance for each session
- Upload and share notes within a group
- Group chat messages
- Notifications for group activity
- Attendance and participation reports

## User Roles

| Role | What they can do |
| --- | --- |
| Administrator | Manage users, modules and groups; view system-wide reports  |
| Group Owner | Create and manage a group, schedule sessions, manage members, take attendance, view group reports |
| Student | Join groups, vote on session times, view sessions, upload notes, chat, view own attendance |
| Tutor (optional) | Join groups to support members, view sessions and notes, and take part in group chat |

## Tech Stack

| Part | Technology |
| --- | --- |
| Language | Python 3.14.5 |
| Framework | Django 6.1.3 with Django REST Framework |
| Database | [MySQL] |
| Frontend | [React] |
| Testing | Django test framework |

## Setup

### Requirements

- Python [version]
- Git
- [MySQL ]
- [Node.js, if the project has a React frontend]

### Installation

```bash
git clone https://github.com/[username]/[repository].git
cd [repository]
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
```

### Environment variables

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_DEBUG` | `True` for development, `False` for production |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated host names |
| `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | Database connection |

### Database and demo data

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata [demo_data.json]   # if provided
```

### Run the application

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Running the Tests

```bash
python manage.py test
```

## Demo Accounts

Demo accounts are created by the demo data. Ask your supervisor for the login details; do not publish passwords in this file.

## Project Documents

| Document | Location |
| --- | --- |
| Proposal | `docs/` |
| Requirements (SRS) | `docs/` |
| Work Breakdown Structure | `docs/` |
| Design (ERD, URL map, wireframes) | `docs/` |
| Test plan | `docs/` |

## Screenshots

[Add screenshots of the main pages here.]
