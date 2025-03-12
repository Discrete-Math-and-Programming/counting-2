
# Implement two versions of a powerset function.
# Both will take as input a set represented as a list of integers.
# Name the version that uses recursion powerset_rec and the version that uses
# iteration powerset_iter.



def test():

    # Test for powerset_rec

    results = {}
    test_cases =\
            {'powerset_rec': [
                ([[]],[]),
                ([[1,2,3]],[[], [1], [2], [3], [1, 2], [1, 3], [2, 3],
                                     [1, 2, 3]])],
             'powerset_iter': [
                ([[]],[]),
                ([[1,2,3]],[[], [1], [2], [3], [1, 2], [1, 3], [2, 3],
                                     [1, 2, 3]])]
            } 


    for funcname, cases  in test_cases.items():
        try:
            results[funcname] =  "OK" if all([eval(funcname)(*case[0]) == case[1] for case in cases]) else "Not OK"
        except NameError:
            results[funcname] = "Not Implemented"
        except Exception as e:
            results[funcname] = "Error -- " + str(e)

    print("Function Name            | Status")
    print("-------------------------|--------")
    for key, value in results.items():
        print(f"{key:<24} | {value}")

