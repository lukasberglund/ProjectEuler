digits :: Integer -> [Integer]
digits x = if x < 10 then [x] else [mod x 10] ++ digits (div x 10)
main = print (sum(digits (2^1000)))
