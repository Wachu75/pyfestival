def format_to_csv(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if len(result) == 0:
            return ''
        keys = result[0].keys()
        output = [';'.join(keys)]  #[imie;nazwisko]

        for row in result:
            output.append(';'.join(row.values()))

        return '\n'.join(output)
    return wrapper

def test_format_to_csv():
    @format_to_csv
    def return_dict():
        return [
            {
                'imie': 'Stefan',
                'nazwisko': 'Zeromski'
            },
            {
                'imie': 'Władysław',
                'nazwisko': 'Reymont'
            }
        ]
    result = return_dict()

    assert result == 'imie;nazwisko\nStefan;Zeromski\nWładysław;Reymont'

@format_to_csv
def return_sample():
    return [
        {
            'id':'1',
            'name': 'lemon'
         },
        {
            'id': '2',
            'name': 'orange'
        }
    ]

print(return_sample())

