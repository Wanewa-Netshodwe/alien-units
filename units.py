def convert(ratios, from_unit, to_unit, value):
  
    visited_units = set()
    link = from_unit
    vl = value

    if from_unit == to_unit:
        return value
    
    if (from_unit, to_unit) in ratios:
        return value / ratios[(from_unit, to_unit)]
    
    if (to_unit, from_unit) in ratios:
        return value * ratios[(to_unit, from_unit)]


    def change_link():
        nonlocal link, vl
      
        visited_units.add(link)

        for k in list(ratios):
            if link in k:
                if link == k[0] and k[1] not in visited_units:
                    vl /= ratios[k]
                    link = k[1]
                    return True
                elif link == k[1] and k[0] not in visited_units:
                    vl *= ratios[k]
                    link = k[0]
                    return True
        
        return False
    
    
    while link != to_unit:
        if not change_link():
            return None
    
    return vl


 
