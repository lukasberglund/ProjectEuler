tri n = div (n * (n + 1)) 2
squ n = n ^ 2
pen n = div (n * ((3 * n) - 1)) 2
hex n = n * (2 * n - 1)
hep n = div (n * ((5 * n) - 3)) 2
oct n = n * (3 * n - 2)

fourD fun = [fun n | n <- [1..100], fun n >= 1000, fun n <= 9999]

fourDTri = fourD tri
fourDSqu = fourD squ
fourDPen = fourD pen
fourDHex = fourD hex
fourDHep = fourD hep
fourDOct = fourD oct

n1 = 8128
n2 = 2882
n3 = 8281
n4 = 8128

sumList [] = []
sumList l = head(l) ++ sumList (tail l)

isRot m n = (mod m 100 == div n 100)
n4Candidates l = [n | n <- l, isRot n3 n]
candidates l m = [n | n <- l, isRot m n]
n5Candidates = sumList [candidates l n4| l <- [fourDHep, fourDOct]]
n6Candidates = candidates fourDOct (n5Candidates!!0) ++ candidates fourDHep (n5Candidates!!1)
main = print n6Candidates
