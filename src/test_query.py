from utils.query.query import preform_query


if __name__ == "__main__":
    query_string = input("Query: ")
    result = preform_query(query_string)
    print(result)