
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Convert both numbers to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract divisor multiplied by powers of 2
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient
