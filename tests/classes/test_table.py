from cmath import exp
from phtml import Table, TableRow, TableHeader, TableData
import pytest


def test_empty():
    item = Table()
    expected = [
        '<table></table>',
    ]
    actual = item.return_document
    assert actual == expected

    item = TableRow()
    expected = [
        '<tr></tr>',
    ]
    actual = item.return_document
    assert actual == expected

    item = TableHeader()
    expected = [
        '<th></th>',
    ]
    actual = item.return_document
    assert actual == expected

    item = TableData()
    expected = [
        '<td></td>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Table()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<table class="testOne testTwo"></table>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Table()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<table style="testOne: testTwo;"></table>',
    ]
    actual = item.return_document
    assert actual == expected

def test_classes_and_styles():
    item = Table()
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<table class="testOne testTwo" style="testOne: testTwo;"></table>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_internal():
    item = Table()
    item.internal.append('test on the inside')
    expected = [
        '<table>',
        '    test on the inside',
        '</table>',
    ]
    actual = item.return_document
    assert actual == expected

def test_table():
    table = Table()

    data = [
        ['index', 'name', 'age'],  # Header
        [0, 'John', '20'],  # Data 0
        [1, 'Jill', '30'],  # Data 1
        [2, 'Jack', '40'],  # Data 2
    ]

    header_row = TableRow()
    for item in data.pop(0):
        header_row.internal.append(TableHeader(internal=item))
    table.internal.append(header_row)

    for row in data:
        data_row = TableRow()
        for item in row:
            data_row.internal.append(TableData(internal=item))
        table.internal.append(data_row)

    expected = [
        '<table>',
        '    <tr>',
        '        <th>',
        '            index',
        '        </th>',
        '        <th>',
        '            name',
        '        </th>',
        '        <th>',
        '            age',
        '        </th>',
        '    </tr>',
        '    <tr>',
        '        <td>',
        '            0',
        '        </td>',
        '        <td>',
        '            John',
        '        </td>',
        '        <td>',
        '            20',
        '        </td>',
        '    </tr>',
        '    <tr>',
        '        <td>',
        '            1',
        '        </td>',
        '        <td>',
        '            Jill',
        '        </td>',
        '        <td>',
        '            30',
        '        </td>',
        '    </tr>',
        '    <tr>',
        '        <td>',
        '            2',
        '        </td>',
        '        <td>',
        '            Jack',
        '        </td>',
        '        <td>',
        '            40',
        '        </td>',
        '    </tr>',
        '</table>',
    ]
    actual = table.return_document
    for i in actual:
        print(i)
    assert actual == expected



# def test_internal_object():
#     item = Paragraph()
#     d1 = Paragraph()
#     d2 = Paragraph()
#     item.internal.extend([d1, d2])
#     expected = [
#         '<p>',
#         '    <p></p>',
#         '    <p></p>',
#         '</p>',
#     ]
#     actual = item.return_document
#     assert actual == expected
