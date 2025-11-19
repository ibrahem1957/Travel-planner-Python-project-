import data

def getting_destination(budget, trip_types):
    #Creating 2 list to provide the user with global and local recommendations
    global_recommendations = []
    local_recommendations = []
    #Convert all trip type names to lowercase for easy matching using lambda
    trip_types = list(map(lambda t: t.lower(), trip_types))
    """
    Doing iteration over both travel dictionaries (global & local)
    to find:
        - destinations matching the user budget with -100 SAR tolerance 
        - destinations matching any of the chosen trip types
    """
    for des_name, des_info in data.travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        price_diff = budget - avg_price
        if 0 <= price_diff <= 100:
            if any(t in des_info["trip_type"] for t in trip_types):
                global_recommendations.append({des_name: des_info})

    for des_name, des_info in data.saudi_travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        price_diff = budget - avg_price
        if 0 <= price_diff <= 100:
            if any(t in des_info["trip_type"] for t in trip_types):
                local_recommendations.append({des_name: des_info})
    #Trimming lists to only show up to 2 recommendations per list
    global_recommendations = global_recommendations[:2]
    local_recommendations = local_recommendations[:2]

    #these printing and return logic i wrote them only for testing feel free to modified it to match the output
    if global_recommendations:
        print(f'Global recommendations: {global_recommendations}')
    if local_recommendations:
        print(f'Local recommendations: {local_recommendations}')

    if not global_recommendations and not local_recommendations:
        print ("Sorry! no recommendation matches your preferences and budget found! Please try again with another budget")

    return {
        "global": global_recommendations,
        "local": local_recommendations
    }

