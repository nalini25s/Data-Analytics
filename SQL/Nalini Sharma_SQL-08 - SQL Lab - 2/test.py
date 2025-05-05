import pyodbc
import pytest
from decimal import Decimal
import datetime

# Normalize rows for comparison
def normalize(row):
    """Clean and normalize row data for comparison."""
    normalized = []
    for item in row:
        if isinstance(item, str):
            normalized.append(item.strip())
        elif isinstance(item, Decimal):
            normalized.append(round(item, 2))
        elif isinstance(item, datetime.date):
            normalized.append(item.isoformat())  # Convert dates to string
        else:
            normalized.append(item)
    return tuple(normalized)

def assert_normalized(actual, expected):
    assert sorted(map(normalize, actual)) == sorted(map(normalize, expected))

@pytest.fixture
def mysql_connection():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=LAPTOP-0TK9QJEO;'
        'DATABASE=sales_db;'
        'Trusted_Connection=yes;'
    )
    connection.autocommit = True
    yield connection
    connection.close()

def test1(mysql_connection):
    cursor = mysql_connection.cursor()
    cursor.execute(open('1.sql', 'r').read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [
        ('John Doe', Decimal('500')),
        ('Jane Smith', Decimal('500')),
        ('Bob Johnson', Decimal('240')),
        ('Alice Brown', Decimal('640')),
        ('Mary Davis', Decimal('240'))
    ]
    assert_normalized(rows, expected)

def test2(mysql_connection):
    cursor = mysql_connection.cursor()
    cursor.execute(open('2.sql', 'r').read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [('Widget A', 40)]
    assert_normalized(rows, expected)
    
def test3(mysql_connection):
    cursor = mysql_connection.cursor()
    cursor.execute(open('3.sql', 'r').read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [
        ('Widget A', Decimal('800')),
        ('Widget B', Decimal('330')),
        ('Widget C', Decimal('640')),
        ('Widget D', Decimal('350'))
    ]
    assert_normalized(rows, expected)

def test4(mysql_connection):
    cursor = mysql_connection.cursor()
    cursor.execute(open('4.sql', 'r').read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [
        (datetime.date(2023, 12, 1), 1),
        (datetime.date(2023, 12, 2), 1),
        (datetime.date(2023, 12, 3), 2),
        (datetime.date(2023, 12, 5), 1),
        (datetime.date(2023, 12, 6), 1),
        (datetime.date(2023, 12, 7), 1),
        (datetime.date(2023, 12, 8), 1),
        (datetime.date(2023, 12, 9), 1)
    ]
    assert_normalized(rows, expected)

def test5(mysql_connection):
    cursor = mysql_connection.cursor()
    cursor.execute(open('5.sql', 'r').read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [
        ('Alice Brown', Decimal('640')),
        ('John Doe', Decimal('500')),
        ('Jane Smith', Decimal('500'))
    ]
    assert_normalized(rows, expected)