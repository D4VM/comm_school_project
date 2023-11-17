import re


def validate_url(provided_url: str) -> bool:
    """
    Validates URL provided by user request.
    If URL is valid for www.myauto.ge, and has product ID. returns True.

    :param provided_url:
    :return:
    """
    # Regex Patterns
    pattern_digits = r'\d{8}'  # Finding Digits
    pattern_myauto_ge = r'myauto\.ge'  # Finding Text

    check_digits = re.search(pattern_digits, provided_url)
    check_myauto_ge = re.search(pattern_myauto_ge, provided_url)

    return bool(check_digits) and bool(check_myauto_ge)


def extract_id(provided_url: str) -> str:
    """
    Extracts ID from myauto.ge URL

    :param provided_url:
    :return:
    """
    pattern_digits = r'\d{8}'  # finding digits
    product_id = re.search(pattern_digits, provided_url)
    return product_id.group(0)


def calculate_average(numbers):
    """
    As func name says
    :param numbers:
    :return:
    """
    if not numbers:
        return 0  # Avoid division by zero for an empty list

    total = sum(numbers)
    average = total / len(numbers)
    return average
