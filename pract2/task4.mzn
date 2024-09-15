include "globals.mzn";

array[1..6] of var 0..9: digits;  

constraint all_different(digits);

constraint sum(digits[1..3]) = sum(digits[4..6]);

solve minimize sum(digits[1..6]);