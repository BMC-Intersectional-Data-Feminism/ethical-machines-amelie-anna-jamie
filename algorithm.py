import urban_planning 

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def student_algorithm(option1, option2):
    """Students define their own algorithm"""
    print('Write your own algorithm here!')
    #how to make and use dictionaries python AI overview
    cat_rank = {
    "Ambulance": 20, 
    "Pedestrian": 18, 
    "Bicyclist": 12, 
    "Public Bus": 11, 
    "Light Rail": 10, 
    "Motorcyclist": 9, 
    "Police vehicle": 8, 
    "Carpool": 7, 
    "Ride-share vehicle": 6, 
    "Human-driven car": 5, 
    "Self-driving car": 4, 
    "Animal": 3, 
    "Autonomous delivery robot": 2, 
    "Street-cleaning robot": 1
    }

    moral_rank = {
        "Large wild animal such as a deer": 10
    }
    m1 = 0
    m2 = 0
    if (option1[1] in moral_rank and option2[1] in moral_rank) :
        m1 = moral_rank[option1[1]]
        m2 = moral_rank[option2[1]]

    if (option1[0] in cat_rank and option2[0] in cat_rank) :
        if ((cat_rank[option1[0]]+ m1) > (cat_rank[option2[0]])+ m2) :
            return option1, option2
        else :
            return option2, option1
    else :
        return option1, option2
    
    if (option1[1] in cat_rank and option2[1] in cat_rank) :
        if((cat_rank[option1[1]]) > (cat_rank[option2[0]])):
            return option1, option2
        else :
            return option2, option1

# Function to run the simulation using a given algorithm
# Run the activity
#urban_planning.run_activity()

# Run the activity using the example algorithm
#print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = always_pick_non_vehicle)
urban_planning.run_activity(num_scenarios=25, decision_function = student_algorithm)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")
