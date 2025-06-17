def calculator(a,b,operator):
    try:
        a=float(a)
        b=float(b)
        if operator=="+":
            return a+b
        elif operator=="-":
            return a-b        
        elif operator=="*":
            return a*b
        elif operator=="/":
            if b==0:
                return "Error:Zero division error "
            return a/b 
    except ValueError:
        return "Error: Value Error "
    except TypeError:
        return "Error : Type Error"
    except Exception as e:
        return f"Error: unexpected exception {str(e)}"
print(calculator(10,5,"/"))
print(calculator(10,"ten","+"))
print(calculator(5,3,"$"))