

def tokenize(code):
    """
    tokenize the incoming string into a list of tokens.
    "(" ")" dont typically have spaces before and after so we should replace
    them with a padded version. This will help in tokenizing the string.
    """
    return code.replace("(", " ( ").replace(")", " ) ").split()




def parse_lisp(tokenized_code):
    """
    Returns the abstract syntax tree (AST) of the lisp code provided
    This is really rudimentary in its implementation

    I don't think I'm capturing all the possible errors here:
        - if we have extra ")" we end up exiting the loop early
    """
    output = []
    token = tokenized_code.pop(0)
    #we should never enter the function with a close bracket
    #as it will get captured in the while loop
    if token == ")":
        raise Exception("Misplaced ')'")
    #enter th recursive section
    if token == "(":
        try:
            while tokenized_code[0] != ")":
                #call itself to get the basic element
                output.append(parse_lisp(tokenized_code))
            #remove the ")"
            tokenized_code.pop(0)
        except Exception:
            raise Exception("Misplaced '('")
        return output
    #base case where the smallest value is just an element
    else:
        return token



if __name__ == '__main__':
    code = "(first (list (+ 1 3) (+ 2 3) 9 10))"
    print parse_lisp(tokenize(code))
