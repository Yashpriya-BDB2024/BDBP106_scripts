def sorted_function_usage():
    friends_dict=[{"Name": "Harshita", "Age": 24, "City": "Bikaner"},{"Name": "Mounika", "Age": 22, "City": "Bangalore"}]
    sort_by_age=lambda x: x["Age"]   # to extract the age for sorting
    sorted_dict_by_age=sorted(friends_dict, key=sort_by_age)   # sort friends_dict by age as key using sort_by_age function.
    return sorted_dict_by_age
def main():
    print(sorted_function_usage())
if __name__ == "__main__":
    main()