"""Restaurant rating lister."""

scores_file = open("scores.txt")


def make_a_line(filename):
	restaurant_rating_list = []
	for line in scores_file:
		line_restaurant_rating = line.rstrip().split(":")
		restaurant_rating_list.append(line_restaurant_rating)
	return (restaurant_rating_list)
		
# print (make_a_line(scores_file))

rest_list=make_a_line(scores_file)

def creating_dictionary(newlist):
	for item in restaurant_rating:
		restaurant_rating_dict = {item[0]: item[1]}
		print (restaurant_rating_dict)
	return restaurant_rating_dict

