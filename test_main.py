import main
from tabulate import tabulate

def test_read_files():
    assert main.read_files() == []
    assert main.read_files(['notExist.csv']) == []
    assert main.read_files(['test.csv']) == [['iphone','apple','999','4.9']]

def test_calculate_average_rating():
    assert main.calculate_average_rating() == [['','brand','rating']]
    assert main.calculate_average_rating([['iphone','apple','999','4.9'],['iphone','apple','999','4.9']]) == [['','brand','rating'],[1, 'apple',4.90]]

def test_output():
    assert main.output('average-rating') == print('No data to make report. Please, add at least one file with data.')
    assert main.output('average-rating',[['iphone','apple','999','4.9'],['iphone','apple','999','4.9']]) == print(tabulate([['','brand','rating'],[1, 'apple',4.90]], headers='firstrow', tablefmt="pretty"))