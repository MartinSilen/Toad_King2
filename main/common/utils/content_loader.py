import re


def _check_if_key(line):
    match = re.search(r'\A@', line)
    if match:
        return True
    else:
        return False


def _trim_key(key) -> str:
    key = re.sub(r'\A@', '', key)
    key = re.sub(r' ', '_', key)
    key = key.strip()
    key.encode('utf-8')
    return key


def _trim_newlines(text: str):
    result = text.strip()
    return result


def parse_responses(path_to_file):
    path = path_to_file
    responses_dict = {}
    try:
        with open(path, 'r') as file:
            line = file.readline()
            phrase = ''
            key = ''
            while line:
                if _check_if_key(line):
                    if key != '' and phrase != '':
                        responses_dict[_trim_key(key)] = _trim_newlines(phrase)
                        key = ''
                        phrase = ''
                    key = line
                    line = file.readline()
                elif line != '' or ' ':
                    phrase += line
                    line = file.readline()
                else:
                    line = file.readline()
        responses_dict[_trim_key(key)] = _trim_newlines(phrase)
        return responses_dict
    except(FileNotFoundError, EOFError):
        print(path + ' failed to load')
        return {}
