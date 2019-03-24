browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
print(browsing_session.pop())

# extending a list
string_to_apped = "abc"
browsing_session.extend(string_to_apped)
print(browsing_session)
print(type(string_to_apped))

# Insert an item at a given position
browsing_session.insert(2, "y")
print(browsing_session)
