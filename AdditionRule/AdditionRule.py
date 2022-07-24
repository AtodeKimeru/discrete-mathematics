def prob_a_or_b(a, b, all_possible_outcomes):
    # probability of event a
    prob_a = len(a)/len(all_possible_outcomes)
	
	# probability of event b
    prob_b = len(b)/len(all_possible_outcomes)
	
	# intersection of events a and b
    inter = a.intersection(b)
	
	# probability of intersection of events a and b
    prob_inter = len(inter)/len(all_possible_outcomes)
	
	# add return statement here
    return prob_a + prob_b - prob_inter
