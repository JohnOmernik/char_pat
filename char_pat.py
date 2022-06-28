def char_pat(astring, case_insensitive=True):
    if case_insensitive:
        astring = astring.lower()
        
    pat_dict = []
    
    prev_type = None
    for c in astring:
        nc = ord(c)
        if nc >= 65 and nc <= 90:
            c_type = "C"
        elif nc >= 97 and nc <= 122:
            c_type = "c"
        elif nc >=48 and nc <= 57:
            c_type = "d"
        elif (nc >= 32 and nc <=47) or (nc >= 58 and nc <=64) or (nc >= 91 and nc <= 96) or (nc >= 123 and nc <= 126):
            c_type = "s"
        else: # non-printable characters
            c_type = "x"
        
        if prev_type is None or prev_type != c_type:
            pat_dict.append({c_type: 1})
        elif prev_type == c_type:
            pat_dict[-1][c_type] += 1
        prev_type = c_type
        
    out_pat = ""
    for p in pat_dict:
        out_pat += list(p.keys())[0] + str(list(p.values())[0])
    return out_pat
