def melons_sold_by_salesperson(file_name):
    """Generates a dictionare with salespeople and number of melons they sold"""
    #open melon_report file
    melon_report = open(file_name)
    #create empty dictionary melons_by_person
    melons_by_person = {}
    for line in melon_report:
        line = line.rstrip()
    #assign variables, = strip and split report file
        salesperson, total_income, num_melons = line.split("|")

        #if salesperson name is in melon_report
        if salesperson in melons_by_person:
            melons_by_person[salesperson] += int(num_melons)
        else:
            melons_by_person[salesperson] = int(num_melons)

    return melons_by_person

# melons_sold_by_salesperson("sales-report.txt")
#melons_by_person[salesperson] = 


def print_report(melons_sold_by_salesperson):
    """Prints a report of total melons sold by salesperson""" 
    for salesperson, num_melons in melons_sold_by_salesperson.items():
        print(f"{salesperson}: {num_melons}")   

print_report(melons_sold_by_salesperson("sales-report.txt"))