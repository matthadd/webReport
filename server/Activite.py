from Lot import Lot

class Activite:
    """Class Activite
    """
    # Attributes:
    list_manger = None  # () 
    _id = None  # (std::string) 
    _status = None  # (bool) 
    _exp_init_date = None  # (char*) 
    _exp_end_date = None  # (char*) 
    _list_user = None  # () 
    _real_init_date = None  # (char*) 
    _real_end_date = None  # (char*) 
    _description = None  # (std::string) 
    _total_purechase = None  # (int) 
    _budget_expected = None  # () 
    
    # Operations
    def get_id(self):
       
        
        return self._id 
       
        
    
    def get_status(self):
        
        
        return self._status
        
        
    
    def get_exp_init_date(self):
        
        
        return self._exp_init_date
        
        
    
    def get_exp_end_date(self):
        
        
        return self._exp_end_date
        
     
    
    def get_budget_time_unit(self):
        
        
        return self._budget_time_unit
       
       
    
    def get_list_user(self):
        
        
        return  self._list_user
        
    
    def get_real_init_date(self):
        
        
        return self._real_init_date
        
      
    
    def get_real_end_date(self):
       
        
        return self._real_end_date
        
    
    def get_description(self):
        
        
        return self._description
        
       
    
    def get_buget_time_currency(self):
      
        
        return self._buget_time_currency
       
    
    def set_id(self,id):
       self._id=id
        
        return None
       
     
    
    def set_status(self,status):
        self._status=status
        
        return None
        
        
    
    def set_exp_init_date(self,exp_init_date):
        
        self._exp_init_date=exp_init_date
        return None
        
    
    def set_exp_end_date(self,exp_end_date):
      self._exp_end_date=exp_end_date
        
        return None
        
    
    def set_budget_time_unit(self,budget_time_unit):
    self._budget_time_unit=budget_time_unit
        return None 
    
    def set_list_user(self,list_user):
       self._list_user=list_user
        return None 
    
    def set_real_init_date(self,real_init_date):
       self._real_init_date=real_init_date
        return None 
    
    def set_real_init_date(self,real_init_date):
        self._real_init_date=real_init_date
        return None 
    
    def set_description(self,description):
       self._description=description
        return None 
    
    def set_buget_time_currency(self,buget_time_currency):
        self._buget_time_currency=buget_time_currency
        return None 
    
    def get_total_purechase(self):
        
        return self._total_purechase
    
    def set_total_purechase(self,total_purechase):
        self._total_purechase=total_purechas
        return None 
    
    def get_budget(self):
        
        return self._budget
    
    def set_budget(self,budget):
        self._budget=budget
        return None 
    
    def get_list_manager(self):
        
        return self._list_manager
    
    def set_list_manager(self,list_manager):
       self._list_manager=list_manager
        return None 
    

