import Data.Char

largestSequence :: Int -> [Int] -> Int
largestSequence _ [] = 0
largestSequence n digits
  | length firstN == n && start /= 0 = findLargest start start digits rest
  | otherwise = largestSequence n $ tail digits
  where
    firstN = take n digits
    start = product firstN
    rest = drop n digits

    findLargest :: Int -> Int -> [Int] -> [Int] -> Int
    findLargest largest _ _ [] = largest

    findLargest largest current (x:xs) (0:ys) =
      let otherLargest = largestSequence n ys
      in if largest > otherLargest then largest else otherLargest

    findLargest largest current front@(x:xs) back@(y:ys)
      = findLargest newLargest next xs ys
      where
        next = current `div` x * y
        newLargest = if next > largest then next else largest



main = do
  digits <- map digitToInt <$> filter isDigit <$> readFile "input.txt"
  print $ largestSequence 13 digits
