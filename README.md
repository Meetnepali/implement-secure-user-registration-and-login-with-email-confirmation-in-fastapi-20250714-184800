# Guidance for Task: Secure User Registration/Login API with Email Confirmation

## Objective
Implement TWO FastAPI endpoints to securely handle user registration (with email confirmation) and user login (with JWT). You will ensure secure password handling, unique emails, asynchronous background tasks for confirmation, and robust input validation and error handling, grouped under an /auth router.

## Your Task
- Complete the implementation of a registration endpoint that:
  - Registers users with unique email addresses
  - Hashes passwords securely
  - Stores a unique email confirmation token
  - Asynchronously (background) simulates sending an email confirmation token
- Complete the login endpoint so that:
  - Only users with confirmed emails can log in
  - Returns a JWT on successful login (use PyJWT or equivalent)
- Implement the email confirmation endpoint so the user can confirm their email with a token
- Ensure all error handling, validation, and status codes reliably cover common failure cases
- Endpoints should be grouped in a router and use FastAPI dependency injection where appropriate

## Project Structure
- You are provided a project structure using FastAPI, SQLAlchemy, and Pydantic
- All key starting files are present, but core registration, login, and email confirmation logic may be incomplete or need enhancement
- Database is SQLite via SQLAlchemy (model provided in app/models.py)
- Password hashing with Passlib
- JWT logic is in app/utils.py for extensibility

## Requirements
- Follow best practices for password security and JWT handling
- All endpoints should return appropriate status codes and clear error messages using FastAPI's HTTPException
- Simulate email confirmation token sending by printing to console (actual email sending NOT required)
- Use Pydantic for data validation on all requests and responses
- Make sure registration fails gracefully for duplicate emails
- Only confirmed users can get a JWT at login

## Verifying Your Solution
- Register a user at POST /auth/register
- Look for the token printed to the console (simulated email)
- Confirm the user at POST /auth/confirm (with email and token)
- Log in at POST /auth/login and verify a JWT is returned only if email is confirmed
- Attempt to register with the same email and expect a validation error
- Attempt to log in before confirmation or with an invalid password and confirm proper errors are raised

Review all relevant files prior to beginning. Structure your endpoints carefully and employ strong validation and separation of logic to promote maintainability and testability.