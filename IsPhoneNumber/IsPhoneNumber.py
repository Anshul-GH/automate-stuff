import re


def isPhoneNumber(inp_str):
    phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    mo = phoneNumberRegex.search(inp_str)
    print('Phone number found: ', mo.group(), mo.group(0), mo.group(1), mo.group(2), mo.groups())


if __name__ == '__main__':
    print('Print some string text:')
    inp_str = input()
    isPhoneNumber(inp_str)