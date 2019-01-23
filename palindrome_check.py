def test_suite():
    for tst, exp in test_inputs.items():
        actual = check_palindrome(tst)
        if actual == exp:
            print("OK")
        else:
            print("NOK")

# Returns reverse of a String			
def reverse_string(string):
	reverse = ""
		
	for index in range(len(string)-1, -1, -1):
		reverse = reverse+string[index]
		
	return reverse
			
def check_palindrome(string):
	"""
		This checks if the given input string is a palindrome
		It returns True if the input string is a palindrome
		It returns False if the input string is not a palindrome
	"""
	if string == reverse_string(string):
		return True
	else:
		return False
		
		
# Main test cases
test_inputs = \
    {
        "radar" : True, # test string : expected status
        "panama" : False,
        "Madman" : False,
        "TCATGAACGTCTTCTGCAAGTACT" : True,
        "GACATACTCCTCCACCTCATACAG" : False,
    }


test_suite()