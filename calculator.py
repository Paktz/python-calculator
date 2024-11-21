class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # Changed from b - a 

    def multiply(self, a, b):
        result = 0
        absolute_b = b
        nf = 1
        if b < 0:
            absolute_b = self.subtract(0, b)
            nf = self.subtract(0, 1) 
        for i in range(absolute_b):
            result = self.add(result,a)
        if nf > 0:
            return result
        else: return self.subtract(0, result)
        
    def divide(self, a, b):
        result = 0
        if(b == 0):
            return "undefined"
        while a >= b: # Changed from a > b
            if b < 0:
                a = self.add(a, b)
                result -= 1
            else:
                a = self.subtract(a, b)
                result += 1
        while a <= b: # Changed from a > b
            if a == 0:
                break
            # result -= 1
            if (a < 0)&(b < 0):
                a = self.subtract(a, b)
                result += 1
            else:
                a = self.add(a, b)
                result -= 1
        return result
    def modulo(self, a, b):
        if b == 0:
            return "undefined"
        
        abs_a = a if a >= 0 else self.subtract(0, a)
        abs_b = b if b >= 0 else self.subtract(0, b)
        
        # Subtract b from a until we can't anymore
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            
        # Apply the sign of the original dividend
        return abs_a if a >= 0 else self.subtract(0, abs_a)

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))