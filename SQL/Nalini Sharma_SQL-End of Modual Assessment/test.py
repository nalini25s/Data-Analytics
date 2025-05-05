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
        'DATABASE=DA062025;'
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
    expected = [(2, 1002, 5, Decimal('150')), 
                    (7, 1002, 6, Decimal('180')), 
                    (4, 1003, 8, Decimal('240')), 
                    (8, 1003, 10, Decimal('400')), 
                    (6, 1004, 7, Decimal('350'))]
    assert_normalized(rows, expected)
  
def test2(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('2.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [('John Doe', 25), 
                    ('Alice Brown', 18), 
                    ('Jane Smith', 12), 
                    ('Mary Davis', 12), 
                    ('Bob Johnson', 9)]
    assert_normalized(rows, expected)

    
def test3(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('3.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [('Widget A', Decimal('800'), 'High Revenue'), 
                    ('Widget B', Decimal('330'), 'High Revenue'), 
                    ('Widget C', Decimal('640'), 'High Revenue'), 
                    ('Widget D', Decimal('350'), 'High Revenue')]
    assert_normalized(rows, expected)

    
def test4(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('4.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [('John Doe', 2), ('Jane Smith', 2), ('Alice Brown', 2)]
    assert_normalized(rows, expected)


def test5(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('5.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [
    (1, 'Joh', 'Widget A', Decimal('200.00')),
    (3, 'Bob', 'Widget A', Decimal('60.00')),
    (5, 'Joh', 'Widget A', Decimal('300.00')),
    (9, 'Mar', 'Widget A', Decimal('240.00')),
    (2, 'Jan', 'Widget B', Decimal('150.00')),
    (7, 'Bob', 'Widget B', Decimal('180.00')),
    (4, 'Ali', 'Widget C', Decimal('240.00')),
    (8, 'Ali', 'Widget C', Decimal('400.00')),
    (6, 'Jan', 'Widget D', Decimal('350.00'))
]
    assert_normalized(rows, expected)


def test6(mysql_connection):
    cursor = mysql_connection.cursor()
    with open('6.sql', 'r') as file:
        cursor.execute(file.read())
    rows = cursor.fetchall()
    cursor.close()
    expected = [
    ('widget a', 40),
    ('widget b', 11),
    ('widget c', 18),
    ('widget d', 7)
]
    assert_normalized(rows, expected)

