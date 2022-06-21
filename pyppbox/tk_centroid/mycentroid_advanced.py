from math import hypot


class MyCTTracker(object):


    def __init__(self, cfg):
        self.max_distance = cfg.max_distance
        self.plist = []
        self.clist = []


    def getDist(self, p1, p2):
        res = 0.0
        (x1, y1) = p1
        (x2, y2) = p2
        res = hypot(x2 - x1, y2 - y1)
        return res


    def getProbableID(self, point, plist, max_distance):
        id = -1
        dis_list = []

        for p in plist:
            dis_list.append(self.getDist(point, p.getRepspoint()))
        
        min_dis = dis_list[0]

        index = 0
        for p in plist:
            if min_dis >= dis_list[index]:
                min_dis = dis_list[index]
                id = p.getCid()
            index += 1

        if min_dis > max_distance:
            id = -1

        return id


    def getOldIDsByCid(self, cid):
        faceid = "Unknown"
        deepid = "Unknown"

        for p in self.plist:
            if cid == p.getCid():
                faceid = p.getFaceid()
                deepid = p.getDeepid()
                break
        
        return faceid, deepid


    def getAvailableIDs(self, usedIDs):
        aIDs = []
        len_plist = len(self.plist)
        len_clist = len(self.clist)

        if len_plist >= len_clist:
            aIDs = list(set(range(0, len_plist)) - set(usedIDs))
        elif len_clist > len_plist:
            aIDs = list(set(range(0, len_clist)) - set(usedIDs))

        return aIDs


    def update(self, _, current_ppobjlist):
        self.plist = self.clist
        self.clist = current_ppobjlist
        hang_list_cindex = []
        used_cids = []

        if not self.plist:
            pass
        elif len(self.clist) > 0:

            for i in range (0, len(self.clist)):
                
                prev_id = self.getProbableID(self.clist[i].getRepspoint(), self.plist, self.max_distance)

                if prev_id == -1 or prev_id in used_cids:
                    hang_list_cindex.append(i)
                else:
                    faceid, deepid = self.getOldIDsByCid(prev_id)
                    self.clist[i].updateIDs(prev_id, faceid, deepid)
                    used_cids.append(prev_id)

            i = 0
            for i in range(0, len(hang_list_cindex)):
                cid = hang_list_cindex[i]
                new_id = self.getAvailableIDs(used_cids)[0]
                self.clist[cid].updateIDs(new_id, "Unknown", "Unknown")
                i += 1

        return self.clist
