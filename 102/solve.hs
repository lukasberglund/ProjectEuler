

triangles = (lines contents)
firstOcc str ',' = [i | i <- [0 .. length str], str !! i == ','] !! 0

main = do
    contents <- readFile "p102_triangles.txt"
    
