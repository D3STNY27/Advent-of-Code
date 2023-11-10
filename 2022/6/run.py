char_map = {}

with open('input.txt', 'r') as file_in:
    stream = file_in.readline()

    for i in range(13):
        char_map[stream[i]] = 1 if stream[i] not in char_map else char_map[stream[i]]+1
    
    for i in range(13, len(stream)):
        status = True
        for key in char_map:
            if char_map[key] > 1:
                status = False
        
        if stream[i] not in char_map and status:
            print(i)
            break
    
        if stream[i-13] in char_map:
            char_map[stream[i-13]] -= 1
            if char_map[stream[i-13]]==0:
                del char_map[stream[i-13]]
    
        char_map[stream[i]] = 1 if stream[i] not in char_map else char_map[stream[i]]+1
