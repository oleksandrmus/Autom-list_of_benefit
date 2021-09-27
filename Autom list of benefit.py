
def list_benefits():
    list_of_benefits =["more organaized code","more readable code","easier ccode to reuse",
                            "alowing programers to share code together"]
    print (list_of_benefits)
    return list_of_benefits
list_benefits()
# build in +
def build_sentence(benefit):

    print(benefit+"is a benefit of functions!")
    return benefit + "is a benefit of functions!"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    print(build_sentence(list_of_benefits[0]))

    print(build_sentence(list_of_benefits[1]))

    print(build_sentence(list_of_benefits[2]))

    print(build_sentence(list_of_benefits[3]))


name_the_benefits_of_functions()