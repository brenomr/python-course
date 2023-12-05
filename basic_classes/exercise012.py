"""
Make a function to merge two lists, the rules are:
- The list with less elements will be the main list
- The return need to be a tuple
- e.g:
    list_1 = ["city 1", "city 2", "city 3" ]
    list_1 = ["CT1", "CT2" ]

    return: [ ("city 1", "CT1"), ("city 2", "CT2") ]
"""
cities = [ "Salvador", "São Paulo", "Campinas", "Brasília" ]
acronym = [ "BA", "SP", "SP" ]


def merge_lists(city_list: list, acronym_list: list):
    """Merge two lists based on the short one."""

    if len(city_list) < len(acronym_list):
        shortest_list = city_list
    else:
        shortest_list = acronym_list

    # long solution
    # merged = []
    # for index, item in enumerate(shortest_list):
    #     merged.append((city_list[index], acronym_list[index]))

    # short solution
    merged = [ (city_list[index], acronym_list[index]) for index, item in enumerate(shortest_list) ]

    print(merged)

merge_lists(cities, acronym)
