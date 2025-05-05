import pyodbc
import pytest
from decimal import Decimal

# Normalize rows for comparison
def normalize(row):
    """Clean and normalize row data for comparison."""
    normalized = []
    for item in row:
        if isinstance(item, str):
            normalized.append(item.strip())  # Strip whitespace from strings
        elif isinstance(item, float):
            normalized.append(round(item, 2))  # Optional: Round floats if needed
        elif isinstance(item, Decimal):
            normalized.append(item)  # Keep Decimal types intact
        else:
            normalized.append(item)  # Other types (e.g., int) stay as they are
    return tuple(normalized)

@pytest.fixture
def mysql_connection():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=LAPTOP-0TK9QJEO;'
        'DATABASE=social_media_db;'
        'Trusted_Connection=yes;'
    )
    connection.autocommit = True
    yield connection
    connection.close()

def test1(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('1.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [('sunset_lover', 400), ('sky_wanderer', 350), ('neon_ninja', 250), ('starlight_dancer', 200), ('zen_master', 150)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 1 failed: Expected {expected_rows}, got {rows}"
    
def test2(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('2.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [('sunset_lover',)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 2 failed: Expected {expected_rows}, got {rows}"
    
def test3(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('3.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [('starlight_dancer', 120, 450)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 3 failed: Expected {expected_rows}, got {rows}"
    
def test4(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('4.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [(2,)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 4 failed: Expected {expected_rows}, got {rows}"

def test5(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('5.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [('Female', 1250), ('Male', 1200), ('Other', 600)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 5 failed: Expected {expected_rows}, got {rows}"

def test6(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('6.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [(645,)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 6 failed: Expected {expected_rows}, got {rows}"

def test7(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('7.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [(Decimal('600'),), (Decimal('900'),), (Decimal('800'),)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 7 failed: Expected {expected_rows}, got {rows}"
    
def test8(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('8.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    
    expected_rows = [('sky_wanderer', 900), ('sunset_lover', 800), ('neon_ninja', 600)]
    # Normalize and compare
    assert [normalize(row) for row in rows] == [normalize(row) for row in expected_rows], f"Test 8 failed: Expected {expected_rows}, got {rows}"
    