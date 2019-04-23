def course_grader(test_scores):
    test_avg = sum(test_scores)/len(test_scores)
    
    if test_avg >= 70 and min(test_scores) > 50:
        return("pass")
    elif test_avg < 70 or min(test_scores) <= 50:
        return("fail")

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
    main()
