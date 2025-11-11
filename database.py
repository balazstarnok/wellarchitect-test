"""
Database module with SQL injection vulnerabilities and vulnerable dependencies.
This file tests:
- Import scanning (uses vulnerable packages)
- Reachable CVE detection (imports + usage)
- Security findings (SQL injection)
"""
import sqlite3
import flask
from flask import request
import psycopg2  # Vulnerable version in requirements
from cryptography.fernet import Fernet  # Vulnerable cryptography


def execute_query_unsafe(query):
    """
    UNSAFE: SQL injection vulnerability
    This function directly executes user input without sanitization
    """
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    # Vulnerable: direct string interpolation
    cursor.execute(f"SELECT * FROM users WHERE username = '{query}'")
    results = cursor.fetchall()
    conn.close()
    return results


def get_user_by_id(user_id):
    """
    UNSAFE: SQL injection via string formatting
    """
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + str(user_id))
    return cursor.fetchone()


def search_users():
    """
    Flask route with SQL injection vulnerability
    """
    search = request.args.get('q', '')
    # Vulnerable: direct parameter usage
    query = f"SELECT * FROM users WHERE name LIKE '%{search}%'"
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def encrypt_data(data):
    """
    Uses vulnerable cryptography library
    This import will be detected by import scanner
    """
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data.encode())
    return encrypted


def connect_postgres(host, database, user, password):
    """
    Uses vulnerable psycopg2 library
    This import will be detected and should show as reachable CVE
    """
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password  # Hardcoded password - security issue
    )
    return conn


# API keys that should be detected by Gitleaks
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

