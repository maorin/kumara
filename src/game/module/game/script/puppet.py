'''
Created on 2016年5月3日

@author: maojj
'''
import Queue

class Puppet():
    cur_path = None
    start = None
    end = None
    
    def fire_dead_event(self):
        pass
    
    def fire_move_event(self):
        pass
    '''
    def get_cur_path(self):
        frontier = Queue()
        frontier.put(self.start)
        visited = {}
        visited[self.start] = True
        
        while not frontier.empty():
            current = frontier.get()
            for next in graph.neighbors(current):
                if next not in visited:
                    frontier.put(next)
                    visited[next] = True
        return frontier
    '''
class Footman(Puppet):
    pass

class Tank(Puppet):
    pass