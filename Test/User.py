from roles import roles

class User:
    """Class User
    """
    # Attributes:
    nom = None  # (str) 
    prenom = None  # (str) 
    matricule = None  # (str) 
    password = None  # (str) 
    metier = None  # (str) 
    roles = {}  # (list) 
    photo = {} # (list) 
    status = None  # (int) 
    
    # Operations
    
    def __Init__(self, nom, prenom, matricule, password, metier, newRole , newPhoto, roles = [0]):
        """function User
        
        nom: str
        prenom: str
        matricule: str
        password: str
        metier: str
        newRole : str
        newPhoto: list
        : 
        roles: list
        
        returns 
        """
        self.nom=nom
        self.prenom=prenom
        self.matricule=matricule
        self.password=password
        self.metier=metier
        self.roles.append(newRole)
        self.photo.append(newPhoto)

        
    
    def updateUser(self, nom, prenom, matricule, password, metier, roles):
        """function updateUser
        
        nom: str
        prenom: str
        matricule: str
        password: str
        metier: str
        roles: list
        
        returns void
        """
        self.nom=nom
        self.prenom=prenom
        self.matricule=matricule
        self.password=password
        self.metier=metier
        self.roles.append(roles)
    
    def createProject(self, dateBegin, dateEnd, budget):
        """function createProject
        
        dateBegin: str
        dateEnd: str
        budget: int
        
        returns 
        """

        return None # should raise NotImplementedError()
    
    def updateProject(self, datebegin, dateEnd, budget):
        """function updateProject
        
        datebegin: str
        dateEnd: str
        budget: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def createMetier(self, metier):
        """function createMetier
        
        metier: string
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def updateMetier(self, metier):
        """function updateMetier
        
        metier: str
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def giveRole(self, role, matricule):
        """function giveRole
        
        role: str
        matricule: str
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def createLot(self, dateBegin, dateEnd, budget):
        """function createLot
        
        dateBegin: str
        dateEnd: str
        budget: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def updateLot(self, dateBegin, dateEnd, budget):
        """function updateLot
        
        dateBegin: string
        dateEnd: str
        budget: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def giveLotToRespo(self, id_lot, matricule_respo):
        """function giveLotToRespo
        
        id_lot: str
        matricule_respo: str
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def terminateLot(self, id_lot):
        """function terminateLot
        
        id_lot: string
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def createActivity(self, dateBegin, dateEnd, budget):
        """function createActivity
        
        dateBegin: str
        dateEnd: str
        budget: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def updateActivity(self, dateBegin, dateEnd, budget):
        """function updateActivity
        
        dateBegin: str
        dateEnd: int
        budget: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def giveActivityToRespoMetier(self, id_activity, matricule_respo):
        """function giveActivityToRespoMetier
        
        id_activity: string
        matricule_respo: str
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def terminateActivity(self, id_activity):
        """function terminateActivity
        
        id_activity: 
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def giveActivityToPeople(self, id_activity, matricule_user):
        """function giveActivityToPeople
        
        id_activity: str
        matricule_user: str
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def setInfoUser(self, input_string):
        """function setInfoUser
        
        input_string: string
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def setInfoWork(self, input_string, timeWorking, budget):
        """function setInfoWork
        
        input_string: string
        timeWorking: 
        budget: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    

