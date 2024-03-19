1. In my class i would have the following attributes:

-numerator: This attribute stores the numerator of the fractional part. It can be of type bigNum to handle arbitrary precision.
-denominator: This attribute stores the denominator of the fractional part. Also of type bigNum, it ensures accurate representation of fractions with large denominators.
-precision: This attribute stores the number of decimal places in the fractional part, it can be of type int.
-sign: This attribute stores the sign of the fractional number ('+' for positive, '-' for negative). It can be of type str.

2. To determine the integer and fractional portions of A string (e.g., '123.456'), i would split the string at the decimal point ('.'). The part before the decimal point is the integer portion, and the part after is the fractional portion.

3. The fractional part of the number can be stored using a bigNum to help with precision. Both integer and fractional parts are stored similarly, but the fractional part needs tracking to distinguish between integer and fractional values.

4. I would modify the __add__() method for this fractional class by handle addition of both integer and fractional parts separately. This would maintain precision by considering the number of decimal places in the result, and handle carry-over from the fractional part to the integer part.

-Drake Landon 
c0870202
