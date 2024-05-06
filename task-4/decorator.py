import re

class PhoneValidationError(ValueError):
    pass

class NameValidationError(ValueError):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            name, phone = args[0]
            
            if not re.match(r'^[a-zA-Zа-яА-Я]+$', name): # chack name for only 
                raise NameValidationError

            if not re.match(r'^\d{10,}$', phone):
                raise PhoneValidationError
            
            return func(*args, **kwargs)
        
        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        except KeyError:
            print ("Enter user name")
        except ValueError:
            print ("Give me name and phone please")
        except IndexError:
            print ("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner

def input_error_name(func):
    def inner(*args, **kwargs):
        try:
            name, = args[0]
            
            if not re.match(r'^[a-zA-Zа-яА-Я]+$', name): # chack name for only 
                raise NameValidationError
            
            return func(*args, **kwargs)
        
        except PhoneValidationError:
            print('Invalid phone number. Phone number should contain only digits and be at least 10 digits long.')
        except NameValidationError:
            print("Invalid name. Name should contain only letters.")
        except KeyError:
            print ("Enter user name")
        except ValueError:
            print ("Give me name and phone please")
        except IndexError:
            print ("Missing arguments")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")

    return inner