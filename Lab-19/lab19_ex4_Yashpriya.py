def union_and_intersection():
#Make a set of all the vowels
    vowels={'a','e','i','o','u'}
#Make a set of all the consonants
    consonants={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
#Merge/unite the vowels & consonants & store in set called 'alpha'
    alpha=vowels.union(consonants)
    print(f"The alpha set (after union of vowels & consonants) looks like: {alpha}")

#Make a set containing digits from 0 to 9
    numeric={0,1,2,3,4,5,6,7,8,9}
#Merge these digits with the above 'alpha' set containing both vowels & consonants
    alphanumeric=alpha.union(numeric)
    print(f"The alphanumeric set (after union of alpha & digits) looks like: {alphanumeric}")

#Compute the difference between 'alpha' set & 'vowels' set
# (vowels+consonants)-vowels = consonants
    difference=alpha-vowels
    print(f"The difference between alpha & vowels: {difference}")

#Compute the difference between the above output & 'consonants' set
# consonants - consonants = empty set
    diff=difference-consonants
    print(f"The difference between the above output & consonants: {diff}")

#To check the intersecting/same elements in 'vowels' set & 'consonants' set
# There is no such intersecting elements between them.
    intersection=vowels.intersection(consonants)
    print(f"The output of intersection of vowels with consonant sets: {intersection}")

#To check the intersecting/same elements in 'vowels' set & 'alphanumeric' set
# Only the vowels are common in both the sets
    intersect=vowels.intersection(alphanumeric)
    print(f"The output of intersection of vowels with alphanumeric sets: {intersect}")

def main():
    union_and_intersection()
if __name__ == "__main__":
    main()