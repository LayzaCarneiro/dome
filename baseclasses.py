import os
import subprocess as sp

OPR_HOMEPAGE = 'homepage'


#arquitecture classes
class User:
    pass

class MultChannelApp:
    def __init__(self):
        self.system = 'sys_test'  #same system for all
        self.user = 'root' #same user for all
        #self.pwd = 'pwd'  #without password in this version
        self.__SE = SecurityEngine(self) #security engine instance
    
    #navigate operations
    def homePage(self):
        return self.__SE.execute(OPR_HOMEPAGE)
                    
    #CRUD data operations
    def addData(self, data): 
        pass
    def updateData(self, data): 
        pass
    def delData(self, data): 
        pass
    def selectData(self): 
        pass
    #Meta-data operations
    def addAttribute(self, name, type, entity, notnull=False):
        opr = 'addAttribute: ' + name + '.' + type + '.' + entity #TODO
        return self.__SE.execute(opr)
       
    def delAttribute(self, name, type, entity):
        pass
    
    
class IntegrationEngine:
    def __init__(self, SE):
        self.__SE = SE

class ExternalService:
    pass

class SecurityEngine:
    def __init__(self, MUP, IE=None):
        self.__MUP = MUP #Multchannel App
        
        if IE is None:
            self.__IE = IntegrationEngine(self)
        else:
            self.__IE = IE #Integration Engine
        
        #TODO: security operations
        #...
        #user access allowed        
        self.__AC = AutonomousController(self) #autonomous controller instance

    def __authorize(self, opr):
        return True #for this experiment, all operations will be allowed

    def execute(self, opr):
        if not(self.__authorize(opr)):
            return None
        #else: authorized
        #call Autonomous Controller
        task = self.getSystem() + ': ' + self.getUser() + ': ' + opr #TODO: transform to object Task
        return self.__AC.plan(task)

    #util methods
    def getSystem(self):
        return self.__MUP.system

    def getUser(self):
        return self.__MUP.user

class AutonomousController:
    def __init__(self, SE):
        self.__SE = SE #Security Engine object
        self.__DT = DomainTransformer(self) #Domain Transform object
        self.__IC = InterfaceController(self) #Interface Controller object
        self.__AIE = AIEngine(self) #Artificial Intelligence Engine object
        
    def __monitor(self):
        pass

    def __analyze(self):
        pass
    
    def plan(self, task):
        return self.__execute(task) #in this version, all tasks are going to be executed immediately
    
    def __execute(self, task):
        #TODO: manager the type of task
        #...
        
        tasksList = [task]#.transform TODO
        return self.__DT.updateModel(tasksList)
        
    def __knowledge(self):
        pass
    
    #util methods
    def getSystem(self):
        return self.__SE.getSystem()
    
class AIEngine:
    def __init__(self, AC):
        self.__AC = AC #Autonomous Controller object
    #TODO: AI Services
    #...
    
class InterfaceController:
    def __init__(self, AC):
        self.__AC = AC #Autonomous Controller Object
        
        #starting the python virtual env
        #https://docs.python.org/3/tutorial/venv.html
        self.__venv_path = self.getSystem() + '_env'
        
        if not os.path.exists(self.__venv_path):
            print('Creating the python virtual environment...')
            os.system('python -m venv ' + self.__venv_path) #synchronous
            
        print('Activating the python virtual environment...')
        os.chdir(self.__venv_path + '\\Scripts')
        os.system('activate.bat')
        os.chdir('..\\')
        #print(os.getcwd())

        self.__webapp_path = self.getSystem() + '_web' 
        if not os.path.exists(self.__webapp_path):
            os.system('django-admin startproject ' + self.__webapp_path) #synchronous
        
        os.chdir(self.__webapp_path)
        self.webapp_process = sp.Popen(['python.exe', 'manage.py', 'runserver'], #asynchronous
                                stdout=sp.PIPE,
                                universal_newlines=True, shell=True)        
        #py manage.py startapp polls
        #os.system('dir')
        # + 
        
    #util methods
    def getSystem(self):
        return self.__AC.getSystem()



class BusinessProcessEngine:
    pass

class AnalyticsEngine:
    pass

class DomainTransformer:
    def __init__(self, AC):
        self.__AC = AC #Autonomous Controller Object
            
    def updateModel(self, tasksList):
        return 'Modelo atualizado...' + str(tasksList)