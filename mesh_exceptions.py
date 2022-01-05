import time
class meshExcep:
    
 #----------UUID-------------------------------------------

    def receive_UUIDv3(self) -> bool: 
        with open("log\output.log", 'r') as f:
            data = f.read()
        if "Received UUID" in data:   
            data = data.replace("Received UUID", "Received__UUID")   
            with open("log\output.log", 'w') as w:
                w.write(data)
            return True
        else:
            print("Plug an unprovisioned device!")
            return False

    
    def checkForUUID(self):
       for _ in range(10):
           if self.receive_UUIDv3():
               return True
           time.sleep(1)
       print("No UUID was found")
       return False

#--------------Provisioning-------------------------------

    #Wat is het punt van deze functie?
    def wait_till_provisioned_succesfully(self):
        with open("log\output.log", 'r') as f:
            for line in f:
                if 'INFO' in line:
                    if "Provisioning link closed" in line:
                        print('provisioned succesfully')
                        return True
                    else:
                        print("Retry provisioning")
                        return False
 


    def provisioned_succesful(self) -> bool: 
        with open("log\output.log", 'r') as f:
            data = f.read()
        if "Provisioning link closed" in data:   
            data = data.replace("Provisioning link closed", "Provisioning_link_closed")   #functie schrijven om spaties te vervangen door '_'
            with open("log\output.log", 'w') as w:
                w.write(data)
            return True
        else:
            self.wait_till_provisioned_succesfully()
            return False

    
    def check_for_provisioning(self):
       for _ in range(10):
           if self.provisioned_succesful():
               return True
           time.sleep(1)
       print("Provisioning failed")
       return False

    

#----------------composition_data-------------------------------------------------

    def recognize_model(self) -> int:
        server = 1000
        client = 1001
        with open("log\output.log", 'r') as f:
            data = f.read()
        if '"modelId": "1000"' in data: 
            return True
        elif '"modelId": "1001"' in data:   
            return True
        else:
            print("no model founded yet")
            return False


    def check_for_model(self):
        for _ in range(10):
            if self.recognize_model():
                return True
            time.sleep(1)
        else:
            return False                   

    # def receive_compositiondata(self, recognize_model):                     
    #     with open("log\output.log", 'r') as f:
    #         for line in f:
    #             if not 'INFO' in line:
    #                 if "modelId" in line:
    #                     index = line.index(f'modelId :{model}')
    #                     buffer = line[index + 11:]
    #                     out = buffer.split('"')[0]
    #                     print(out)
    #                     print(f'compositiondata for model {model} succesful received')


#-----------------add_appkey---------------------------------------------------------------------------

    
    def receive_appkey(self, appkey: int): 
        with open("log\output.log", 'r') as f:
            data = f.read()
        if (f'Appkey add {appkey}') in data:   
            data = data.replace("Appkey add", "Appkey_add")   
            with open("log\output.log", 'w') as w:
                w.write(data)
            return True
        else:
            print("no appkey added yet")
            return False

    
    def check_for_appkey(self):
       for _ in range(10):
           if self.receive_appkey(0):
               return True
           time.sleep(1)
       print("No appkey")
       return False

# def appkey_added(self, appkey: int, subnet: int, node: int): #hex number voor model moet worden gefixt
#         with open("log\output.log", 'r') as f:
#             for line in f:
#                 if 'INFO' in line:
#                     if "Appkey add" in line:
#                         index = line.index(f'Appkey add {numbApp} succeded for subnet {subnet} at node {node}')
#                         buffer = line[index + 11:]
# #                        out = buffer.split('s')[0]
#                         print(buffer)
#                         print(f'appkey: {numbApp} added succesfully')


#--------------------bind_appkey-------------------------------------------------------------------------
    def appkey_bind(self, appkey: int): 
        with open("log\output.log", 'r') as f:
            data = f.read()
        if (f'Appkey bind {appkey}') in data:   
            data = data.replace("Appkey bind", "Appkey_bind")   
            with open("log\output.log", 'w') as w:
                w.write(data)
            return True
        else:
            print("Appkey not binded yet")
            return False

    
    def check_for_binding(self):
       for _ in range(10):
           if self.appkey_bind(0):
               return True
           time.sleep(1)
       print("no binding")
       return False

        
#     def appkey_binded(self, numbApp: int, model: int, node: int): #hex number voor model en node has to be fixed..
#         with open("log\output.log", 'r') as f:
#             for line in f:
#                 if 'INFO' in line:
#                     if "Appkey bind" in line:
#                         index = line.index(f'Appkey bind {numbApp} to model {model} at {node}')
#                         buffer = line[index + 12:]
# #                       out = buffer.split('s')[0]
#                         print(buffer)
#                         succes = print(f'appkey {numbApp} binded succesfully')
#         return succes

 


 
def main():
    a = meshExcep()
#    a.receive_UUID()
#     #a.no_UUID()
#     a.UUID_received("Received UUID")
#     #a.provisioned_succesful()
#    a.receive_compositiondata(1000)
#   a.receive_compositiondata()
#    a.appkey_added()
#    a.appkey_binded(0, 1000, 999)
 #   a.receive_UUIDv1()
#  a.receive_UUIDv2()
  #  print(a.receive_UUIDv3())
  #  a.recognize_model()
  #  a.check_for_model()
    # a.receive_UUIDv5()
    # a.removeDuplicate()
    #a.no_model_found()
    a.check_for_appkey()
   # a.check_for_binding()


if __name__ == '__main__':
    main()
            





# file = open ("log\output.log")
# print(file.read())
# search_word = "Received UUID"
# if(search_word in file.read()):
#     print("word founc")
# else:
#     print("word not found")


#----------------------UUIDs------------------
   # def receive_UUID(self):
    #   #  print("UUID succes")
    #     with open("log\output.log", 'r') as f:
    #         for line in f:
    #             if 'INFO' in line:
    #                 if "Received UUID" in line:
    #                     succes = print('UUID succesful received')
    #     return succes


    # def receive_UUIDv1(self): 
    #     with open("log\output.log", 'r') as f:
    #         for line in f:
    #             if 'INFO' in line:
    #                 if "Received UUID" in line:
    #                     index = line.index("Received")
    #                     buffer = line[index + 14:]
    #                     out = buffer.split("with")[0]
    #                     print(buffer)
    #                     succes = print(f'received UUID: {buffer} succesfully')
    #     return succes

#---------------UUID received. UUID wordt in een lijst gezet en die lijst wordt steeds vergeleken met nieuwe binnenkomende UUIDS's
    # def receive_UUIDv2(self): 
    #     UUID_list = []
    #     with open("log\output.log", 'r') as f:
    #         for line in f:
    #             if 'INFO' in line:
    #                 if "Received UUID" in line:                    
    #                     index = line.index("Received")
    #                     buffer = line[index + 14:]
    #                     out = buffer.split("w")[0]
    #                     for i in range(0, len(UUID_list)):
    #                         if UUID_list[i] == out:                               
    #                             return False
    #                     UUID_list.append(out)
    #     return True


#---------------UUID received maar wat te doen bij 2e UUID------------------
    # def receive_UUIDv4(self) -> bool: 
    #     with open("log\output.log", 'r') as f:
    #         for line in f:
    #             if 'INFO' in line:
    #                 if "Received UUID" in line:     
    #                     return True
                        
    #     return False


#------------remove duplicates-----------------------------------------
    # def removeDuplicate(str):
    #     self.meshExcep = meshExcep()
    #     s=set(str)
    #     s="".join(s)
    #     print("Without Order:",s)
    #     t=""
    #     for i in str:
    #         if(i in t):
    #             pass
    #         else:
    #             t=t+i
    #         print("With Order:",t)
      
    # str= receive_UUIDv5(self).UUID_list
    # removeDuplicate(str)
#--------------------------------------------------------

#------of dit voor de UUID-------------------       #check voor UUID
    # def UUID_received(self, name : str)->int:
    #     self.LOGFILE_PATH = 'log\output.log'
    #     out = 0

    #     with open(self.LOGFILE_PATH, 'r') as f:
    #         for line in f:
    #             if "INFO" in line:
    #                 if name in line:
    #                     index = line.index(name)
    #                     buffer = line[index + 14:]
    #                     out = int(buffer.split("w")[0]) 

    #         return out
#------------------------------------------------
    # def provisioned_succesful(self) -> bool:
    #     with open("log\output.log", 'r') as f:
    #         for line in f:
    #             if 'INFO' in line:
    #                 if "Provisioning link closed" in line:
    #                     print('provisioned succesfully!')
    #                     time.sleep(0.5)
    #                     return True
    #                 else:
    #                     return False