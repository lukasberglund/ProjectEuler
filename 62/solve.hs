digits :: Integral x => x -> [x]
digits x = if x < 10 then [x] else [mod x 10] ++ digits (div x 10)

removeIth :: [Int] -> Int -> [Int]
removeIth l i = (take (i - 1) l) ++ (drop i l)

addToEach :: Int -> [[Int]] -> [[Int]]
addToEach x l = [[x] ++ s | s <- l]

permutations :: [Int] -> [[Int]]
permutations [] = []
permutations l = sum [addToEach i (permutations (removeIth l i)) | i <- [1..(length l)]]

main = print (permutations [1,2,3])
