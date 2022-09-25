import math
from id import Id

class IdList:
    # @staticmethod
    def __init__(self, mylist, status):
        self.ids = self.create_id_list(mylist, status)

    def create_id_list(self, mylist, status):
        n = len(mylist) / 3
        i = 0
        n_int = math.floor(n)
        ids = []
        for k in range(n_int):
            # create new id
            # ids.append(bar.__init__())
            new_id = Id()
            ids.append(new_id)
            ids[k]['value'] = int(mylist[i])
            i += 1
            ids[k]['title'] = mylist[i]
            i += 1
            ids[k]['real'] = mylist[i]
            ids[k]['id_status'] = status
        return ids