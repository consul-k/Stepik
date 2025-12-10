def analyze_portals(portal_list):
    sorted_portals = sorted(portal_list)
    
    average = sum(portal_list) / len(portal_list)
    
    above_average = {portal for portal in portal_list if portal > average}
    
    return (sorted_portals, above_average)
