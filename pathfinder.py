import sys
from tree import treeBuilder

build = treeBuilder()


if len(sys.argv) != 4:
    print "\n Incorrect call \n Try: python pathfinder.py text.txt 'first name' 'second name'\n"

else:
    """
    Collecting arguments from console
    The fileArg holds the text file to be read from. firstArg and secondArg holds the names to checked.
    """
    for arg in sys.argv:
        fileArg = sys.argv[1]
        firstArg = sys.argv[2]
        secondArg = sys.argv[3]

    nameInput1 = " ".join(firstArg.split()).lower()
    nameInput2 = " ".join(secondArg.split()).lower()

    fr = open(fileArg)
    theFile = fr.read()
    listStrip = theFile.strip()
    firstSplit = listStrip.split('|')
    firstSplit = [str(value).strip() for value in firstSplit]  # removes whitespace from values in the list

    employeeIdList = []
    nameList = []
    managerIdList = []

    listLength = len(firstSplit)  # currently = 37
    x = 0

    while x < listLength - 1:
        if x % 4 == 0:
            employeeIdList.append(firstSplit[x + 1])
            nameList.append(firstSplit[x+2])
            if x == 4:
                managerIdList.append(firstSplit[0])
            else:
                managerIdList.append(firstSplit[x + 3])

        x += 1

    """
    print firstSplit
    print employeeIdList
    print managerIdList
    print nameList
    """

    """
    *********Building the Trees*********

    Constructing the organization tree with names of employees
    """
    oChart = build.binaryTree(nameList[1])
    build.insertLeft(oChart, nameList[2])
    build.insertRight(oChart, nameList[3])
    build.insertLeft(build.getLeftChild(oChart), nameList[4])
    build.insertLeft(build.getRightChild(oChart), nameList[5])
    build.insertRight(build.getRightChild(oChart), nameList[6])
    build.insertLeft(build.getLeftChild(build.getLeftChild(oChart)), nameList[7])
    build.insertRight(build.getLeftChild(build.getLeftChild(oChart)), nameList[8])

    """
    Constructing the organization tree with manager ID
    The tree root has an empty (" ") manager ID, the sting "N" is used as a placeholder
    """
    mChart = build.binaryTree('N')
    build.insertLeft(mChart, managerIdList[2])
    build.insertRight(mChart, managerIdList[3])
    build.insertLeft(build.getLeftChild(mChart), managerIdList[4])
    build.insertLeft(build.getRightChild(mChart), managerIdList[5])
    build.insertRight(build.getRightChild(mChart), managerIdList[6])
    build.insertLeft(build.getLeftChild(build.getLeftChild(mChart)), managerIdList[7])
    build.insertRight(build.getLeftChild(build.getLeftChild(mChart)), managerIdList[8])

    """
    Constructing the organization tree with Employee ID
    """
    eChart = build.binaryTree(employeeIdList[1])
    build.insertLeft(eChart, employeeIdList[2])
    build.insertRight(eChart, employeeIdList[3])
    build.insertLeft(build.getLeftChild(eChart), employeeIdList[4])
    build.insertLeft(build.getRightChild(eChart), employeeIdList[5])
    build.insertRight(build.getRightChild(eChart), employeeIdList[6])
    build.insertLeft(build.getLeftChild(build.getLeftChild(eChart)), employeeIdList[7])
    build.insertRight(build.getLeftChild(build.getLeftChild(eChart)), employeeIdList[8])
    """
    ***********End of Tree construction*********
    """


    """
    nTreeRoot, nTreeLeft, nTreeRight are the Employee Name tree Root, Left subtree and Right subtree respectively;
    mTreeRoot, mTreeLeft, mTreeRight are the Manager ID tree Root, Left subtree and Right subtree respectively; while
    eTreeRoot, eTreeLeft, eTreeRight are the Employing ID tree Root, Left subtree and Right subtree respectively.
    """
    nTreeRoot = oChart[0]
    nTreeLeft = oChart[1]
    nTreeRight = oChart[2]

    mTreeRoot = mChart[0]
    mTreeLeft = mChart[1]
    mTreeRight = mChart[2]

    eTreeRoot = eChart[0]
    eTreeLeft = eChart[1]
    eTreeRight = eChart[2]


    #Tree traverse
    def treeTraverse(t, treeTypes=(list, tuple)):
        if isinstance(t, treeTypes):
            for valueX in t:
                for subValue in treeTraverse(valueX):
                    yield subValue
        else:
            yield t


    # Takes in the search name and then returns the index, manager id and tree position(like root or left)
    def findInput(searchname):
        if searchname in nRootTransverse:
            indexholder = nRootTransverse.index(searchname)
            managerId = mRootTransverse[indexholder]
            return indexholder, managerId, 'Root'

        elif searchname in nLeftTransverse:
            indexholder = nLeftTransverse.index(searchname)
            managerId = mLeftTransverse[indexholder]
            return indexholder, managerId, 'Left'

        elif searchname in nRightTransverse:
            indexholder = nRightTransverse.index(searchname)
            managerId = mRightTransverse[indexholder]
            return indexholder, managerId, 'Right'

        else:
            print '\n', searchname, ' not found on my tree'
            return False


    """
    # traverse the root, left subtree and right subtree for the name tree and manager id tree.
    This uses the treeTraverse function to traverse the tree in 3 different part. First the root
    is traversed and then the output is stored in a list[]. The left subtree is then traversed followed by the
    right subtree. The output is stored in a list.

    nRootTransverse  = holds the root node, which is the name at the top of the organization chat
    nLeftTransverse = holds the left subtree, which are the names on the left side of the organization chart
    nLeftTransverse = hold the right subtree, which are the name on the right side of the organization chart

    mRootTransverse, mLeftTransverse and mRightTransverse hold the manager id for the traversed tree

    eRootTransverse, eLeftTransverse and eRightTransverse hold the employee id for the traversed tree
    """
    nRootTransverse = list(treeTraverse(nTreeRoot))
    nLeftTransverse = list(treeTraverse(nTreeLeft))
    nRightTransverse = list(treeTraverse(nTreeRight))

    mRootTransverse = list(treeTraverse(mTreeRoot))
    mLeftTransverse = list(treeTraverse(mTreeLeft))
    mRightTransverse = list(treeTraverse(mTreeRight))

    eRootTransverse = list(treeTraverse(eTreeRoot))
    eLeftTransverse = list(treeTraverse(eTreeLeft))
    eRightTransverse = list(treeTraverse(eTreeRight))


    """
    This converts the contents of the employee name tree to lowercase.
    So if the initial tree was = ["A", "B", "C"] it then becomes ["a", "b", "c"]
    """
    nRootTransverse = [x.lower() for x in nRootTransverse]
    nLeftTransverse = [x.lower() for x in nLeftTransverse]
    nRightTransverse = [x.lower() for x in nRightTransverse]


    """
    The "findParentRight" locates the immediate parent of a right subtree which has the same employee ID.
    The "findParentLeft" does the same thing but for the left subtree.
    Both functions accepts 2 arguments which are lists (argv1[] and argv2[]).
    Both functions return the parent node for 2 children on the same level (Manager ID) and the parent employee id

    The title() function capitalize the sting output. eg. 'name' would be 'Name'
    """
    def findParentRight(argv1, argv2):
        if argv1[0] > argv2[0]:
            parent = nRightTransverse[argv2[0]-1] + ' (' + str(eRightTransverse[argv2[0]-1]) + ')'
            return parent.title()
        else:
            parent = nRightTransverse[argv1[0]-1] + ' (' + str(eRightTransverse[argv1[0]-1]) + ')'
            return parent.title()


    # find parent of a left subtree
    def findParentLeft(argv1, argv2):
        if argv1[0] > argv2[0]:
            parent = nLeftTransverse[argv2[0]-1] + ' (' + str(eLeftTransverse[argv2[0]-1]) + ')'
            return parent
        else:
            parent = nLeftTransverse[argv1[0]-1] + ' (' + str(eLeftTransverse[argv1[0]-1]) + ')'
            return parent.title()


    """
    The "path" function locates and returns the path between two names on the organization chart.
    The function accepts two arguments, then check if they are on the same level (ie, with the same manager id), on the
    same side of the tree (ie, if they are both on the left or right or on different sides).

    The function also checks if the names entered are from the "left -> Right", "Right -> Left", or from Root to either
    left or write.

    The .title() function capitalize the sting output. eg. 'name' would be 'Name'

    An example of the path function output is as follows:
    path("a","c") =>   a (1) -> b (2) <- c (3)

    The number in the bracket is the employee id
    """
    def path(argv1, argv2):
        if argv1[1] == argv2[1] and argv1[2] == argv2[2]:  # if both entries have same manager id and are on same Tree side
            if argv1 == argv2:          # if both entries are the same person
                if argv1[2] == 'Root':
                    print '\n', nRootTransverse[argv1[0]].title(), '(' + str(eRootTransverse[argv1[0]]) + ')', '->', nRootTransverse[argv2[0]].title(), '(' + str(eRootTransverse[argv2[0]]) + ')', '\n'
                elif argv1[2] == 'Left':
                    print '\n', nLeftTransverse[argv1[0]].title(), '(' + str(eLeftTransverse[argv1[0]]) + ')',  '->', nLeftTransverse[argv2[0]].title(), '(' + str(eLeftTransverse[argv2[0]]) + ')',  '\n'
                else:
                    print '\n', nRightTransverse[argv1[0]].title(), '(' + str(eRightTransverse[argv1[0]]) + ')' '->', nRightTransverse[argv2[0]].title(), '(' + str(eRightTransverse[argv2[0]]) + ')',  '\n'

            else:           # if both entries are different people
                if argv1[2] == 'Left':
                    print '\n', nLeftTransverse[argv1[0]].title(), '(' + str(eLeftTransverse[argv1[0]]) + ')', '->', findParentLeft(argv1, argv2), '<-', nLeftTransverse[argv2[0]].title(), '(' + str(eLeftTransverse[argv2[0]]) + ')', '\n'
                elif argv1[2] == 'Right':
                    print '\n', nRightTransverse[argv1[0]].title(), '(' + str(eRightTransverse[argv1[0]]) + ')', '->', findParentRight(argv1, argv2), '<-', nRightTransverse[argv2[0]].title(), '(' + str(eRightTransverse[argv2[0]]) + ')', '\n'

        elif argv1[2] != argv2[2]:  # if the entries are from different sides of the tree. ie one from left and other right
            if argv1[2] == 'Left':           # if the first name is from the left subtree and second name is from the right
                if argv2[2] == 'Root':      # checks if the second input is the root node
                    tempLHolder = [nLeftTransverse[argv1[0]], ' (' + str(eLeftTransverse[argv1[0]]) + ')', ' -> ']       # tempLHolder[] holds the names and their paths

                    j = argv1[0]-1
                    for i in range(argv1[0], -1, -1):
                        if j != -1:
                            if mLeftTransverse[i] != mLeftTransverse[j]:
                                tempLHolder.append(nLeftTransverse[j])                 # appends the name
                                tempLHolder.append(' (' + str(eLeftTransverse[j]) + ')')        # appends the employee id
                                tempLHolder.append(' -> ')
                        j -= 1
                    tempLHolder.append(nRootTransverse[argv2[0]])                      # appends the root
                    tempLHolder.append(' (' + str(eRootTransverse[argv2[0]]) + ')')     # appends the root employee id


                    print '\n', ''.join(str(i) for i in tempLHolder).title(), '\n'

                else:
                    tempLHolder = [nLeftTransverse[argv1[0]],  ' (' + str(eLeftTransverse[argv1[0]]) + ')', ' -> ']  # tempLHolder[] holds the names and their paths

                    j = argv1[0]-1
                    for i in range(argv1[0], -1, -1):
                        if j != -1:
                            if mLeftTransverse[i] != mLeftTransverse[j]:
                                tempLHolder.append(nLeftTransverse[j])                          # appends the name
                                tempLHolder.append(' (' + str(eLeftTransverse[j]) + ')')        # appends the employee id
                                tempLHolder.append(' -> ')
                        j -= 1

                    tempLHolder.append(nRootTransverse[0])                 # This appends the Root node to tempLHolder list
                    tempLHolder.append(' (' + str(eRootTransverse[0]) + ')')     # appends the root employee id

                    j = argv2[0]-1                                  # This now starts to append the right side of tree
                    for i in range(argv2[0], -1, -1):
                        if j != -1:
                            if mRightTransverse[i] != mRightTransverse[j]:
                                tempLHolder.append(' <- ')
                                tempLHolder.append(nRightTransverse[j])                         # appends the name
                                tempLHolder.append(' (' + str(eRightTransverse[j]) + ')')       # appends the employee id
                        j -= 1
                    tempLHolder.append(' <- ')
                    tempLHolder.append(nRightTransverse[argv2[0]])              # appends the second input
                    tempLHolder.append(' (' + str(eRightTransverse[argv2[0]]) + ')')     # appends the second input employee id

                    """
                    The content of the tempLHolder list which is the path from 'Left' -> 'Right'
                    is printed on a single line. Output is like c -> b -> a <- d <- e

                    The title() function capitalize the sting output. eg. 'name' would be 'Name'
                    """
                    print '\n', ''.join(str(i) for i in tempLHolder).title(), '\n'

            elif argv1[2] == 'Right':          # if the first name is from the Right subtree and Second name from the left
                if argv2[2] == 'Root':          # checks if the second input is the root node
                    tempRHolder = [nRightTransverse[argv1[0]],  ' (' + str(eRightTransverse[argv1[0]]) + ')', ' -> ']      # tempRHolder[] holds the names and their paths
                    j = argv1[0]-1
                    for i in range(argv1[0], -1, -1):
                        if j != -1:
                            if mRightTransverse[i] != mRightTransverse[j]:
                                tempRHolder.append(nRightTransverse[j])
                                tempRHolder.append(' (' + str(eRightTransverse[j]) + ')')
                                tempRHolder.append(' -> ')
                        j -= 1
                    tempRHolder.append(nRootTransverse[argv2[0]])
                    tempRHolder.append(' (' + str(eRootTransverse[argv2[0]]) + ')')     # appends the root employee id

                    print '\n', ''.join(str(i) for i in tempRHolder).title(), '\n'

                else:                   # that is when second input is from the left subtree
                    tempRHolder = [nRightTransverse[argv1[0]],  ' (' + str(eRightTransverse[argv1[0]]) + ')', ' -> ']      # tempRHolder[] holds the names and their paths

                    j = argv1[0]-1
                    for i in range(argv1[0], -1, -1):
                        if j != -1:
                            if mRightTransverse[i] != mRightTransverse[j]:
                                tempRHolder.append(nRightTransverse[j])
                                tempRHolder.append(' (' + str(eRightTransverse[j]) + ')')
                                tempRHolder.append(' -> ')
                        j -= 1

                    tempRHolder.append(nRootTransverse[0])      # This appends the Root node to tempRHolder list
                    tempRHolder.append(' (' + str(eRootTransverse[0]) + ')')

                    j = 1
                    for i in range(argv2[0]):
                        if j != 3:
                            if mLeftTransverse[i] != mLeftTransverse[j]:
                                tempRHolder.append(' <- ')
                                tempRHolder.append(nLeftTransverse[i])
                                tempRHolder.append(' (' + str(eLeftTransverse[i]) + ')')
                        j += 1
                    tempRHolder.append(' <- ')
                    tempRHolder.append(nLeftTransverse[argv2[0]])
                    tempRHolder.append(' (' + str(eLeftTransverse[argv2[0]]) + ')')     # appends the second input employee id

                    """
                    The content of the tempRHolder list which is the path from 'Right' -> 'Left'
                    is printed on a single line. Output is like e -> d -> a <- b <- c

                    The title() function capitalize the sting output. eg. 'name' would be 'Name'
                    """
                    print '\n', ''.join(str(i) for i in tempRHolder).title(), '\n'

            elif argv1[2] == 'Root':            # checks if the first name is the root of the tree
                if argv2[2] == 'Left':          # checks if the second name is on the left subtree
                    tempLHolder = [nLeftTransverse[argv2[0]], ' (' + str(eLeftTransverse[argv2[0]]) + ')', ' -> ']       # tempLHolder[] holds the names, employee id and their paths

                    j = argv2[0]-1              # j is one less than the array index of the second name.
                    for i in range(argv2[0], -1, -1):
                        if j != -1:
                            if mLeftTransverse[i] != mLeftTransverse[j]:
                                tempLHolder.append(nLeftTransverse[j])
                                tempLHolder.append(' (' + str(eLeftTransverse[j]) + ')')
                                tempLHolder.append(' -> ')
                        j -= 1
                    tempLHolder.append(nRootTransverse[argv1[0]])
                    tempLHolder.append(' (' + str(eRootTransverse[0]) + ')')

                    print '\n', ''.join(str(i) for i in tempLHolder).title(), '\n'

                else:                                               # this runs when the second value is on the right side
                    tempRHolder = [nRightTransverse[argv2[0]], ' (' + str(eRightTransverse[argv2[0]]) + ')', ' -> ']      # tempRHolder[] holds the names and their paths

                    j = argv2[0]-1
                    for i in range(argv2[0], -1, -1):
                        if j != -1:
                            if mRightTransverse[i] != mRightTransverse[j]:
                                tempRHolder.append(nRightTransverse[j])
                                tempRHolder.append(' (' + str(eRightTransverse[j]) + ')')
                                tempRHolder.append(' -> ')
                        j -= 1
                    tempRHolder.append(nRootTransverse[argv1[0]])
                    tempRHolder.append(' (' + str(eRootTransverse[argv1[0]]) + ')')

                    print '\n', ''.join(str(i) for i in tempRHolder).title(), '\n'

        elif argv1[2] == argv2[2]:           # checks if both entries are on the same side of the tree but with different manager id
            if argv1[2] == 'Left':
                if argv1[0] < argv2[0]:      # check for the higher node by looking for the input with the lesser list index
                    top = argv1
                    lower = argv2
                elif argv1[0] > argv2[0]:
                    top = argv2
                    lower = argv1

                tempLHolder = [nLeftTransverse[lower[0]], ' (' + str(eLeftTransverse[lower[0]]) + ')', ' -> ']       # tempLHolder[] holds the names and their paths

                j = lower[0]-1              # j is one less than the array index of the lowest index.
                for i in range(lower[0], 1, -1):    # Loop runs in reverse within the range of the lowest index & stops at 1
                    if j != top[0]:                 # This stops the loop from appending the name with the top index
                        if mLeftTransverse[i] != mLeftTransverse[j]:
                            tempLHolder.append(nLeftTransverse[j])
                            tempLHolder.append(' (' + str(eLeftTransverse[j]) + ')')
                            tempLHolder.append(' -> ')
                    j -= 1
                tempLHolder.append(nLeftTransverse[top[0]])         # This appends the final name to the list
                tempLHolder.append(' (' + str(eLeftTransverse[top[0]]) + ')')

                print '\n', ''.join(str(i) for i in tempLHolder).title(), '\n'


            elif argv1[2] == 'Right':
                if argv1[0] < argv2[0]:      # check for the higher node by looking for the input with the lesser list index
                    top = argv1
                    lower = argv2
                elif argv1[0] > argv2[0]:
                    top = argv2
                    lower = argv1

                tempRHolder = [nRightTransverse[lower[0]], ' (' + str(eRightTransverse[lower[0]]) + ')', ' -> ']       # tempRHolder[] holds the names and their paths

                j = lower[0]-1              # j is one less than the array index of the lowest index.
                for i in range(lower[0], 1, -1):    # Loop runs in reverse within the range of the lowest index & stops at 1
                    if j != top[0]:                 # This stops the loop from appending the name with the top index
                        if mRightTransverse[i] != mRightTransverse[j]:
                            tempRHolder.append(nRightTransverse[j])
                            tempRHolder.append(' (' + str(eRightTransverse[j]) + ')')
                            tempRHolder.append(' -> ')
                    j -= 1
                tempRHolder.append(nRightTransverse[top[0]])         # This appends the final name to the list
                tempRHolder.append(' (' + str(eRightTransverse[top[0]]) + ')')

                print '\n', ''.join(str(i) for i in tempRHolder).title(), '\n'


    """
    firstName holds the return values from the findInput function for the first name, while
    secondName holds the return value for the second name.
    """
    firstName = findInput(nameInput1)           # calls the findInput function to check if the name is on the tree
    secondName = findInput(nameInput2)

    if firstName is False or secondName is False:
        print '\nCheck the names again!!!\n'

    else:
        """
        path accepts two parameters and then returns the
        path between the two names on the organization chart.
        """
        path(firstName, secondName)