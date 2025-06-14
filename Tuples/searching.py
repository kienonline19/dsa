def search_tuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} is found at {i} index"
        
    return "The element is not found!"


new_tuple = tuple("abcdef")

print('a' in new_tuple)
print('w' in new_tuple)

print(new_tuple.index('d'))

print(search_tuple(new_tuple, 'e'))
print(search_tuple(new_tuple, 'w'))
