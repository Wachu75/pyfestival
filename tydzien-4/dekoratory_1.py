def format_to_csv(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if len(result) == 0:
            return ''
        keys = result[0].keys()
        output = [';'.join(keys)]
        for row in result:
            output.append(';'.join(row.values()))
        return '\n'.join(output)
    return wrapper

def test_format_to_csv():
    @format_to_csv
    def return_dict():
        return [
            {
                'imię': 'aa',
                'nazwisko': 'aa'
            },
            {
                'imię': 'vv',
                'nazwisko': 'vv'
            }
        ]
    result = return_dict()

    assert result == 'imię;nazwisko\naa;aa\nvv;vv'

if __name__ == "__main__":
    @format_to_csv
    def return_dict():
        return [
            {
                'imię': 'aa',
                'nazwisko': 'aa'
            },
            {
                'imię': 'vv',
                'nazwisko': 'vv'
            }
        ]

    print(return_dict())