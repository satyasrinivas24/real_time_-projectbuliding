class  School_admission:
  def __init__(self):
   self.board = None
   self.medium = None
   self.class_name = None 
   self.location = None
  
  def get_medium(self,board):
    if board == "CBSE":
      return ["English","Telugu"]
    elif board == "ICSE":
      return ["English","Hindi"]
    elif board == "STATE":
      return ['Telugu']

  def get_fee(self,class_name):
    fee_structure = {
        "6" :  120000,
        "7" :  140000,
        "8" :  160000,
        "9" :  180000,
        "10":  220000


    }
    if class_name in fee_structure:
      return fee_structure[class_name]
    else:
      return 0


  def collect_inputs(self):

    vaild_board = ["CBSE","ICSE","STATE"]
    user_board = input("Choose the board:").upper()
    if user_board not in vaild_board:
      print("Invalid board you was seleted")
      
    else:
        self.board = user_board
        print("you selected:",user_board)
  
#---------------------------------------------------------------------------- 
    available_medium = self.get_medium(self.board)
    
    user_medium = input("choose the medium:").capitalize()
    if user_medium not in available_medium:
        print("Invalid medium you selected")
    else:
      self.medium = user_medium

      print("you selected:",user_medium)
#-----------------------------------------------------------------------------
    class_option = ["6","7","8","9","10"]
    self.class_name= input("Choose the class:")
    if self.class_name not in class_option:

      print("Invalid class name you selected")
       
    else:
        print("you selected:",self.class_name)
      

#-----------------------------------------------------------------------------
    self.location= input("Are you local or non-local:")
    if self.location == "local":
      print("I am :",self.location)
    else:
  
      print("I am not in :",self.location)
    return True
#-------------------------------------------------------------------------------
  def calculate_fee(self):
    school_fee = self.get_fee(self.class_name)
    if self.location == "local":
        
        return school_fee * 0.9
    else:
        return school_fee
    


#---------------------------------------------------------------------------

  def display_total(self):
      final_fee = self.calculate_fee()
      print("\n-------Admission Final Details---------")
      print(f"Board: {self.board}")
      print(f"Medium:{self.medium}")
      print(f"Class:{self.class_name}")
      print(f"Location:{self.location}")
      print(f"Total fee to be pay:{int(final_fee)}")
    
admission = School_admission()
if admission.collect_inputs():
     admission.display_total()

