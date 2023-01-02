# intent mapping
# >>>>> !!! DON'T CHANGE THE KEYS OF THE INTENT_MAP !!! <<<<<
# >>>>> !!! KEEP ALL ELEMENTS OF THE VALUE LISTS IN LOWER CASE !!! <<<<<
import os

INTENT_MAP = {
    'GREETING': {'greeting', 'greetings', 'hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening'},
    'ADD': {'add', 'create', 'insert', 'include', 'put', 'define', 'register', 'record'},
    'UPDATE': {'update', 'change', 'modify', 'alter', 'edit', 'correct', 'revise', 'replace', 'renew', 'redefine'},
    'READ': {'read', 'show', 'list', 'search', 'find', 'select', 'get', 'retrieve', 'fetch', 'view', 'give', 'display'},
    'DELETE': {'delete', 'remove', 'destroy', 'del', 'erase', 'kill'},
    'CANCELLATION': {'cancellation', 'cancel', 'stop', 'quit', 'exit'},
    'CONFIRMATION': {'confirmation', 'confirm', 'ok', 'yes'},
    'HELP': {'help', 'know'},
    'GOODBYE': {'bye', 'goodbye'},
    'MEANINGLESS': {'unknown', 'unintelligible', 'unrecognized', 'meaningless', 'uninterpretable'}
}

USELESS_EXPRESSIONS_FOR_INTENT_DISCOVERY = ['please', 'i want to', 'i want', 'could you', 'can you']

# bot msgs
MISUNDERSTANDING = [
    """Um. I don't recognize it. Which operation do you want to do? Save, update, delete or get some information? (
    say 'help' for samples) """
    ,
    """Sorry, but I didn't get it. Try something like 'register new student' or 'get student information gender=Male' 
    (say 'help' for more samples) """
    , "Please, repeat in another way, because I didn't get it. (say 'help' for more info)"]

GREETINGS = ["Hi! You can say something like 'Save student with name=Anderson'",
             "Hello! Please say something like 'Get student with name=Anderson'",
             "Hello! Good see you here! Please say some data operation like 'Include student with name=Anderson, "
             "email=andersonmg@gmail.com' "
             ]

BYE = ["Ok! Thank you. See you next time!",
       "Thank you so much. I stand at your disposal.",
       "Thank you! If you need add some info, please text me."
       ]

HELP = ["""I'm a bot that helps you add your information in an organized, secure, and flexible way. Say what you 
want to add, update, delete or only get info. \nFor example, say something like 'add a class with 
name=Self-Adaptive Systems', 'view classes', or 'delete class name=Java'. """,
        """I'm a bot that allows you to add your information using natural language. Like a traditional system, 
    but more accessible and flexible. \nFor instance, to register a student, say 'add student with gender=Female, 
    name=Mary, email=mary@school.com' or 'delete student name=Mary'. """,
        """I'm your bot that securely saves your information. I understand better direct sentences. \nThus let me know 
    first what you want to do (add, read or delete some data), what type the information you want to operate (a 
    student, a class, a class registration, etc.), and, finally, the data itself. \nSome examples: 'add class 
    registration with student=Anderson, class=Python', 'delete registration student=Anderson', 'get info about the 
    class=Python'. """
        ]

CANCEL = ['No problem! The operation was canceled successfully.']

CANCEL_WITHOUT_PENDING_INTENT = ['There is no operation to cancel.']

CONFIRMATION_WITHOUT_PENDING_INTENT = ['There is no operation to confirm.']

ASK_CONFIRM = ['OK to confirm current operation;\nCANCEL to cancel. ;)]',
               "[Any time you can say 'ok' to confirm the operation, or 'cancel' to cancel the current operation]"
               ]

ATTRIBUTE_FORMAT = [
    "I'll understand better if the data is in the following format:\n<<data name>> = <<data value>>\nFor "
    "example:\nage = 21"]

ATTRIBUTE_FORMAT_FIRST_ATTEMPT = lambda opr, clas: [
    f"Ok! We are going to <b>{opr}</b> a <b>{clas}</b>. Please, now inform the data in the following format:\n<<data name>> = "
    f"<<data value>>\nFor example:\nage = 21"]

ATTRIBUTE_OK = lambda opr, clas: [f"Ok! I got it!\nWe are going to <b>{opr}</b> a <b>{clas}</b>.\nSay 'Ok' to confirm\n'Cancel' to "
                                  f"cancel this operation."]

SAVE_SUCCESS = ['Ok! Information saved successfully!',
                'It done! Information saved. ;)',
                "Yes! All done. We've saved your data with security."]

DELETE_SUCCESS = lambda n_del: [f"Ok! <b>{n_del}</b> registers deleted.",
                                f"Done! <b>{n_del}</b> deleted.",
                                f"<b>{n_del}</b> registers deleted successfully."
                                ]

DELETE_FAILURE = ['Nothing to delete. Please, try again.']

NO_REGISTERS = ['There are no info to show.']

LIMIT_REGISTERS = 10  # limit of registers to show

LIMIT_REGISTERS_MSG = "A maximum of <b>" + str(LIMIT_REGISTERS) + \
                      "</b>  registers are shown. Apply filters to a more accurate search."

CLASS_NOT_IN_DOMAIN = lambda clas: [f"There is no information about <b>'{clas}'</b> saved. \nPlease, try something else."]

MISSING_CLASS = [
    "Would you please inform me of the information type that you want to operate? For instance, if you are trying to "
    "add data about a student, say 'student'.\n(If you wish to cancel this operation, say 'cancel'.)"]
MULTIPLE_CLASSES = ['Please, try to inform the information type with only one word or between "...", ok?']

GENERAL_FAILURE = '[ERROR] Sorry, but I could not complete the operation because of an internal error. Please, ' \
                  'try again using other words. '

# config variables
MANAGED_SYSTEM_NAME = 'managedsys'
SUFFIX_ENV = '_env'
SUFFIX_CONFIG = '_config'
SUFFIX_WEB = '_web'
WEBAPP_HOME_URL = 'http://localhost/admin'
RUN_WEB_SERVER = True

PNL_GENERAL_THRESHOLD = 0.75

TIMEOUT_MSG_PARSER = 60  # seconds

DEBUG_MODE = False

USE_PARSER_CACHE = True

if DEBUG_MODE:
    TIMEOUT_MSG_PARSER = 999999

# django default user
DJANGO_SUPERUSER_DEFAULT_USERNAME = 'admin'
DJANGO_SUPERUSER_DEFAULT_PASSWORD = 'admin'
DJANGO_SUPERUSER_DEFAULT_EMAIL = 'admin@t2s.org'

# Hugging Face token
HUGGINGFACE_TOKEN = os.environ['HUGGINGFACE_TOKEN']
