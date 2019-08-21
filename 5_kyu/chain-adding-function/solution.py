# visit: https://www.codewars.com/kata/a-chain-adding-function/python

# Custom integer class, defines __call__ which returns which returns instance of itself 
# with update value
class Custom(int):
    def __call__(self, v):
        return Custom(self + v)
    
# define our function which returns a Custom instance and passes our value 
def add(v):
    return Custom(v)