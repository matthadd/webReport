
class Project:
    """Class Project
    """
    # Attributes:
    list_manager[] = None  # () 
    _Name = None  # (std::string) 
    _status = None  # (bool) 
    _ci = None  # (std::string) 
    _list_lot[] = None  # () 
    _client = None  # (std::string) 
    _description = None  # (std::string) 
    _exp_init_date = None  # (char*) 
    _exp_end_date = None  # (char*) 
    _budget = None  # (init) 
    _time_project = None  # (char*) 
    _real_init_date = None  # (char*) 
    _real_end_date = None  # (char*) 
    
    # Operations
    def add_lot(self):
        """function add_lot
        
        returns 
        """
        return None
    
    def remove_lot(self):
        """function remove_lot
        
        returns 
        """
        return None 
    
    def get_id(self):
        
        return self._id
    
    def set_id(self,id):
        self._id= id
        return None
    
    def get_status(self):
        
        return self._status
    
    def set_status(self,status):
        self._status= status
        return None 
    
    def get_list_lot(self):
        
        return self._list_lot
    
    def set_list_lot(self,list_lot):
        self._list_lot=list_lot
        return None
    
    def get_client(self):
        
        return self._client
    
    def set_client(self,client):
        self._client=client
        return None
    
    def get_description(self):
       
        return self._description
    
    def set_description(self,description):
       self._description= description
        return None 
    
    def get_exp_init_date(self):
       
        return self._exp_init_date
    
    def set_exp_init_date(self,exp_init_date):
       self._exp_init_date= exp_init_date
        return None 
    
    def get_exp_end_date(self):
        
        return self._exp_end_date
    
    def set_exp_end_date(self,exp_end_date):
        self._exp_end_date=exp_end_date
        return None
    
    def get_real_init_date(self):
        
        return self._real_init_date
    
    def set_real_init_date(self,real_init_date):
        self._real_init_date=real_init_date
        
        return None 
    
    def set_real_end_date(self,real_end_date):
        self.__real_end_date=real_end_date
        return None 
    
    def get_real_end_date(self):
        
        return self.__real_end_date
    
    def get_list_manager(self):
        
        return self._list_manager
    
    def set_list_manager(self,list_manager):
        self._list_manager=list_manager
        return None
    

