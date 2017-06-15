
class BinarySearch(list):
    length = 0

    def __init__(self, a, b):
        step = b              #initialise the list here using b as step
        self.append(step)
        for n in range(1, a):
            step += b
            self.append(step)
        self.length = len(self)

    def search(self, value):       #initialize the result dict
        result = {"count": 0, "index": 0}    
        temp = self    #make a copy of the list as temp since we are going to mess around
        index = 0

        while len(temp) > 1:
            if temp[len(temp) - 1] == value:     #if our value is at the end set index to count-1 and break since we found the index
                if len(temp) == len(self):
                    index = len(temp) - 1
                else:
                    index += 1
                break
            elif temp[0] == value:         # if out value is at the start set index to 0 and break since we found the index
                index += 0
                break
            result.update({"count": result.get("count") + 1})  #for each loop increase count plus one
            
            middle = int(len(temp) / 2)     # if out value is at the middle set index to 0 and break since we found the index
            if temp[middle] <= value:
                index += - int(middle / 2)
                temp = temp[middle:]
            else:
                index += middle
                temp = temp[:middle]

        result.update({"index": index})
        return result