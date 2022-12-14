def min_window(s, req_chars):

    # hash to keep account of how many required characters we've checked off
    # each key will represent a character in req_chars
    # we preset each to 1 and will look to lower it to 0 when each is fulfilled

    hash = {}
    for c in req_chars:
        hash[c] = 1

    # trackers that we need
    # this is a counter to measure string length against

    counter = len(req_chars)
    begin = 0
    end = 0
    substr_size = len(s) + 1
    head = 0

    while end < len(s):

        # continue running while there's more elements in `s` to process
        if s[end] in hash:  # we've found a letter we needed to fulfill

            # modify the length counter, we can use this as part of our substring
            if hash[s[end]] > 0:
                counter -= 1

            # modify the dictionary to say we've gotten this character requirement
            hash[s[end]] -= 1

        # from here, we increase begin pointer to make it invalid/valid again

        while counter == 0:  # valid, we have what we need

            # calculate the current substring size since we care about min

            if end - begin + 1 < substr_size:
                substr_size = end - begin + 1
                head = begin

            # we want to shrink it from the beginning now
            # to make it the minimum size possible

            if s[begin] in hash:
                hash[s[begin]] += 1

                # this is a character we need

                if hash[s[begin]] > 0:
                    counter += 1  # make it invalid
            begin += 1

        # Keep expanding the window once we are done contracting, try more substrings

        end += 1

    return "" if substr_size == len(s) + 1 else s[head : head + substr_size]


print(min_window("csamsbffffcd", "abc"))