def find_excluded_options(value_list: list, true_list: list) -> list:
    return [value for value in value_list if value not in true_list]
