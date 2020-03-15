{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red109\green109\blue109;\red32\green32\blue32;\red117\green114\blue185;
\red191\green100\blue38;\red153\green168\blue186;\red160\green0\blue163;\red128\green63\blue122;\red88\green118\blue71;
\red254\green187\blue91;\red86\green132\blue173;}
{\*\expandedcolortbl;;\csgenericrgb\c42745\c42745\c42745;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c45882\c44706\c72549;
\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c60000\c65882\c72941;\csgenericrgb\c62745\c0\c63922;\csgenericrgb\c50196\c24706\c47843;\csgenericrgb\c34510\c46275\c27843;
\csgenericrgb\c99608\c73333\c35686;\csgenericrgb\c33725\c51765\c67843;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf2 \cb3 #\
#  Homework 12 - Binary Heap\
#\
#  Problem: Binary Heap Class\
#\
#  Prompt: Create a Heap class/constructor\
#\
#  The Heap will take in the following input:\
#\
#                type: argument should be either 'min' or 'max'. This will\
#                      dictate whether the heap will be a minheap or maxheap.\
#                      The comparator method will be affected by this\
#                      argument. See method description below\
#\
#  The Heap will have the following property:\
#\
#             storage: list\
#\
#                type: \cf4 property\cf2  that will be either 'min' or 'max'. This will\
#                      be dictated by\
#\
#  The Heap will have the following methods:\
#\
#             compare: takes in two arguments (a and b). Depending on the heap\
#                      type (minheap or maxheap), the comparator will behave\
#                      differently. If the heap is a minheap, then the compare\
#                      function will return true if a is less than b, false\
#                      otherwise. If the heap is a maxheap, then the compare\
#                      function will return true if a is greater than b, false\
#                      otherwise.\
#\
#                swap: takes in two indexes and swaps the elements at the two\
#                      indexes in the storage list\
#\
#                peak: returns the peak element of the storage list. This\
#                      will be the most minimum and maximum element for a\
#                      minheap and maxheap respectively\
#\
#                size: returns the number of elements in the heap\
#\
#              insert: inserts a value into the heap. Should begin by pushing\
#                      the value onto the end of the list, and then calling\
#                      the bubbleUp method from the last index of the list\
#\
#           bubble_up: takes in an index, and considers the element at that\
#                      index to be a child. Continues to swap that child with\
#                      its parent value if the heap comparator condition is\
#                      not fulfilled\
#\
#         remove_peak: removes the peak element from the heap and returns it.\
#                      Should begin by swapping the 0th-index element with the\
#                      last element in the storage list. Uses bubbleDown\
#                      method from the 0th index\
#\
#         bubble_down: takes in an index, and considers the element at this\
#                      index to be the parent. Continues to swap this parent\
#                      element with its children if the heap comparator\
#                      condition is not fulfilled\
#\
#              remove: takes in a value and (if it exists in the heap),\
#                      removes that value from the heap data structure and\
#                      returns it. Should rearrange the rest of the heap to\
#                      ensure the heap comparator conditions are fulfilled\
#                      for all of its elements\
#\
#\
#\
#  Input:  N/A\
#  Output: A Heap instance\
#\
#  What are the time and auxilliary space complexities of the various methods?\
#\
\
\cf5 class \cf6 Heap:\
\
    \cf5 def \cf7 __init__\cf6 (\cf8 self\cf5 , \cf6 type=\cf9 'min'\cf6 ):\
        \cf2 # YOUR WORK HERE\
        \cf8 self\cf6 .storage = []\
        \cf5 if \cf6 type == \cf9 'min'\cf6 :\
            \cf8 self\cf6 .type = \cf9 'min'\
        \cf5 else\cf6 :\
            \cf8 self\cf6 .type = \cf9 'max'\
\
\
    \cf2 # Time Complexity: O(1)\
    # Auxiliary Space Complexity: O(1)\
    \cf5 def \cf10 compare\cf6 (\cf8 self\cf5 , \cf6 a\cf5 , \cf6 b):\
        \cf2 # YOUR WORK HERE\
        \cf5 if\cf6 (\cf8 self\cf6 .type == \cf9 'min' \cf5 and \cf8 self\cf6 .storage[a] <= \cf8 self\cf6 .storage[b]):\
            \cf5 return True\
        elif\cf6 (\cf8 self\cf6 .type == \cf9 'min' \cf5 and \cf8 self\cf6 .storage[a] > \cf8 self\cf6 .storage[b]):\
            \cf5 return False\
        elif\cf6 (\cf8 self\cf6 .type == \cf9 'max' \cf5 and \cf8 self\cf6 .storage[a] < \cf8 self\cf6 .storage[b]):\
            \cf5 return False\
        else\cf6 :\
            \cf5 return True\
\
\
    \cf2 # Time Complexity: O(1)\
    # Auxiliary Space Complexity: O(1)\
    \cf5 def \cf10 swap\cf6 (\cf8 self\cf5 , \cf6 index1\cf5 , \cf6 index2):\
        \cf2 # YOUR WORK HERE\
        \cf8 self\cf6 .storage[index1]\cf5 , \cf8 self\cf6 .storage[index2] = \cf8 self\cf6 .storage[index2]\cf5 , \cf8 self\cf6 .storage[index1]\
        \cf5 return \cf8 self\
\
\
    \cf2 # Time Complexity:\
    # Auxiliary Space Complexity:\
    \cf5 def \cf10 peak\cf6 (\cf8 self\cf6 ):\
        \cf5 return \cf8 self\cf6 .storage[\cf11 0\cf6 ]\
\
    \cf2 # Time Complexity:O(N)\
    # Auxiliary Space Complexity:O(1)\
    \cf5 def \cf10 size\cf6 (\cf8 self\cf6 ):\
        \cf2 # YOUR WORK HERE\
        \cf6 size = \cf4 len\cf6 (\cf8 self\cf6 .storage)\
        \cf5 return \cf6 size\
\
    \cf2 # Time Complexity:\
    # Auxiliary Space Complexity:\
    \cf5 def \cf10 insert\cf6 (\cf8 self\cf5 , \cf6 value):\
        \cf8 self\cf6 .append(value)\
        \cf2 # YOUR WORK HERE\
        \cf5 pass\
\
    \cf2 # Time Complexity:\
    # Auxiliary Space Complexity:\
    \cf5 def \cf10 bubble_up\cf6 (\cf8 self\cf5 , \cf6 index):\
        \cf2 # YOUR WORK HERE\
        \cf5 while \cf8 self\cf6 :\
            child1 = \cf11 2\cf6 *index + \cf11 1\
            \cf6 child2 = \cf11 2\cf6 *index + \cf11 2\
            \cf6 swapWhich = compare(\cf8 self\cf5 ,\cf6 index.child1\cf5 ,\cf6 index.child2)\
            \cf5 if \cf6 swapWhich == \cf5 True\cf6 :\
                swapNow = compare(\cf8 self\cf5 ,\cf6 index\cf5 ,\cf6 child1)\
                \cf5 if \cf6 swapNow == \cf5 True\cf6 :\
                    swap(\cf8 self\cf5 , \cf6 index\cf5 , \cf6 child1)\
            \cf5 else\cf6 :\
                swapNow = compare(\cf8 self\cf5 ,\cf6 index\cf5 ,\cf6 child2)\
                \cf5 if \cf6 swapNow == \cf5 True\cf6 :\
                    swap(\cf8 self\cf5 , \cf6 index\cf5 , \cf6 child2)\
\
\
\
    \cf2 # Time Complexity:\
    # Auxiliary Space Complexity:\
    \cf5 def \cf10 remove_peak\cf6 (\cf8 self\cf6 ):\
        \cf2 # YOUR WORK HERE\
        \cf5 pass\
\
    \cf2 # Time Complexity:\
    # Auxiliary Space Complexity:\
    \cf5 def \cf10 bubble_down\cf6 (\cf8 self\cf5 , \cf6 index):\
        \cf2 # YOUR WORK HERE\
        \cf5 pass\
\
    \cf2 # Time Complexity:\
    # Auxiliary Space Complexity:\
    \cf5 def \cf10 remove\cf6 (\cf8 self\cf5 , \cf6 value):\
        \cf2 # YOUR WORK HERE\
        \cf5 pass\
\
\
\cf2 ############################################################\
###############  DO NOT TOUCH TEST BELOW!!!  ###############\
############################################################\
\
# custom assert function to handle tests\
# input: count \{List\} - keeps track out how many tests pass and how many total\
#        in the form of a two item array i.e., [0, 0]\
# input: name \{String\} - describes the test\
# input: test \{Function\} - performs a set of operations and returns a boolean\
#        indicating if test passed\
# output: \{None\}\
\cf5 def \cf10 expect\cf6 (count\cf5 , \cf6 name\cf5 , \cf6 test):\
    \cf5 if \cf6 (count \cf5 is None or not \cf4 isinstance\cf6 (count\cf5 , \cf4 list\cf6 ) \cf5 or \cf4 len\cf6 (count) != \cf11 2\cf6 ):\
        count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
    \cf5 else\cf6 :\
        count[\cf11 1\cf6 ] += \cf11 1\
\
    \cf6 result = \cf9 'false'\
    \cf6 error_msg = \cf5 None\
    try\cf6 :\
        \cf5 if \cf6 test():\
            result = \cf9 ' true'\
            \cf6 count[\cf11 0\cf6 ] += \cf11 1\
    \cf5 except \cf4 Exception \cf5 as \cf6 err:\
        error_msg = \cf4 str\cf6 (err)\
\
    \cf4 print\cf6 (\cf9 '  ' \cf6 + (\cf4 str\cf6 (count[\cf11 1\cf6 ]) + \cf9 ')   '\cf6 ) + result + \cf9 ' : ' \cf6 + name)\
    \cf5 if \cf6 error_msg \cf5 is not None\cf6 :\
        \cf4 print\cf6 (\cf9 '       ' \cf6 + error_msg + \cf9 '\cf5 \\n\cf9 '\cf6 )\
\
\cf2 # compare if two flat lists are equal\
\cf5 def \cf10 lists_equal\cf6 (lst1\cf5 , \cf6 lst2):\
    \cf5 if \cf4 len\cf6 (lst1) != \cf4 len\cf6 (lst2):\
        \cf5 return False\
    for \cf6 i \cf5 in \cf4 range\cf6 (\cf11 0\cf5 , \cf4 len\cf6 (lst1)):\
        \cf5 if \cf6 lst1[i] != lst2[i]:\
            \cf5 return False\
    return True\
\
\
\
\cf4 print\cf6 (\cf9 'Heap Class'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 isinstance\cf6 (work\cf5 , \cf4 object\cf6 )\
\
\
expect(test_count\cf5 , \cf9 'able to create an instance'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'storage'\cf6 )\
\
\
expect(test_count\cf5 , \cf9 'has storage property'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'type'\cf6 )\
\
\
expect(test_count\cf5 , \cf9 'has type property'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 isinstance\cf6 (work.storage\cf5 , \cf4 list\cf6 )\
\
\
expect(test_count\cf5 , \cf9 'default storage set to a list'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf6 work.type == \cf9 'min'\
\
\
\cf6 expect(test_count\cf5 , \cf9 'default type property is set to \cf5 \\'\cf9 min\cf5 \\'\cf9 '\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    \cf5 return \cf6 work.type == \cf9 'max'\
\
\
\cf6 expect(test_count\cf5 , \cf9 'default type property can be set to \cf5 \\'\cf9 max\cf5 \\'\cf9 '\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap compare method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'compare'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'compare'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has compare method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage.append(\cf11 1\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    \cf5 return \cf6 work.compare(\cf11 0\cf5 , \cf11 1\cf6 ) \cf5 is True\
\
\
\cf6 expect(test_count\cf5 , \cf9 'returns true for minheap if element at first argument index is less than element at second argument index'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    work.storage.append(\cf11 1\cf6 )\
    \cf5 return \cf6 work.compare(\cf11 0\cf5 , \cf11 1\cf6 ) \cf5 is False\
\
\
\cf6 expect(test_count\cf5 , \cf9 'returns false for minheap if element at first argument index is greater than element at second argument index'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    work.storage.append(\cf11 1\cf6 )\
    \cf5 return \cf6 work.compare(\cf11 0\cf5 , \cf11 1\cf6 ) \cf5 is True\
\
\
\cf6 expect(test_count\cf5 , \cf9 'returns true for maxheap if element at first argument index is greater than element at second argument index'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage.append(\cf11 1\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    \cf5 return \cf6 work.compare(\cf11 0\cf5 , \cf11 1\cf6 ) \cf5 is False\
\
\
\cf6 expect(test_count\cf5 , \cf9 'returns false for maxheap if element at first argument index is less than element at second argument index'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap swap method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'swap'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'swap'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has swap method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    work.storage.append(\cf11 1\cf6 )\
    work.storage.append(\cf11 5\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    work.swap(\cf11 0\cf5 , \cf11 2\cf6 )\
    \cf5 return \cf6 work.storage[\cf11 0\cf6 ] == \cf11 10 \cf5 and \cf6 work.storage[\cf11 2\cf6 ] == \cf11 1\
\
\
\cf6 expect(test_count\cf5 , \cf9 'should be able to swap the locations of two elements given two indices'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap peak method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'peak'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'peak'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has peak method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    work.storage.append(\cf11 1\cf6 )\
    work.storage.append(\cf11 5\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    \cf5 return \cf6 work.peak() == \cf11 1\
\
\
\cf6 expect(test_count\cf5 , \cf9 'should return the 0th element of the storage array'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.insert(\cf11 2\cf6 )\
    work.insert(\cf11 5\cf6 )\
    work.insert(\cf11 10\cf6 )\
    work.insert(\cf11 1\cf6 )\
    \cf5 return \cf6 work.peak() == \cf11 1\
\
\
\cf6 expect(test_count\cf5 , \cf9 'upon building out your insert method, should return the smallest element for a minheap'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.insert(\cf11 2\cf6 )\
    work.insert(\cf11 5\cf6 )\
    work.insert(\cf11 10\cf6 )\
    work.insert(\cf11 1\cf6 )\
    \cf5 return \cf6 work.peak() == \cf11 10\
\
\
\cf6 expect(test_count\cf5 , \cf9 'upon building out your insert method, should return the largest element for a maxheap'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap size method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'size'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'size'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has size method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    work.storage.append(\cf11 1\cf6 )\
    work.storage.append(\cf11 5\cf6 )\
    work.storage.append(\cf11 10\cf6 )\
    \cf5 return \cf6 work.size == \cf11 3\
\
\
\cf6 expect(test_count\cf5 , \cf9 'returns number of elements in the storage array'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap insert method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'insert'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'insert'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has insert method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    work.insert(\cf11 5\cf6 )\
    \cf5 return \cf6 work.storage[\cf11 0\cf6 ] == \cf11 5\
\
\
\cf6 expect(test_count\cf5 , \cf9 'should be able to insert a single element'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.insert(\cf11 5\cf6 )\
    work.insert(\cf11 10\cf6 )\
    work.insert(\cf11 7\cf6 )\
    work.insert(\cf11 1\cf6 )\
    work.insert(\cf11 8\cf6 )\
    work.insert(\cf11 6\cf6 )\
    \cf5 return \cf6 work.peak() == \cf11 1\
\
\
\cf6 expect(test_count\cf5 , \cf9 'should be able to insert multiple elements into a minheap and have peak element be smallest element'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.insert(\cf11 5\cf6 )\
    work.insert(\cf11 10\cf6 )\
    work.insert(\cf11 7\cf6 )\
    work.insert(\cf11 1\cf6 )\
    work.insert(\cf11 8\cf6 )\
    work.insert(\cf11 6\cf6 )\
    \cf5 return \cf6 work.peak() == \cf11 10\
\
\
\cf6 expect(test_count\cf5 , \cf9 'should be able to insert multiple elements into a maxheap and have peak element be largest element'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap bubble_up method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'bubble_up'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'bubble_up'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has bubble_up method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 2\cf5 , \cf11 4\cf5 , \cf11 7\cf5 , \cf11 6\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 1\cf6 ]\
    work.bubble_up(\cf11 7\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should be able to \cf5 \\'\cf9 bubble up\cf5 \\'\cf9  an element if its minheap condition is not fulfilled'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 9\cf5 , \cf11 8\cf5 , \cf11 5\cf5 , \cf11 7\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 10\cf6 ]\
    work.bubble_up(\cf11 7\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should be able to \cf5 \\'\cf9 bubble up\cf5 \\'\cf9  an element if its maxheap condition is not fulfilled'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    work.bubble_up(\cf11 7\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should not perform bubbling up if minheap conditions are fulfilled'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\
    work.bubble_up(\cf11 7\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should not perform bubbling down if maxheap conditions are fulfilled'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap remove_peak method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'remove_peak'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'remove_peak'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has remove_peak method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    work.insert(\cf11 5\cf6 )\
    work.remove_peak()\
    \cf5 return \cf4 len\cf6 (work.storage) == \cf11 0\
\
\
\cf6 expect(test_count\cf5 , \cf9 'should be able to remove a single element'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    example = work.remove_peak()\
    \cf5 return \cf6 example == \cf11 1 \cf5 and \cf6 lists_equal([\cf11 2\cf5 , \cf11 4\cf5 , \cf11 7\cf5 , \cf11 6\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should be able to remove and return peak element for a minheap and rearrange minheap accordingly'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\
    example = work.remove_peak()\
    \cf5 return \cf6 example == \cf11 10 \cf5 and \cf6 lists_equal([\cf11 9\cf5 , \cf11 8\cf5 , \cf11 5\cf5 , \cf11 7\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should be able to remove and return peak element for a maxheap and rearrange maxheap accordingly'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap bubble_down method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'bubble_down'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'bubble_down'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has bubble_down method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    work.bubble_down(\cf11 0\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 1\cf5 , \cf11 4\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 10\cf5 , \cf11 9\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should be able to \cf5 \\'\cf9 bubble down\cf5 \\'\cf9  an element if its minheap condition is not fulfilled'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 2\cf5 , \cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 7\cf6 ]\
    work.bubble_down(\cf11 0\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 10\cf5 , \cf11 8\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 2\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 7\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should be able to \cf5 \\'\cf9 bubble down\cf5 \\'\cf9  an element if its maxheap condition is not fulfilled'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    work.bubble_down(\cf11 0\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should not perform bubbling down if minheap conditions are fulfilled'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\
    work.bubble_down(\cf11 0\cf6 )\
    \cf5 return \cf6 lists_equal([\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\cf5 , \cf6 work.storage)\
\
\
expect(test_count\cf5 , \cf9 'should not perform bubbling down if maxheap conditions are fulfilled'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
\
\cf4 print\cf6 (\cf9 'Heap remove method'\cf6 )\
test_count = [\cf11 0\cf5 , \cf11 0\cf6 ]\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap()\
    \cf5 return \cf4 hasattr\cf6 (work\cf5 , \cf9 'remove'\cf6 ) \cf5 and \cf4 callable\cf6 (\cf4 getattr\cf6 (work\cf5 , \cf9 'remove'\cf6 ))\
\
\
expect(test_count\cf5 , \cf9 'has remove method'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    example = work.remove(\cf11 10\cf6 )\
    \cf5 return \cf6 example == \cf11 10 \cf5 and \cf6 lists_equal(work.storage\cf5 , \cf6 [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 6\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 7\cf5 , \cf11 8\cf6 ])\
\
\
expect(test_count\cf5 , \cf9 'is able to remove specified value from minheap'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\
    example = work.remove(\cf11 6\cf6 )\
    \cf5 return \cf6 example == \cf11 6 \cf5 and \cf6 lists_equal(work.storage\cf5 , \cf6 [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 7\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 5\cf5 , \cf11 2\cf6 ])\
\
\
expect(test_count\cf5 , \cf9 'is able to remove specified value from maxheap'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    example = work.remove(\cf11 6\cf6 )\
    \cf5 return \cf6 example == \cf11 6 \cf5 and \cf6 lists_equal(work.storage\cf5 , \cf6 [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf6 ])\
\
\
expect(test_count\cf5 , \cf9 'is able to remove last value from minheap'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\
    example = work.remove(\cf11 7\cf6 )\
    \cf5 return \cf6 example == \cf11 7 \cf5 and \cf6 lists_equal(work.storage\cf5 , \cf6 [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf6 ])\
\
\
expect(test_count\cf5 , \cf9 'is able to remove last value from maxheap'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'min'\cf6 )\
    work.storage = [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ]\
    work.remove(\cf11 3\cf6 )\
    \cf5 return \cf6 lists_equal(work.storage\cf5 , \cf6 [\cf11 1\cf5 , \cf11 2\cf5 , \cf11 7\cf5 , \cf11 4\cf5 , \cf11 9\cf5 , \cf11 10\cf5 , \cf11 8\cf5 , \cf11 6\cf6 ])\
\
\
expect(test_count\cf5 , \cf9 'does not remove anything from minheap if value does not exist'\cf5 , \cf6 test)\
\
\
\cf5 def \cf10 test\cf6 ():\
    work = Heap(\cf9 'max'\cf6 )\
    work.storage = [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ]\
    work.remove(\cf11 4\cf6 )\
    \cf5 return \cf6 lists_equal(work.storage\cf5 , \cf6 [\cf11 10\cf5 , \cf11 9\cf5 , \cf11 5\cf5 , \cf11 8\cf5 , \cf11 3\cf5 , \cf11 6\cf5 , \cf11 2\cf5 , \cf11 7\cf6 ])\
\
\
expect(test_count\cf5 , \cf9 'does not remove anything from maxheap if value does not exist'\cf5 , \cf6 test)\
\
\cf4 print\cf6 (\cf9 'PASSED: ' \cf6 + \cf4 str\cf6 (test_count[\cf11 0\cf6 ]) + \cf9 ' / ' \cf6 + \cf4 str\cf6 (test_count[\cf11 1\cf6 ]) + \cf9 '\cf5 \\n\\n\cf9 '\cf6 )\
\
}