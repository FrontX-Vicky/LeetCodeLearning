# Test Cases for Trie (Prefix Tree) Problems
# Run: python test_cases.py

from main import (
    Trie, TrieNode, WordDictionary, findWords,
    longestCommonPrefix, replaceWords, WordFilter
)


class TestRunner:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.current_problem = ""
    
    def set_problem(self, name):
        self.current_problem = name
        print(f"\n{'=' * 60}")
        print(f"Testing: {name}")
        print('=' * 60)
    
    def test(self, result, expected, test_name):
        self.tests_run += 1
        
        # Handle list comparison (order may vary)
        if isinstance(result, list) and isinstance(expected, list):
            result_sorted = sorted(result)
            expected_sorted = sorted(expected)
            passed = result_sorted == expected_sorted
        else:
            passed = result == expected
        
        if passed:
            self.tests_passed += 1
            print(f"✓ {test_name}")
        else:
            print(f"✗ {test_name}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    def summary(self):
        print(f"\n{'=' * 60}")
        print(f"SUMMARY: {self.tests_passed}/{self.tests_run} tests passed")
        percentage = (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0
        print(f"Success Rate: {percentage:.1f}%")
        print('=' * 60)


def test_trie():
    runner = TestRunner()
    runner.set_problem("PROBLEM 1: IMPLEMENT TRIE")
    
    # Test 1: Basic insert and search
    trie = Trie()
    trie.insert("apple")
    runner.test(trie.search("apple"), True, "Test 1: Search inserted word")
    
    # Test 2: Search non-existent word
    runner.test(trie.search("app"), False, "Test 2: Search prefix (not full word)")
    
    # Test 3: StartsWith prefix
    runner.test(trie.startsWith("app"), True, "Test 3: StartsWith existing prefix")
    
    # Test 4: Insert and search again
    trie.insert("app")
    runner.test(trie.search("app"), True, "Test 4: Search after second insert")
    
    # Test 5: Multiple words
    trie2 = Trie()
    trie2.insert("cat")
    trie2.insert("car")
    trie2.insert("dog")
    runner.test(trie2.search("cat"), True, "Test 5a: Search 'cat'")
    runner.test(trie2.search("car"), True, "Test 5b: Search 'car'")
    runner.test(trie2.search("dog"), True, "Test 5c: Search 'dog'")
    runner.test(trie2.startsWith("ca"), True, "Test 5d: Prefix 'ca'")
    
    # Test 6: Empty prefix
    runner.test(trie2.startsWith(""), True, "Test 6: Empty prefix (always true)")
    
    # Test 7: Non-existent prefix
    runner.test(trie2.startsWith("z"), False, "Test 7: Non-existent prefix")
    
    # Test 8: Partial match
    runner.test(trie2.search("ca"), False, "Test 8: Partial word not found")
    
    return runner


def test_word_dictionary():
    runner = TestRunner()
    runner.set_problem("PROBLEM 2: ADD AND SEARCH WORDS")
    
    # Test 1: Basic operations
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    
    runner.test(wd.search("pad"), False, "Test 1: Search non-existent")
    runner.test(wd.search("bad"), True, "Test 2: Search exact word")
    
    # Test 3: Wildcard at start
    runner.test(wd.search(".ad"), True, "Test 3: Wildcard at start '.ad'")
    
    # Test 4: Multiple wildcards
    runner.test(wd.search("b.."), True, "Test 4: Multiple wildcards 'b..'")
    
    # Test 5: All wildcards
    runner.test(wd.search("..."), True, "Test 5: All wildcards '...'")
    
    # Test 6: Wildcard mismatch
    runner.test(wd.search("..d"), True, "Test 6: Wildcard '..d'")
    
    # Test 7: Wrong length
    runner.test(wd.search("...."), False, "Test 7: Too many chars")
    
    # Test 8: Single character
    wd2 = WordDictionary()
    wd2.addWord("a")
    runner.test(wd2.search("."), True, "Test 8: Single wildcard")
    
    # Test 9: Mixed pattern
    wd3 = WordDictionary()
    wd3.addWord("at")
    wd3.addWord("and")
    wd3.addWord("an")
    wd3.addWord("add")
    runner.test(wd3.search("a"), False, "Test 9a: Exact 'a'")
    runner.test(wd3.search(".at"), False, "Test 9b: Pattern '.at'")
    runner.test(wd3.search("an."), True, "Test 9c: Pattern 'an.'")
    runner.test(wd3.search("a.d"), True, "Test 9d: Pattern 'a.d'")
    
    return runner


def test_find_words():
    runner = TestRunner()
    runner.set_problem("PROBLEM 3: WORD SEARCH II")
    
    # Test 1: Standard example
    board1 = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words1 = ["oath","pea","eat","rain"]
    result = findWords(board1, words1)
    runner.test(result, ["eat","oath"], "Test 1: Standard board")
    
    # Test 2: Single word
    board2 = [['a','b'],['c','d']]
    words2 = ["abcb"]
    result = findWords(board2, words2)
    runner.test(result, [], "Test 2: Invalid path (revisit cell)")
    
    # Test 3: All words found
    board3 = [['a','a']]
    words3 = ["a","aa"]
    result = findWords(board3, words3)
    runner.test(result, ["a","aa"], "Test 3: Multiple matches")
    
    # Test 4: No words found
    board4 = [['a','b'],['c','d']]
    words4 = ["xyz"]
    result = findWords(board4, words4)
    runner.test(result, [], "Test 4: No words found")
    
    # Test 5: Single cell
    board5 = [['a']]
    words5 = ["a"]
    result = findWords(board5, words5)
    runner.test(result, ["a"], "Test 5: Single cell match")
    
    return runner


def test_longest_common_prefix():
    runner = TestRunner()
    runner.set_problem("PROBLEM 4: LONGEST COMMON PREFIX")
    
    # Test 1: Standard case
    runner.test(longestCommonPrefix(["flower","flow","flight"]), "fl", 
                "Test 1: Standard LCP")
    
    # Test 2: No common prefix
    runner.test(longestCommonPrefix(["dog","racecar","car"]), "", 
                "Test 2: No common prefix")
    
    # Test 3: Single string
    runner.test(longestCommonPrefix(["hello"]), "hello", 
                "Test 3: Single string")
    
    # Test 4: Empty array
    runner.test(longestCommonPrefix([]), "", 
                "Test 4: Empty array")
    
    # Test 5: All same
    runner.test(longestCommonPrefix(["test","test","test"]), "test", 
                "Test 5: All identical")
    
    # Test 6: One empty string
    runner.test(longestCommonPrefix(["hello","","world"]), "", 
                "Test 6: Contains empty string")
    
    # Test 7: Prefix is entire first word
    runner.test(longestCommonPrefix(["a","ab","abc"]), "a", 
                "Test 7: Prefix is shortest word")
    
    # Test 8: Two strings
    runner.test(longestCommonPrefix(["abc","abcd"]), "abc", 
                "Test 8: Two strings")
    
    return runner


def test_replace_words():
    runner = TestRunner()
    runner.set_problem("PROBLEM 5: REPLACE WORDS")
    
    # Test 1: Standard case
    dict1 = ["cat","bat","rat"]
    sent1 = "the cattle was rattled by the battery"
    expected1 = "the cat was rat by the bat"
    runner.test(replaceWords(dict1, sent1), expected1, 
                "Test 1: Standard replacement")
    
    # Test 2: No replacements
    dict2 = ["a","b","c"]
    sent2 = "aadsfasf absbs bbab cadsfafs"
    expected2 = "a a b c"
    runner.test(replaceWords(dict2, sent2), expected2, 
                "Test 2: All words replaced")
    
    # Test 3: No matches
    dict3 = ["cat","bat","rat"]
    sent3 = "the dog was happy"
    expected3 = "the dog was happy"
    runner.test(replaceWords(dict3, sent3), expected3, 
                "Test 3: No matches")
    
    # Test 4: Multiple roots for same word
    dict4 = ["a","aa","aaa"]
    sent4 = "aaaa"
    expected4 = "a"
    runner.test(replaceWords(dict4, sent4), expected4, 
                "Test 4: Choose shortest root")
    
    # Test 5: Empty dictionary
    dict5 = []
    sent5 = "hello world"
    expected5 = "hello world"
    runner.test(replaceWords(dict5, sent5), expected5, 
                "Test 5: Empty dictionary")
    
    return runner


def test_word_filter():
    runner = TestRunner()
    runner.set_problem("PROBLEM 6: PREFIX AND SUFFIX SEARCH")
    
    # Test 1: Basic case
    wf1 = WordFilter(["apple"])
    runner.test(wf1.f("a", "e"), 0, "Test 1: Basic match")
    
    # Test 2: Multiple words
    wf2 = WordFilter(["apple", "banana", "application"])
    runner.test(wf2.f("app", "e"), 2, "Test 2: Return highest index")
    runner.test(wf2.f("a", "a"), 1, "Test 2b: Banana match")
    
    # Test 3: No match
    wf3 = WordFilter(["apple"])
    runner.test(wf3.f("b", "e"), -1, "Test 3: No match")
    
    # Test 4: Empty prefix/suffix
    wf4 = WordFilter(["test"])
    runner.test(wf4.f("", "t"), 0, "Test 4: Empty prefix")
    runner.test(wf4.f("t", ""), 0, "Test 4b: Empty suffix")
    
    # Test 5: Duplicate words (later index)
    wf5 = WordFilter(["apple", "app", "apple"])
    runner.test(wf5.f("a", "e"), 2, "Test 5: Duplicate word, return later index")
    
    return runner


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TRIE (PREFIX TREE) - TEST SUITE")
    print("=" * 60)
    
    all_runners = []
    
    # Run all tests
    all_runners.append(test_trie())
    all_runners.append(test_word_dictionary())
    all_runners.append(test_find_words())
    all_runners.append(test_longest_common_prefix())
    all_runners.append(test_replace_words())
    all_runners.append(test_word_filter())
    
    # Overall summary
    total_tests = sum(r.tests_run for r in all_runners)
    total_passed = sum(r.tests_passed for r in all_runners)
    
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_tests - total_passed}")
    percentage = (total_passed / total_tests * 100) if total_tests > 0 else 0
    print(f"Success Rate: {percentage:.1f}%")
    print("=" * 60)
    
    # Grade
    if percentage >= 95:
        grade = "A+"
    elif percentage >= 90:
        grade = "A"
    elif percentage >= 85:
        grade = "B+"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 75:
        grade = "C+"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "D"
    
    print(f"\nGrade: {grade}")
    print("=" * 60)
