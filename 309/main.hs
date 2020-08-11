import Data.List (sortOn)

-- The problem can be found here https://projecteuler.net/problem=309

testMaxY :: Int
testMaxY = 200

maxY :: Int
maxY = 1000000

main = do
  print $ length $ findSolutions $ prtnByLegs $ findTriples $ maxY

type Triple = (Int, Int, Int)

showSolution :: (Triple, Triple) -> Triple
showSolution ((w, s, x), (w', t, y)) = (x, y, h)
  where
    h = (s * t) `div` (s + t)

-- Given all pythagorean triples, find all pairs of triples that represent a
-- solution to the problem
findSolutions :: [[Triple]] -> [(Triple, Triple)]
findSolutions triples = concatMap getSolutions triples
  where
    getSolutions :: [Triple] -> [(Triple, Triple)]
    getSolutions (x:xs) = getSolutions xs ++ (makePair x <$> filter (isSolution x) xs)
    getSolutions [] = []
    isSolution :: Triple -> Triple -> Bool
    isSolution (w, s, x) (w', t, y) = (s * t) `mod` (s + t) == 0
    makePair :: a -> b -> (a, b)
    makePair x y = (x, y)

-- Partition the triples into sublists to where the first leg is the same
prtnByLegs :: [Triple] -> [[Triple]]
prtnByLegs triples = prtnNghbrsOn first $ sortOn first $ triples ++ legsFlipped
  where
    legsFlipped = map (\(a, b, c) -> (b, a, c)) triples
    first (a, _, _) = a


-- Partition a list into groups of neighbors such that the neighbors match when
-- inputed into the given function. Ex:
--    prtnNghbrsOn even [1, 2, 4, 3, 9, 2] -> [[1], [2, 4], [3, 9], [2]]
prtnNghbrsOn :: (Eq b) => (a -> b) -> [a] -> [[a]]
prtnNghbrsOn f = foldl g []
  where
    g [] x = [[x]]
    g acc@(xs:xss) x = if (f (head xs)) == f x then (x:xs):xss else [x]:acc

-- Find all pythagorean triples (a, b, c) where a^2 + b^2 = c^2 and c < x using
-- euclids formula. Info can be found here
--  https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
findTriples :: Int -> [Triple]
findTriples x = concatMap triplesFromCoprimes validCoprimes
  where
    genTriple :: Int -> Int -> Int -> Triple
    genTriple m n k =
      (k * (m ^ 2 - n ^ 2), k * (2 * m * n), k * (m ^ 2 + n ^ 2))
    triplesFromCoprimes :: (Int, Int) -> [Triple]
    triplesFromCoprimes (m, n) =
      map (genTriple m n) [1 .. (x - 1) `div` (m ^ 2 + n ^ 2)]
    notBothOdd :: (Int, Int) -> Bool
    notBothOdd (x, y) = (even x || even y)
    validCoprimes = filter notBothOdd $ genCoprimes x


-- Generate all pairs (m, n) such that m and n are coprimes, m > n > 0
-- and m ^2 + n^2 <= x. Algorithm can be found here
-- https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs
genCoprimes :: Int -> [(Int, Int)]
genCoprimes x = concatMap fromRoot [(2, 1), (3, 1)]
  where
    fromRoot :: (Int, Int) -> [(Int, Int)]
    fromRoot (m, n) =
      (m, n) :
      concatMap fromRoot (filter (\(m, n) -> m ^ 2 + n ^ 2 < x) branches)
      where
        branches = [(2 * m - n, m), (2 * m + n, m), (m + 2 * n, n)]
