
"""
An example of a rung
+V                           -V
I----[/20/]----I----( 30 )----I
I              I              I
I              I----( 20 )----I
"""


"""
a contact in a ladder logic program
ctype:
    This is an id for what typr of contact it is
    0: this is for a relay
    1: this is for a button whose state can be changed at runtime
n_state:
    this is for the normal state of the relay:
    TRUE: normally open contact
    FALSE: normally closed contact
relay:
this refers to the coil or button id that the contact is connected
"""
class contact:
    def __init__(self,n_state,relay,c_type):
        self.n_state = n_state
        self.relay = relay
        self.c_type = c_type 
    """
    Gets the state of the contact
    ARGS:
        inp:    list of all button and coil states
    """
    def get_state(self,inp,is_energized):
        if (self.n_state == inp[self.c_type][self.relay]):
            return True
        else:
            return False
    def show(self):
        if (c_type == 0):
            if(n_state == False):
                return(  f"-[/{self.relay}/]-")
            if(n_state == True):
                return( f"-[/{self.relay}/]-")
        else:
            #button symbol:w
            return(f"-_-{self.relay}-_-") 
class coil:
    def __init__(self,relay):
        self.relay = relay
    
    def get_state(self,inp,is_energized):
        inp[0][self.relay] = is_energized 

    def show(self):
        return( f"-( {self.relay} )-")

"""
class rung:
    def __init__(self, c_list):
        self.c_list = c_list
    
    def run(self,inp):
"""
class tape:
    def __init__(self):
        self.tapes = ['']
        self.rows = 0
        self.tl = 0
    def multiprint(self,row,col,what):
        # used fro tabular prrinting
        nr = row - self.rows
        if ( nr > 0):
            for i in range(nr):
                self.tapes.append('o' * self.tl)
                self.rows = self.rows + 1

        print(self.tapes)
        n =  (col + len(what)) - self.tl 
        if (n>0):
            print("w")
            for i in range(0,self.rows+1):
                print("e")
                self.tapes[i] = self.tapes[i] +  ('w' * n)
        self.tapes[row] = self.tapes[row][0:col] + what 
        print(self.tapes)
        
 
t = tape()
t.multiprint( 2 , 3,"ja")

        
