#Place each file name into a list name deliveryFiles
deliveryFiles = ['um-deliveries-day-1.txt', 'um-deliveries-day-2.txt', 'um-deliveries-day-3.txt']

#Create a function that will process each file, taking deliveryFiles as an input
def processDeliveryFile(deliveryFiles):
    """
    Takes in delivery files and returns a report

    Returns a list
    """
#Processes each file in list of deliveryFiles
    for eachFile in deliveryFiles:
        #Open the named file
        current_file = open(eachFile)
        #Remove repetitive printing of day and make it dynamic (grabs 5th to last character of file name) --> Important will require a change for two digit numbers 
        print(f"Day {eachFile[-5]}")
        #Process each line in the file
        for line in current_file:
            #Remove whitespace on the right for each line
            line = line.rstrip()
            #Separate each substring at '|'
            words = line.split('|')
            #Grab first word of the split string
            melon = words[0]
            #Grab second to last word of the split string
            count = words[-2]
            #Grab last word of the split string
            amount = words[-1]
            
            print(f"Delivered {count} {melon}s for total of ${amount}")
        #End processesing by closing the file
        current_file.close()

#Call function and pass list of delivery file names
processDeliveryFile(deliveryFiles)