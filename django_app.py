"""
Django models with vulnerable dependencies and security issues.
Tests detection of Django CVEs and SQL injection patterns.
"""
from django.db import models
from django.http import HttpResponse
from django.db import connection
import lxml.etree as ET
from bs4 import BeautifulSoup


class User(models.Model):
    """User model"""
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)  # Plain text password storage - bad!
    api_key = models.CharField(max_length=255)


def get_user_unsafe(request):
    """
    UNSAFE: SQL injection vulnerability using raw SQL
    Django 2.2.0 is vulnerable + bad code
    """
    user_id = request.GET.get('id')
    # Vulnerable: raw SQL with string interpolation
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        row = cursor.fetchone()
    return HttpResponse(str(row))


def parse_xml(xml_string):
    """
    XML parsing with vulnerable lxml
    Tests lxml import and usage detection
    """
    parser = ET.XMLParser(resolve_entities=True)  # XXE vulnerability
    tree = ET.fromstring(xml_string, parser)
    return tree


def parse_html(html_content):
    """
    HTML parsing with BeautifulSoup
    Tests beautifulsoup4 import and usage
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract all links
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    
    return links


def process_user_data(user_input):
    """
    Multiple vulnerability patterns
    """
    # SQL injection via Django ORM raw query
    users = User.objects.raw(
        f"SELECT * FROM myapp_user WHERE username = '{user_input}'"
    )
    
    # XXE via lxml
    xml = f"<user><name>{user_input}</name></user>"
    tree = parse_xml(xml.encode())
    
    return list(users)

