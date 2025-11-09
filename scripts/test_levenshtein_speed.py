if __name__ == "__main__":
    from Levenshtein import distance
    import time as t

    test1="Muhammad"
    test2="Mohammed"

    t0=t.time()
    for i in range(100000):
        dist = distance(test1,test2)

    print(f"Computed d={dist} a 100000 times in {round(t.time()-t0,2)} seconds.")